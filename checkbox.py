import argparse
import json
import requests
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--session', type=str, required=True, help='session map id')
parser.add_argument('-q', '--question', type=str, required=True, help='question id')
parser.add_argument('-n', '--num', type=int, required=True, help='number of questions')
parser.add_argument('-c', '--cookies', type=str, default='cookies.json', help='path to cookies json file')
args = parser.parse_args()

session_map_id = args.session
question_id = args.question
num_of_questions = args.num

with open('cookies.json', 'r') as reader:
    cookies = json.load(reader)


def resubmit():
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://lams.ntu.edu.sg/lams/tool/laasse10/pages/learning/results.jsp?sessionMapID=sessionMapID-%s' % session_map_id,
        'Connection': 'keep-alive',
    }

    params = (
        ('sessionMapID', 'sessionMapID-%s' % session_map_id),
    )

    response = requests.get('https://lams.ntu.edu.sg/lams/tool/laasse10/learning/resubmit.do', headers=headers, params=params, cookies=cookies)


def sumbit(data):
    headers = {
        'Origin': 'https://lams.ntu.edu.sg',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://lams.ntu.edu.sg/lams/tool/laasse10/learning/resubmit.do?sessionMapID=sessionMapID-%s' % session_map_id,
        'Connection': 'keep-alive',
    }

    params = (
        ('sessionMapID', 'sessionMapID-%s' % session_map_id),
        ('isTimelimitExpired', 'false'),
    )

    return requests.post('https://lams.ntu.edu.sg/lams/tool/laasse10/learning/submitAll.do',
                            headers=headers, params=params, cookies=cookies, data=data)


def main():
    for mask in range(2**num_of_questions):
        data = [('questionUid0', question_id)]
        # if mask != 22: continue
        for i in range(args.num):
            if (mask >> i) & 1:
                data.append(('question0_%s' % i, 'true'))

        response = sumbit(data)

        print(response, str(bin(mask))[2:].zfill(num_of_questions), file=sys.stderr)
        if 'Next Activity' in response.text:
            print(data, file=sys.stderr)
            break

        resubmit()


if __name__ == '__main__':
    main()
