#post an image in instagram using python
from instapy_cli import client

#Give your username and password
username = 'username'
password = 'password'

#image in same directory or specify whole directory
#support only jpg/jpeg/png images
image = 'image.jpg'

#Caption is optional
caption = '#picoftheday#instamood#instapic#likeforlike'

with client(username,password) as user:
	user.upload(image,caption)
