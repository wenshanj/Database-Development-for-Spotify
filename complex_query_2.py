import psycopg2 as pg2
from prettytable import PrettyTable 

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def US8(playlist_name):
    print("US8: As a user, I want to organize my songs on a playlist by album alphabetical order")
    print("Input: playlist_name = Top Hits of 2010s")
    print()
    print("Playlist:", playlist_name)
    tmpl = '''
     SELECT s.title, a.name, acc.name
       FROM Songs as s
            JOIN Albums as a ON s.album_id = a.album_id
            JOIN Accounts as acc ON a.artist_email = acc.email
            JOIN AddedTo as add ON s.song_id = add.song_id
            JOIN Playlists as p ON add.playlist_id = p.playlist_id
      WHERE p.name = %s
      ORDER BY a.name ASC; 
    '''
    cmd = cur.mogrify(tmpl,[playlist_name])
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['song_title', 'album_name', 'artist_name'])
    for row in rows:
        table.add_row(row)
    print(table)
US8('Top Hits of 2010s')