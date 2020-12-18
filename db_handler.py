import mysql.connector


class DbHandler:

    @staticmethod
    def connect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="meme_notification",
            autocommit=True
        )

    @staticmethod
    def get_preferences():
        conn = DbHandler.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM preferences;"
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def add_user(user_id, username):
        conn = DbHandler.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO users (id, name) VALUES ('%s', '%s');" % (str(user_id), username)
        try:
            cursor.execute(sql)
        except mysql.connector.errors.IntegrityError:
            pass
        conn.close()

    @staticmethod
    def set_preferences_to_user(user_id, preferences):
        conn = DbHandler.connect()
        cursor = conn.cursor()
        sql = "UPDATE users SET preferences = %d WHERE id = %d;" % (preferences, user_id)
        cursor.execute(sql)
        conn.close()

    @staticmethod
    def add_note(user_id, content, notification_date, notification_frequency=1):
        conn = DbHandler.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO notes (notification_date, notification_frequency, content, user) " \
              "VALUES ('%s', '%d', '%s', '%d');" \
              % (str(notification_date), notification_frequency, str(content), user_id)
        cursor.execute(sql)
        conn.close()

    @staticmethod
    def get_notes_by_user_id(user_id, date="all"):
        conn = DbHandler.connect()
        cursor = conn.cursor()
        if date == "all":
            sql = "SELECT * FROM notes WHERE user = '%d';" % user_id
        else:
            sql = "SELECT * FROM notes " \
                  "WHERE user = '%d' AND notification_date " \
                  "BETWEEN '%s 00:00:00' AND '%s 23:59:59';" % (user_id, date, date)
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        str1 = ""
        if len(result) > 0:
            for item in result:
                str1 = str1 + ("Дата напоминания: " + str(item[1]) + "\n" +
                               " Частота напоминания: " + str(item[2]) + "\n" +
                               " Содержимое: " + str(item[3]) + "\n\n")
        else:
            str1 = "У вас еще нет напоминаний, создайте новое!"
        return str1
