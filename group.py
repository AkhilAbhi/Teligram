from config import *
from chanel import *
from mong import *

def grp(client,message):
  print(message)
  if message.service:
    print("user activity")
    pass
  else:
    print("serching")
    query = message.text
    movieSerc(client,message,query)