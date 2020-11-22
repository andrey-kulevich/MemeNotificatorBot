import requests
import bs4
from db_handler import DbHandler


class VkBot:

    def __init__(self, user_id):
        self._USER_ID = user_id
        self._USERNAME = self.get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["ПРИВЕТ"]

    def get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self.clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, message):
        DbHandler.add_user(self._USER_ID, self._USERNAME)

        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!"
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
