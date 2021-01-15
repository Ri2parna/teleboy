"""
	chat_id = dictData-->message-->from-->id
	userdata = dictData-->message-->from-->id
			   dictData-->message-->from-->is_bot
			   dictData-->message-->from-->username
			   dictData-->message-->from-->language_code
	chatDetails = dictData-->message-->chat-->id
				  dictData-->message-->chat-->first_name
				  dictData-->message-->chat-->username
				  dictData-->message-->chat-->type
	date = dictData-->message-->date
	message_text = dictData-->message-->text

"""
# ----------------------------------- GET ENVIRONMENT VARIABLES --------------------------------

# for reading environment variables provided without revealing the code
from os.path import join, dirname

ENV_VARIABLES = dict();
def process_and_add(key, values):
    if(ENV_VARIABLES.get(key)):
        pass
    else:
        ENV_VARIABLES.update({key: value.strip("\"")})

with open(join(dirname(__file__), ".env")) as f:
    for lines in f:
        key, value = lines.strip().split("=")
        process_and_add(key, value)

# -----------------------------------IMPORTS AND LIBRARIES--------------------------------
BOT_URL = ENV_VARIABLES.get('BOT_URL'); 
from flask import Flask, request, jsonify
import requests
from bot_functions import *
# -------------------------------------DRIVER FUNCTION--------------------------------------
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def driver_function():
	if(request.method == 'POST'):
		dictData = request.get_json()
		current_chat_id, name, message_text = get_chat_data(dictData)
		parse_message(message_text, current_chat_id)
	return('OK', 200)