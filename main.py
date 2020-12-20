import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot
from threading import Thread
from db_handler import DbHandler
import random
import time

token = "178ce7a12d102359b07682656b7268637b0aad162eb00a8085b9d2447e5292933ce597ed62126bac8a1f0"
vk = vk_api.VkApi(token=token)
long_poll = VkLongPoll(vk)


def write_message(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.getrandbits(64)})


class CheckNotes(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            notes = DbHandler.get_note_by_current_time()
            if len(notes) > 0:
                for item in notes:
                    text = ""
                    text = text + ("Дата напоминания: " + str(item[1]) + "\n" +
                                   "Содержимое: " + str(item[3]) + "\n\n")
                    write_message(item[4], text)
                    DbHandler.delete_note(item[0])
            time.sleep(0.01)


class CheckMessages(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        for event in long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    bot = VkBot(event.user_id)
                    write_message(event.user_id, bot.new_message(event.text))


CheckNotes()
CheckMessages()

while True:
    time.sleep(0.001)
