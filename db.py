import sqlite3

def drop_table():
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        c.execute('DROP TABLE IF EXISTS greenhouse')
    return True


def create_db():
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        c.execute('CREATE TABLE greenhouse (time REAL, temp REAL)')
    return True

def seed():
    #open the database
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        #open the datafile
        with open(file_name, 'r') as data:
            #interate through the datafile
            for value in data:
                value.replace('\n', '')
                array = value.split(',')
                values = [array[0], array[1]]
                c.execute('INSERT INTO greenhouse VALUES(?, ?)', values)

if __name__ == '__main__':
    drop_table()
    create_db()
    seed('data.dat')
