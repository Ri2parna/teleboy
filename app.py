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
# -----------------------------------IMPORTS AND LIBRARIES--------------------------------
BOT_URL = 'https://api.telegram.org/bot1135130528:AAG9gKH4NGjRZVlnZpT9DuSZ6W_tsVhcOQw/'
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