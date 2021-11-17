import sqlite3 as sql


class DB:
    def __init__(self, values):
        self.conn = sql.connect('data.db')
        self.conn.execute(
            'INSERT INTO Requests(id, Subject, Language, day, time, req_id) values(?, ?, ?, ?, ?, ?);',
            values)
        self.conn.commit()

class DB_Accept:
    def __init__(self, teacher, id):
        self.conn = sql.connect('data.db')
        self.res = self.conn.execute('''select * from Requests where req_id = ?''', id)
        for i in self.res:
            print(i, teacher)

# conn.execute('CREATE TABLE Requests(id integer, Subject varchar(15), Language varchar(10), Date datetime2);')
#
# conn.execute('CREATE TABLE AcceptedRequests(id integer, Subject varchar(15), Language varchar(20), Date datetime2, teacher varchar(25));')
# conn.commit()

# conn.execute('CREATE TABLE messages(links varchar(100));')
# conn.execute('CREATE TABLE SuperUsers(nickname varchar(255), user_id varchar(255));')

# conn.execute(f'INSERT INTO messages(links) values()')
