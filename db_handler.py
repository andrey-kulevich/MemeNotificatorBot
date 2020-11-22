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
        sql = "SELECT * FROM users;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            sql = "INSERT INTO users (id, name) VALUES ('%s', '%s');" % (str(user_id), username)
            cursor.execute(sql)
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
    def get_notes_by_user_id(user_id):
        conn = DbHandler.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM notes WHERE user = '%d';" % user_id
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result

