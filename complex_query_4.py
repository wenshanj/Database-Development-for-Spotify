import psycopg2 as pg2
from prettytable import PrettyTable 

con = pg2.connect(database = 'spotify', user = 'isdb')
con.autocommit = True
cur = con.cursor()

def US10(advertiser_email):
    print("US10: As a user, I want to see the demographics of all the listeners who heard our advertisements")
    print("Input: advertiser_email = mcdonalds@hotmail.com")
    tmpl = '''
     SELECT  ad.ad_id, ad.content, lis.country, lis.gender, date_part('year', AGE(lis.dob))
       FROM Advertisements as ad
            JOIN Listen as l ON ad.ad_id = l.ad_id
            JOIN Accounts as a ON ad.advertiser_email = a.email
            JOIN Listeners as lis ON l.listener_email = lis.listener_email
     WHERE ad.advertiser_email = %s
     ORDER BY ad.ad_id ASC
    '''
    cmd = cur.mogrify(tmpl,[advertiser_email])
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['ad_id', 'ad_content', 'listener_coountry', 'listener_gender', 'listener_age'])
    for row in rows:
        table.add_row(row)
    print(table)
US10("mcdonalds@hotmail.com")