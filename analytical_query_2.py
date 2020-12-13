import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def US4(country):
    print ("US4: As a listener, I want to discover the most popular songs in a given country")
    print ("Input: country = United States")
    tmpl = '''
    SELECT s.title, sum(p.num_played) as total_played
      FROM Albums as a 
           JOIN Songs as s ON a.album_id = s.album_id
           JOIN Play as p ON p.song_id = s.song_id
           JOIN Listeners as l ON l.listener_email = p.listener_email
     WHERE l.country = %s
     GROUP BY s.song_id
     ORDER BY total_played DESC
     LIMIT 1;

    '''
    cmd = cur.mogrify(tmpl,(country,))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(["song_title", "total_played"])
    for row in rows:
        table.add_row(row)
    print(table)

US4("United States")