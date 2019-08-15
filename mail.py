from bs4 import BeautifulSoup as bs
import imaplib
import email
import re

while True:

	def login():
		imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
		imap.login("sharadaeml@gmail.com", "ecebpo14")
		imap.select('INBOX')
		read(imap)

	def read(imap):
		type, data = imap.search(None, '(UNSEEN)')
		
		for num in data[0].split():
			typ, data = imap.fetch(num, '(RFC822)' )
			raw_email = data[0][1]
			raw_email_string = raw_email.decode('utf-8')
			email_message = email.message_from_string(raw_email_string)
			for part in email_message.walk():
			 if part.get_content_type() == "text/plain": # ignore attachments/html
			  body = part.get_payload(decode=True)
			  soup = bs(body, 'html.parser')
			  s =  soup.find('td', text = re.compile('Address'))
			  try:
				  a = s.find_next()
				  print(a.text)
			  except AttributeError:
			  	continue
			 else:
			  continue
			# soup = bs(raw_email, 'html.parser')
			# aa = email.get_content()
			#s =  soup.find('td', text = re.compile('Address'))
			#a = s.find_next()
			# print(soup)

		# login()
		    # for i in s:
		    # 	print(i)
		    # 	print(i.get('href'))

	login()


