import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def US2(email):
    print ("US2: As an artist, I want to see the number of followers I have")
    print ("Input: artist_email = zico@yahoo.com")
    tmpl = '''
    SELECT artist_email, num_followers
      FROM Artists
     WHERE artist_email = %s;
    '''
    cmd = cur.mogrify(tmpl,(email,))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['email', 'num_followers'])
    for row in rows:
        table.add_row(row)
    print(table)

US2("zico@yahoo.com")