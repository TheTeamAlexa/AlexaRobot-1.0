# A Powerful Music And Management Bot
#Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit


import threading
from sqlalchemy import Column, String
from RocksAlexaRobot.modules.sql import BASE, SESSION
#   |----------------------------------|
#   |  Test Module by @Dr_Asad_Ali |
#   |        Kang with Credits         |
#   |----------------------------------|
class NSFWChats(BASE):
    __tablename__ = "nsfw_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

NSFWChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_nsfw(chat_id):
    try:
        chat = SESSION.query(NSFWChats).get(str(chat_id))
        if chat:
            return True
        else:
            return False
    finally:
        SESSION.close()

def set_nsfw(chat_id):
    with INSERTION_LOCK:
        nsfwchat = SESSION.query(NSFWChats).get(str(chat_id))
        if not nsfwchat:
            nsfwchat = NSFWChats(str(chat_id))
        SESSION.add(nsfwchat)
        SESSION.commit()

def rem_nsfw(chat_id):
    with INSERTION_LOCK:
        nsfwchat = SESSION.query(NSFWChats).get(str(chat_id))
        if nsfwchat:
            SESSION.delete(nsfwchat)
        SESSION.commit()


def get_all_nsfw_chats():
    try:
        return SESSION.query(NSFWChats.chat_id).all()
    finally:
        SESSION.close()

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo

