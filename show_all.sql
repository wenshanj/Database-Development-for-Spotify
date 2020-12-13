\c spotify

\echo "Table for all accounts"
SELECT *
  FROM Accounts;

\echo "Table for advertiser"
SELECT *
  FROM Advertisers;

\echo "Table for all artists"
SELECT *
  FROM Artists;

\echo "Table for all listeners"
SELECT *
  FROM Listeners;

\echo "Table for all advertisements"
SELECT *
  FROM Advertisements;

\echo "Table for all albums"
SELECT *
  FROM Albums;

\echo "Table for all songs"
SELECT *
  FROM Songs;

\echo "Table for all playlists"
SELECT *
  FROM Playlists;

\echo "Table for artists that listeners followed"
SELECT *
  FROM Follow;

\echo "Table for ads that listeners listened to"
SELECT *
  FROM Listen;

\echo "Table for songs that listeners played or downloaded"
SELECT *
  FROM Play;

\echo "Table for songs that listeners added to playlists"
SELECT *
  FROM AddedTo;
