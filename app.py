<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask, request, jsonify
app = Flask(__name__)
<<<<<<< HEAD

=======
def parse_message(string, id):
	if(isInstagramUrl(string)):
<<<<<<< HEAD
		image_location = getImageLink(string)
		downloadImage(image_location)
<<<<<<< HEAD
<<<<<<< HEAD
		send_photo(id,'images/test.jpg')
	else:
		send_message(id, string)
=======
		send_photo(id,open('images/test.jpg','rb'))
<<<<<<< HEAD
>>>>>>> e83f43b... Fixed parsing
=======
=======
=======
		image_url = getImageLink(string)
		downloadImage(image_url)
<<<<<<< HEAD
>>>>>>> cec371b... okay
		send_photo(id,'images/test.jpg')
>>>>>>> a77a48d... squashing bugs
=======
		send_photo(id,'./images/test.jpg')
>>>>>>> 445e4c6... okay
	else:
		send_message(id, string)
>>>>>>> b291395... might have fixed the error

def get_chat_data(dictData):
	current_chat_id = dictData['message']['chat']['id']
	name = dictData['message']['chat']['first_name']
	message_text = dictData['message']['text']
	return(current_chat_id, name, message_text)
# send a text message to the user
def send_message(chatId, message):
	message_url = BOT_URL + 'sendMessage'
	json_data = {
        "chat_id": chatId,
        "text": message,
    }
	requests.post(message_url, json=json_data)
#send a photo to the user
def send_photo(chat_id, photo_location):
<<<<<<< HEAD
	message_url = BOT_URL + 'sendPhoto'
	json_data = {
		"chat_id": chat_id,
		"file" : open(photo_location,'rb')
	}
	print(requests.post(message_url,json_data))
<<<<<<< HEAD
>>>>>>> 5cd6e13... learnt git rebase
=======
>>>>>>> 8ae7a88... i dont know what to do
=======
	message_url = BOT_URL + 'sendPhoto?chat_id=' + str(chat_id)
	print(message_url)
	image_file = { 'photo' : open(photo_location,'rb') }
<<<<<<< HEAD
	print(requests.post(message_url,image_file))
>>>>>>> 08e5ff2... fixed image upload
=======
	requests.post(message_url,image_file)
>>>>>>> cec371b... okay
=======
=======
>>>>>>> 2627d30b5fcd194d2fbabe699d0bb772ab629086
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
<<<<<<< HEAD
>>>>>>> d5879b3... New Commit part 1
=======
>>>>>>> 2627d30b5fcd194d2fbabe699d0bb772ab629086
@app.route('/', methods=['GET','POST'])
def driver_function():
	if(request.method == 'POST'):
		dictData = request.get_json()
<<<<<<< HEAD
<<<<<<< HEAD
		print(dictData)
		message_text = dictData['message']['text']
		print(message_text)
		# message_text = dictData['message']['chat']['text']
	return('OK', 200)
=======
		current_chat_id, name, message_text = get_chat_data(dictData)
		parse_message(message_text, current_chat_id)
	return('OK', 200)
>>>>>>> 5cd6e13... learnt git rebase
=======
		current_chat_id, name, message_text = get_chat_data(dictData)
		parse_message(message_text, current_chat_id)
	return('OK', 200)
>>>>>>> 2627d30b5fcd194d2fbabe699d0bb772ab629086
