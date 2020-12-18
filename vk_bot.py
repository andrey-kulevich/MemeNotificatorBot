import requests
import bs4
from db_handler import DbHandler


class VkBot:

    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self.get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["ПРИВЕТ", "ЗАПОМНИ", "ПОКАЖИ", "ХОЧУ", "МНЕ НРАВИТСЯ", "ПОВЕСЕЛИ"]

    def get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self.clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, message):
        DbHandler.add_user(self._USER_ID, self._USERNAME)
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}! \n " \
                   f"Список команд: \n\n" \
                   f"ПРИВЕТ - получить список команд \n\n" \
                   f"ЗАПОМНИ - создать напоминание. Например, запомни/Вынести мусор/2020-12-20 10:00/ \n\n" \
                   f"ПОКАЖИ - показать список всех напоминаний. Если ввести ПОКАЖИ, то выведутся все заметки" \
                   f" за все время, если ввести ПОКАЖИ/2020-10-10/, то выведутся все заметки на эту дату \n\n" \
                   f"ХОЧУ - получить список доступных жанров мемов \n\n" \
                   f"МНЕ НРАВИТСЯ - задать свои предпочтения в мемах \n\n" \
                   f"ПОВЕСЕЛИ - получить случайный мем"
        elif str(message).upper().startswith(self._COMMANDS[1]):
            command = str(message).split('/')
            DbHandler.add_note(self._USER_ID, command[1], command[2])
            return "Готово, бро!"
        elif str(message).upper().startswith(self._COMMANDS[2]):
            command = str(message).split('/')
            if len(command) == 1:
                return DbHandler.get_notes_by_user_id(self._USER_ID)
            else:
                return DbHandler.get_notes_by_user_id(self._USER_ID, command[1])
        else:
            return "Неизвестная команда"

    @staticmethod
    def clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        return result
