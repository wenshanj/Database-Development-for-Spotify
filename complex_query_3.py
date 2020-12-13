import psycopg2 as pg2
from prettytable import PrettyTable 

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def US9(advertiser_email, ad_id):
    print("US9: As an advertiser, I want to see how many people have listened to my advertisement")
    print("Input: advertiser_email = toyota@gmail.com and ad_id = 6")
    tmpl = '''
     SELECT a.name, ad.ad_id, ad.content, count(l.listener_email)
       FROM Advertisements as ad
            JOIN Listen as l ON ad.ad_id = l.ad_id
            JOIN Accounts as a ON ad.advertiser_email = a.email
     WHERE ad.ad_id = %s
       AND ad.advertiser_email = %s
     GROUP BY a.name, ad.ad_id
    '''
    cmd = cur.mogrify(tmpl,(ad_id, advertiser_email))
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['advertiser','ad_id', 'ad_content', 'listener_count'])
    for row in rows:
        table.add_row(row)
    print(table)
    
US9("toyota@gmail.com", 6)