

import sqlite3


class Database:

    def __init__(self, path):
        self.conn = sqlite3.connect(path)

    def select(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        return c.fetchall()

    def execute(self, sql, parameters=[]):
        c = self.conn.cursor()
        c.execute(sql, parameters)
        self.conn.commit()

    def get_bikes(self):
        data = self.select(
            'SELECT * FROM bikes ORDER BY id ASC')
        return [{
            'id': d[0],
            'name': d[1],
            'wheels': d[2],
            'size': d[3],
            'motor': d[4],
            'folding': d[5],
            'image': d[6],
            'available': d[7],

        } for d in data]

    def get_num_bikes(self):
        data = self.select('SELECT COUNT(*) FROM bikes')
        return data[0][0]

    def update_bikes(self, id, available):
        self.execute('UPDATE bikes SET available=? WHERE id=?', [available, id])
    
    def reset_bikes(self, available):
        self.execute('UPDATE bikes SET available=?', [available])

    def close(self):
        self.conn.close()

    
