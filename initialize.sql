-- Un-comment only one line at a time as you
-- incrementally develop the database

\c postgres
DROP DATABASE IF EXISTS spotify;

CREATE database spotify;
\c spotify

\i create.SQL

\copy Accounts(email, password, username, name)                                                                 FROM 'Accounts.csv'     csv header
\copy Advertisers(advertiser_email, business_type, industry)                                                    FROM 'Advertisers.csv'    csv header
\copy Artists(artist_email, monthly_listeners, bio, num_followers)                                              FROM 'Artists.csv' csv header
\copy Listeners(listener_email, account_type, country, gender, dob)                                             FROM 'Listeners.csv' csv header
\copy Advertisements(ad_id,content, total_time, advertiser_email )                                              FROM 'Advertisements.csv'    csv header
\copy Albums(album_id, album_type, name, date_released, label_company, num_song, total_time, artist_email)      FROM 'Albums.csv' csv header
\copy Follow(artist_email, listener_email)                                                                      FROM 'Follow.csv' csv header
\copy Listen(listener_email, ad_id)                                                                             FROM 'Listen.csv' csv header
\copy Songs(song_id, title, time, album_id)                                                                     FROM 'Songs.csv' csv header
\copy Play(song_id, listener_email, downloaded, num_played)                                                     FROM 'Play.csv' csv header
\copy Playlists(playlist_id, name, num_songs, total_time, num_followers, listener_email)                        FROM 'Playlists.csv' csv header
\copy AddedTo(song_id, playlist_id)                                                                             FROM 'AddedTo.csv' csv header
