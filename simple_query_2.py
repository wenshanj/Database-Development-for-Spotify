import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def US5(playlist_id):
    print ("US5: As a listener, I want to see the total number of songs in a given playlist")
    print ("Input: playlist_id = 9")
    tmpl = '''
    SELECT playlist_id, num_songs
      FROM Playlists
     WHERE playlist_id = %s;
    '''
    cmd = cur.mogrify(tmpl,(playlist_id,))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(["playlist_id", "num_songs"])
    for row in rows:
        table.add_row(row)
    print(table)

US5(9)