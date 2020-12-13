-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2020-12-11 04:40:31.971

-- tables
-- Table: Accounts
CREATE TABLE Accounts (
    email varchar(255)  NOT NULL,
    password varchar  NOT NULL,
    username varchar  NOT NULL,
    name varchar  NOT NULL,
    CONSTRAINT Accounts_pk PRIMARY KEY (email)
);

-- Table: AddedTo
CREATE TABLE AddedTo (
    song_id int  NOT NULL,
    playlist_id int  NOT NULL,
    CONSTRAINT AddedTo_pk PRIMARY KEY (song_id,playlist_id)
);

-- Table: Advertisements
CREATE TABLE Advertisements (
    ad_id int  NOT NULL,
    content varchar  NOT NULL,
    total_time int  NOT NULL,
    advertiser_email varchar(255)  NOT NULL,
    CONSTRAINT Advertisements_pk PRIMARY KEY (ad_id)
);

-- Table: Advertisers
CREATE TABLE Advertisers (
    advertiser_email varchar(255)  NOT NULL,
    business_type varchar  NOT NULL,
    industry varchar  NOT NULL,
    CONSTRAINT Advertisers_pk PRIMARY KEY (advertiser_email)
);

-- Table: Albums
CREATE TABLE Albums (
    album_id int  NOT NULL,
    album_type text  NOT NULL,
    name varchar  NOT NULL,
    date_released date  NOT NULL,
    label_company varchar  NOT NULL,
    num_song int  NOT NULL,
    total_time int  NOT NULL,
    artist_email varchar(255)  NOT NULL,
    CONSTRAINT Albums_pk PRIMARY KEY (album_id)
);

-- Table: Artists
CREATE TABLE Artists (
    artist_email varchar(255)  NOT NULL,
    bio text  NOT NULL,
    monthly_listeners bigint  NOT NULL,
    num_followers bigint  NOT NULL,
    CONSTRAINT Artists_pk PRIMARY KEY (artist_email)
);

-- Table: Follow
CREATE TABLE Follow (
    artist_email varchar(255)  NOT NULL,
    listener_email varchar(255)  NOT NULL,
    CONSTRAINT Follow_pk PRIMARY KEY (artist_email,listener_email)
);

-- Table: Listen
CREATE TABLE Listen (
    listener_email varchar(255)  NOT NULL,
    ad_id int  NOT NULL,
    CONSTRAINT Listen_pk PRIMARY KEY (listener_email,ad_id)
);

-- Table: Listeners
CREATE TABLE Listeners (
    listener_email varchar(255)  NOT NULL,
    account_type varchar  NOT NULL,
    country varchar  NOT NULL,
    gender char(1)  NOT NULL,
    dob date  NOT NULL,
    CONSTRAINT Listeners_pk PRIMARY KEY (listener_email)
);

-- Table: Play
CREATE TABLE Play (
    song_id int  NOT NULL,
    downloaded boolean  NOT NULL,
    listener_email varchar(255)  NOT NULL,
    num_played int  NOT NULL,
    CONSTRAINT Play_pk PRIMARY KEY (song_id,listener_email)
);

-- Table: Playlists
CREATE TABLE Playlists (
    playlist_id int  NOT NULL,
    name varchar  NOT NULL,
    num_songs int  NOT NULL,
    total_time int  NOT NULL,
    num_followers int  NOT NULL,
    listener_email varchar(255)  NOT NULL,
    CONSTRAINT Playlists_pk PRIMARY KEY (playlist_id)
);

-- Table: Songs
CREATE TABLE Songs (
    song_id int  NOT NULL,
    title varchar  NOT NULL,
    time int  NOT NULL,
    album_id int  NOT NULL,
    CONSTRAINT Songs_pk PRIMARY KEY (song_id)
);

-- foreign keys
-- Reference: AddedTo_Playlists (table: AddedTo)
ALTER TABLE AddedTo ADD CONSTRAINT AddedTo_Playlists
    FOREIGN KEY (playlist_id)
    REFERENCES Playlists (playlist_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: AddedTo_Songs (table: AddedTo)
ALTER TABLE AddedTo ADD CONSTRAINT AddedTo_Songs
    FOREIGN KEY (song_id)
    REFERENCES Songs (song_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Advertisements_Advertisers (table: Advertisements)
ALTER TABLE Advertisements ADD CONSTRAINT Advertisements_Advertisers
    FOREIGN KEY (advertiser_email)
    REFERENCES Advertisers (advertiser_email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Advertisers_Accounts (table: Advertisers)
ALTER TABLE Advertisers ADD CONSTRAINT Advertisers_Accounts
    FOREIGN KEY (advertiser_email)
    REFERENCES Accounts (email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Albums_Artists (table: Albums)
ALTER TABLE Albums ADD CONSTRAINT Albums_Artists
    FOREIGN KEY (artist_email)
    REFERENCES Artists (artist_email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Artists_Accounts (table: Artists)
ALTER TABLE Artists ADD CONSTRAINT Artists_Accounts
    FOREIGN KEY (artist_email)
    REFERENCES Accounts (email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Follow_Artists (table: Follow)
ALTER TABLE Follow ADD CONSTRAINT Follow_Artists
    FOREIGN KEY (artist_email)
    REFERENCES Artists (artist_email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Follow_Listener (table: Follow)
ALTER TABLE Follow ADD CONSTRAINT Follow_Listener
    FOREIGN KEY (listener_email)
    REFERENCES Listeners (listener_email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Listen_Advertisements (table: Listen)
ALTER TABLE Listen ADD CONSTRAINT Listen_Advertisements
    FOREIGN KEY (ad_id)
    REFERENCES Advertisements (ad_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Listen_Listener (table: Listen)
ALTER TABLE Listen ADD CONSTRAINT Listen_Listener
    FOREIGN KEY (listener_email)
    REFERENCES Listeners (listener_email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Listener_Accounts (table: Listeners)
ALTER TABLE Listeners ADD CONSTRAINT Listener_Accounts
    FOREIGN KEY (listener_email)
    REFERENCES Accounts (email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Play_Listener (table: Play)
ALTER TABLE Play ADD CONSTRAINT Play_Listener
    FOREIGN KEY (listener_email)
    REFERENCES Listeners (listener_email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Play_Songs (table: Play)
ALTER TABLE Play ADD CONSTRAINT Play_Songs
    FOREIGN KEY (song_id)
    REFERENCES Songs (song_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Playlists_Listener (table: Playlists)
ALTER TABLE Playlists ADD CONSTRAINT Playlists_Listener
    FOREIGN KEY (listener_email)
    REFERENCES Listeners (listener_email)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Songs_Albums (table: Songs)
ALTER TABLE Songs ADD CONSTRAINT Songs_Albums
    FOREIGN KEY (album_id)
    REFERENCES Albums (album_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

