import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def US1(email):
    print ("US1: As an artist, I want see the country that my music is streamed the most")
    print ("Input: email = arianagrande@gmail.com")
    tmpl = '''
    SELECT l.country, sum(p.num_played) as total_played
      FROM Albums as a 
           JOIN Songs as s ON a.album_id = s.album_id
           JOIN Play as p ON p.song_id = s.song_id
           JOIN Listeners as l ON l.listener_email = p.listener_email
     WHERE a.artist_email = %s
     GROUP BY l.country
     ORDER BY total_played DESC
     LIMIT 1;

    '''
    cmd = cur.mogrify(tmpl,(email,))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(["country", "total_played"])
    for row in rows:
        table.add_row(row)
    print(table)

US1("arianagrande@gmail.com")