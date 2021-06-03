import sqlite3

class SQLwork:

    def __init__(self, database_file):
        """Подключаемся к БД и сохраняем курсор"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_all_names(self):
        """Получаем все названия фанфиков в БД"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'top_get' (name)").fetchall()

    def names_exists(self, name):
        """Проверяем есть ли имя в базе, если нет то +, иначе -"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'top_get' WHERE name = ?", (name,)).fetchall()
        
            return bool(len(result))

    def add_name(self, name):
        """Добавляем имя фанфика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO 'top_dzen' ('name') VALUES (?)", (name,))

    def update_subscription(self, user_id, status):
        """ Обновляем статус подписки, пока хуй знает зачем"""
        return self.cursor.execute("UPDATE 'top_get' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))

    def close(self):
        """Закрываем соединение с бд"""
        self.connection.close()
