import sqlite3

class botdb:
    # Приєднання до дб
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    #Перевірка наявності користувача у бд
    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?",
                                     (user_id,))
        return bool(len(result.fetchall()))

    #Отримання айді користувача в бд за його айді в тг
    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` =?",
                                     (user_id,))
        return result.fetchall()[0]

    #Створення користувача
    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)",
                            (user_id,))
        return self.conn.commit()

    #оновлення змінної а з бд
    def update_datanuma(self, user_id, datanumber_a):
        self.cursor.execute("UPDATE `users` SET `datanumber_a` = ?  WHERE `user_id` = ?",
                            (datanumber_a, user_id))
        return self.conn.commit()

    #отримання змінної а з бд
    def get_datanuma(self, user_id):
        result = self.cursor.execute("SELECT `datanumber_a` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення змінної b з бд
    def update_datanumb(self, user_id, datanumber_b):
        self.cursor.execute("UPDATE `users` SET `datanumber_b` = ?  WHERE `user_id` = ?",
                            (datanumber_b, user_id))
        return self.conn.commit()

    #отримання змінної b з бд
    def get_datanumb(self, user_id):
        result = self.cursor.execute("SELECT `datanumber_b` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення кількості чисел для вибору
    def update_numbercount(self, user_id, numbercount):
        self.cursor.execute("UPDATE `users` SET `numbercount` = ?  WHERE `user_id` = ?",
                            (numbercount, user_id))
        return self.conn.commit()

    #отримання кількості чисел для вибору
    def get_numbercount(self, user_id):
        result = self.cursor.execute("SELECT `numbercount` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення змінної restate з бд
    def update_restate(self, user_id, restate):
        self.cursor.execute("UPDATE `users` SET `restate` = ?  WHERE `user_id` = ?",
                            (restate, user_id))
        return self.conn.commit()

    #отримання restate
    def get_restate(self, user_id):
        result = self.cursor.execute("SELECT `restate` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення змінної actionstate з бд
    def update_actionstate(self, user_id, actionstate):
        self.cursor.execute("UPDATE `users` SET `actionstate` = ?  WHERE `user_id` = ?",
                            (actionstate, user_id))
        return self.conn.commit()

    #отримання actionstate
    def get_actionstate(self, user_id):
        result = self.cursor.execute("SELECT `actionstate` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення змінної list з бд
    def update_list(self, user_id, list):
        self.cursor.execute("UPDATE `users` SET `list` = ?  WHERE `user_id` = ?",
                            (list, user_id))
        return self.conn.commit()

    #отримання list для вибору
    def get_list(self, user_id):
        result = self.cursor.execute("SELECT `list` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення змінної cube1 з бд
    def update_cube1(self, user_id, cube1):
        self.cursor.execute("UPDATE `users` SET `cube1` = ?  WHERE `user_id` = ?",
                            (cube1, user_id))
        return self.conn.commit()

    #отримання cube1 для вибору
    def get_cube1(self, user_id):
        result = self.cursor.execute("SELECT `cube1` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення змінної cube2 з бд
    def update_cube2(self, user_id, cube2):
        self.cursor.execute("UPDATE `users` SET `cube2` = ?  WHERE `user_id` = ?",
                            (cube2, user_id))
        return self.conn.commit()

    #отримання cube2 для вибору
    def get_cube2(self, user_id):
        result = self.cursor.execute("SELECT `cube2` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення змінної cube3 з бд
    def update_cube3(self, user_id, cube3):
        self.cursor.execute("UPDATE `users` SET `cube3` = ?  WHERE `user_id` = ?",
                            (cube3, user_id))
        return self.conn.commit()

    #отримання cube3 для вибору
    def get_cube3(self, user_id):
        result = self.cursor.execute("SELECT `cube3` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]

    #оновлення змінної cubenum з бд
    def update_cubenum(self, user_id, cubenum):
        self.cursor.execute("UPDATE `users` SET `cubenum` = ?  WHERE `user_id` = ?",
                            (cubenum, user_id))
        return self.conn.commit()

    #отримання cubenum для вибору
    def get_cubenum(self, user_id):
        result = self.cursor.execute("SELECT `cubenum` FROM `users` WHERE `user_id` = ?",
                            (user_id,))
        return result.fetchall()[0]


    def close(self):
        #Закінчння поєдання з бд
        self.conn.close()



