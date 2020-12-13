#not yet implemented by Spotify
import psycopg2 as pg2
from prettytable import PrettyTable 

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def US7():
    print("US7: As a user, I want to see the most played song of all time")
    print("Input: none")

    tmpl = '''
     SELECT s.title, sum(p.num_played)
       FROM Songs as s
            JOIN Play as p ON s.song_id = p.song_id
      GROUP BY p.song_id, s.title
      ORDER BY sum(p.num_played) DESC
      LIMIT 1;

    '''
    cmd = cur.mogrify(tmpl,())
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['song_title', 'num_played'])
    for row in rows:
        table.add_row(row)
    print(table)

US7()