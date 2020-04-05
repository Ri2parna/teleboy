import os
from youtube import isYoutubeUrl, downloadYoutubeVideo
from instagram import *
from app import BOT_URL
# --------------------------------------PARSING FUNCTION-------------------------------------
def parse_message(string, id):
    #check for instagram link
	if(isInstagramUrl(string)):
		send_chat_action(id,0)
		image_url = getImageLink(string) #get url of the image
		downloadImage(image_url) # download the image in images/test.jpg
		print(send_photo(id,'./images/test.jpg')) # send the photo to the user
    #check for youtube link
	elif(isYoutubeUrl(string)):
		print(send_chat_action(id,1))
		file_location = downloadYoutubeVideo(url=string)
		if(file_location):
			print(send_video(id,file_location))
			os.remove(file_location)
		else:
			print(send_message(id,'Could not download the link'))
	else:
		print(send_message(id, string))
# --------------------------------------------OTHER FUNCTIONS------------------------------------

def get_chat_data(dictData):
	current_chat_id = dictData['message']['chat']['id']
	name = dictData['message']['chat']['first_name']
	message_text = dictData['message']['text']
	return(current_chat_id, name, message_text)

def send_chat_action(chatId, type):
	action_type = ['upload_photo', 'upload_video', 'upload_audio', 'upload_document']
	message_url = BOT_URL + 'sendChatAction'
	action = {'action': action_type[type]}
	return (requests.post(message_url + '?chat_id={}'.format(chatId), action=action))
# send a text message to the user
def send_message(chatId, message):
	message_url = BOT_URL + 'sendMessage'
	json_data = {
        "chat_id": chatId,
        "text": message,
    }
	return (requests.post(message_url, json=json_data))

#send a photo to the user
def send_photo(chat_id, photo_location):
	message_url = BOT_URL + 'sendPhoto'
	files = {'photo': open('./images/test.jpg','rb')}
	return(requests.post(message_url + '?chat_id={}'.format(chat_id), files=files))

def send_video(chat_id, video_location):
	message_url = BOT_URL + 'sendVideo'
	files = {'video': open(video_location,'rb')}
	return (requests.post(message_url + '?chat_id={}'.format(chat_id), files=files))