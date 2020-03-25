import re
from pytube import YouTube
def isYoutubeUrl(url):
	pattern = '(.*?)youtube\.com/watch\?v='
	pattern2 = '(.*?)youtu\.be\/'
	if(re.match(pattern,url)):
		return True
	elif(re.match(pattern2,url)):
		return True
	else:
		return False

def downloadYoutubeVideo(url):
	try:
		youtubeObject = YouTube(url)
		title = youtubeObject.title
		yx = (youtubeObject.streams.filter(progressive=True, subtype='mp4').first().download())
		return yx
	except:
		print('Error in downloading format 1')
		return None


if __name__ == "__main__":
	downloadYoutubeVideo("https://www.youtube.com/watch?v=8q9ofIHzmlo")
