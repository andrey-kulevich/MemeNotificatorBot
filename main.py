import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VkBot
import random


def write_message(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.getrandbits(64)})


token = "178ce7a12d102359b07682656b7268637b0aad162eb00a8085b9d2447e5292933ce597ed62126bac8a1f0"
vk = vk_api.VkApi(token=token)
long_poll = VkLongPoll(vk)

for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            bot = VkBot(event.user_id)
            write_message(event.user_id, bot.new_message(event.text))
