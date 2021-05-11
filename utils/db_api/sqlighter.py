import sqlite3

class SQLighter:

    def __init__(self, database_file):
        """Подключаемся к БД и сохраняем курсор"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_all_users(self, status = True):
        """Получаем всех активных пользователей бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'users' WHERE 'status' = ?", (status,)).fetchall()

    def users_exists(self, user_id):
        """проверяем есть ли юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = '%i'" % user_id).fetchall()
            print(len(result))
            return bool(len(result))

    def add_users(self, user_id, user_login, user_password, status = True):
        """Добавляем пользователя"""
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id', 'user_login', 'user_password', 'status') VALUES (?,?,?,?)", (user_id, user_login, user_password, status))

    def update_subscription(self, user_id, status):
        """ Обновляем статус подписки, пока хуй знает зачем"""
        return self.cursor.execute("UPDATE 'users' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))

    def close(self):
        """Закрываем соединение с бд"""
        self.connection.close()
