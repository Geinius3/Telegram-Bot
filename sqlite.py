import sqlite3

class botdb:

    def __init__(self, db_file):
        #Приєднання до дб
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        #Перевірка наявності користувача у бд
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?",
                                     (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        #Отримання айді користувача в бд за його айді в тг
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` =?",
                                     (user_id,))
        return result.fetchall()[0]

    def add_user(self, user_id):
        #Створення користувача
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)",
                            (user_id,))
        return self.conn.commit()

    def update_datanuma(self, user_id, datanumber_a):
        #оновлення змінної а з бд
        self.cursor.execute("UPDATE `users` SET `datanumber_a` = ?  WHERE `user_id` = ?",
                            (datanumber_a, user_id))
        return self.conn.commit()

    def get_datanuma(self, user_id):
        #отримання змінної а з бд
        result = self.cursor.execute("SELECT `datanumber_a` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    def update_datanumb(self, user_id, datanumber_b):
        #оновлення змінної b з бд
        self.cursor.execute("UPDATE `users` SET `datanumber_b` = ?  WHERE `user_id` = ?",
                            (datanumber_b, user_id))
        return self.conn.commit()

    def get_datanumb(self, user_id):
        #отримання змінної b з бд
        result = self.cursor.execute("SELECT `datanumber_b` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]


    def update_numbercount(self, user_id, numbercount):
        #оновлення кількості чисел для вибору
        self.cursor.execute("UPDATE `users` SET `numbercount` = ?  WHERE `user_id` = ?",
                            (numbercount, user_id))
        return self.conn.commit()

    def get_numbercount(self, user_id):
        #отримання кількості чисел для вибору
        result = self.cursor.execute("SELECT `numbercount` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    def update_restate(self, user_id, restate):
        #оновлення змінної b з бд
        self.cursor.execute("UPDATE `users` SET `restate` = ?  WHERE `user_id` = ?",
                            (restate, user_id))
        return self.conn.commit()

    def get_restate(self, user_id):
        #отримання змінної b з бд
        result = self.cursor.execute("SELECT `restate` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]


    def close(self):
        #Закінчння поєдання з бд
        self.conn.close()



