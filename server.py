__author__ = 'kens'

__author__ = 'kens'

import httplib2
import json
import requests

resp, content = httplib2.Http().request("https://api.telegram.org/bot93172737:AAEOi-Zw55fYJuft2BbmPwLAs3t7VfK5_m0/getME")
# should probably change and hide the token in the future.


print 'hi'
print resp

resp, content = httplib2.Http().request("https://api.telegram.org/bot93172737:AAEOi-Zw55fYJuft2BbmPwLAs3t7VfK5_m0/getUpdates")
print resp

#-13226782
resp, content = httplib2.Http().request("https://api.telegram.org/bot93172737:AAEOi-Zw55fYJuft2BbmPwLAs3t7VfK5_m0/GroupChat")
print resp


url = 'https://api.telegram.org/bot93172737:AAEOi-Zw55fYJuft2BbmPwLAs3t7VfK5_m0/sendMessage'
payload = {"chat_id": -13226782, 'text': 'yolo boys'}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print response
