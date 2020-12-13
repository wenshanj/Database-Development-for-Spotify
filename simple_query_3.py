import psycopg2 as pg2
from prettytable import PrettyTable 

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def printPlay(song_id, listener_email):
    print("Original Table")
    tmpl = '''
    SELECT *
      FROM Play
     WHERE song_id = %s
       AND listener_email = %s;
    '''
    cmd = cur.mogrify(tmpl,(song_id, listener_email,))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['song_id', 'downloaded', 'listener_email', 'num_played'])
    for row in rows:
        table.add_row(row)
    print(table)

printPlay(7, "user1@gmail.com")

def US6(song_id, listener_email):
    print("US6: As a user, I want to download songs I like")
    print("Input: song_id = 7 and listener_email = user1@gmail.com")
    tmpl = '''
    INSERT INTO Play(song_id, listener_email, downloaded, num_played)
    VALUES(%s, %s, TRUE, 0) 
    ON CONFLICT (song_id, listener_email)
    DO UPDATE SET downloaded = TRUE;
    
    SELECT *
      FROM Play
     WHERE song_id = %s
       AND listener_email = %s;
    '''
    cmd = cur.mogrify(tmpl,(song_id, listener_email, song_id, listener_email))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['song_id', 'downloaded', 'listener_email', 'num_played'])
    for row in rows:
        table.add_row(row)
    print(table)

US6(7, "user1@gmail.com")