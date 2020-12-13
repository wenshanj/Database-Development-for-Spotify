import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def printAlbums():
    tmpl = '''
    SELECT * 
      FROM Albums
    '''
    cmd = cur.mogrify(tmpl,())
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(["album_id", "album_type", "name", "date_released", "label_company", "num_song", "total_time", "artist_email"])
    for row in rows:
        table.add_row(row)
    print(table)


def printSongs():
    tmpl = '''
    SELECT * 
      FROM Songs
    '''
    cmd = cur.mogrify(tmpl,())
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(["song_id", "title", "time", "album_id"])
    for row in rows:
        table.add_row(row)
    print(table)

def US3(album_id, album_type, name, date_released, label_company, num_song, total_time, artist_email, song_id, title, time, album_id_song):
    print ("US3: As an artist, I want to upload a new song on Spotify")
    print ("Input: album_id = 10, album_type = single, name = Hollywood's Bleeding, date_released = 2019-01-01," 
                  "label_company = Republic Records, num_song = 1, total_time= 228, artist_email = postm@gmail.com,"
                  "song_id = 11, title = Circles, time = 228, album_id_song = 10")
    tmpl = '''
    INSERT INTO Albums (album_id, album_type, name, date_released, label_company, num_song, total_time, artist_email)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    INSERT INTO Songs (song_id, title, time, album_id)
    VALUES (%s, %s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl,(album_id, album_type, name, date_released, label_company, num_song, total_time, artist_email, song_id, title, time, album_id_song,))
    cur.execute(cmd)
    printAlbums()
    printSongs()

US3(10, "single", "Hollywood's Bleeding", "2019-01-01", "Republic Records", 1, 228, "postm@gmail.com", 11, "Circles", 228, 10)

