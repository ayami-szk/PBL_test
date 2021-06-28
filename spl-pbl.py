import sqlite3

con = sqlite3.connect('sql-pbl.db')

cur = con.cursor()

cur.executescript('''
    create table pblmembers(id integer, nickname text, ip text)
''')

cur.executescript('''
    insert into pblmembers values(1,'java','192.168.100.232')
''')
cur.executescript('''
    insert into pblmembers values(2,'ai','192.168.100.233')
''')
cur.executescript('''
    insert into pblmembers values(3,'gunzi','192.168.100.235')
''')
cur.executescript('''
    insert into pblmembers values(4,'cari','192.168.100.230')
''')
cur.executescript('''
    insert into pblmembers values(5,'tomoshi','192.168.100.232')
''')
cur.executescript('''
    insert into pblmembers values(6,'Lfu','192.168.100.231')
''')
cur.executescript('''
    insert into pblmembers values(7,'lucky','192.168.100.231')
''')
cur.executescript('''
    insert into pblmembers values(8,'eto','192.168.100.230')
''')
cur.executescript('''
    insert into pblmembers values(9,'randy','192.168.100.234')
''')
cur.executescript('''
    insert into pblmembers values(10,'ishidon','192.168.100.234')
''')

con.commit()
con.close()
