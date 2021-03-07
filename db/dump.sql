BEGIN TRANSACTION;
CREATE TABLE users(id integer primary key, username text, 
email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim','kim@naver.com','010-1234-1234','kim.com','2021-03-06 20:52:30');
INSERT INTO "users" VALUES(2,'Park','park@naver.com','010-4321-4321','park.com','2021-03-06 20:52:30');
INSERT INTO "users" VALUES(3,'Lee','lee@naver.com','010-5321-5321','lee.com','2021-03-06 20:52:42');
INSERT INTO "users" VALUES(4,'Cho','cho@naver.com','010-6321-4321','cho.com','2021-03-06 20:52:42');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-7321-4321','yoo.com','2021-03-06 20:52:42');
COMMIT;
