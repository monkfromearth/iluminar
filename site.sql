CREATE TABLE tags (id integer primary key auto_increment, name varchar(128), created bigint);

CREATE TABLE courses (id integer primary key auto_increment, tag integer, title varchar(512) not null, link varchar(512) not null, created bigint);

CREATE TABLE cinfo (id integer primary key auto_increment, course integer, name varchar(512) not null, content text, created bigint);

ALTER DATABASE iluminar CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;