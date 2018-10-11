# ML0002
This is a simple tool to help in you finish LAMS online course. No GUI is required, as we believe in simplicity at its finest.
Therefore, Keep Calm and Keep the Brute Force going!

## PROJECT REQUIREMENTS
- Python 3.6
- Everything in the requirement.txt

## DEPENDENCIES INSTALLATION
Easy and simple. Just use `pip install` like so:

```
$ pip install -r requirements.txt --no-index --find-links file:///tmp/packages
```

## Usage

### Setup:
Create a config.json file. The content of JSON file are configuration you can find when launching the LAMS Quiz pop-up. Simply inspect the element The json file should contain the following information:
- JSESSIONID
- ntutestcookie
- mobi
- NTUDMTYPE
- WT_FPC
- NSC_mcwtws_oed3tga_mbnt.ouv.fev.th

Under Network (inside inspect mode), look for Request Header- Cookie and copy all values correspond to the above mentioned information. Then save your config.json file and be ready to launch your program.

### Execution
Open terminal, `$cd` to ML0002 folder and launch checkbox.py script as below:
```
python checkbox.py -s <session_map_id> -q <question_id> -n <num_of_questions> -c <path_to_json_cookies>
```
- Replace the <session_map_id> value with your sessions id. Look under inspect for <form> tag. It should be sthng like this:
  ```
  <form id="answer", name="answer", method="post", action = "/...sessionMapID = sessioMapID-82560">
  ```
- Replace the <question_id > value with your question id. Under the same <form> tag, find the <input> tag use it's value as <question_id>
- Replace the <num_of_questions> with number of checkboxes available in that particular question (will fix the misleading naming)
- Finaly, replace <path_to_json_cookie> with the path to the above mentioned config.json file.

Press enter after typing and formulating the bash as above.
Feel the magic! Thanks!

## Authors
- Timothygk
- Andre Hartanto
