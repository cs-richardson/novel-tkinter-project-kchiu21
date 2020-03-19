BEGIN TRANSACTION;
DROP TABLE IF EXISTS "consumerpurchasenovel";
CREATE TABLE IF NOT EXISTS "consumerpurchasenovel" (
	"isbn"	INTEGER NOT NULL,
	"consumerid"	INTEGER NOT NULL,
	"purchasedate"	NUMERIC NOT NULL,
	"quantity"	NUMERIC NOT NULL,
	FOREIGN KEY("consumerid") REFERENCES "consumer"("consumerid"),
	PRIMARY KEY("purchasedate"),
	FOREIGN KEY("isbn") REFERENCES "novel"("isbn")
);
DROP TABLE IF EXISTS "consumer";
CREATE TABLE IF NOT EXISTS "consumer" (
	"consumerid"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"DOB"	NUMERIC NOT NULL,
	PRIMARY KEY("consumerid")
);
DROP TABLE IF EXISTS "novel";
CREATE TABLE IF NOT EXISTS "novel" (
	"isbn"	INTEGER NOT NULL,
	"authorid"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL,
	PRIMARY KEY("isbn"),
	FOREIGN KEY("authorid") REFERENCES "author"("authorid")
);
DROP TABLE IF EXISTS "author";
CREATE TABLE IF NOT EXISTS "author" (
	"name"	TEXT NOT NULL,
	"DOB"	NUMERIC NOT NULL,
	"authorid"	INTEGER NOT NULL,
	PRIMARY KEY("authorid")
);
INSERT INTO "consumerpurchasenovel" ("isbn","consumerid","purchasedate","quantity") VALUES (101,'C1','10/12/2020',3);
INSERT INTO "consumerpurchasenovel" ("isbn","consumerid","purchasedate","quantity") VALUES (102,'C2','03/03/2020',50);
INSERT INTO "consumer" ("consumerid","name","DOB") VALUES ('C1','adam','10/12/1996');
INSERT INTO "consumer" ("consumerid","name","DOB") VALUES ('C2','John','12/01/1999');
INSERT INTO "novel" ("isbn","authorid","title") VALUES (100,1,'red book');
INSERT INTO "novel" ("isbn","authorid","title") VALUES (101,1,'the book');
INSERT INTO "novel" ("isbn","authorid","title") VALUES (102,2,'cooking book');
INSERT INTO "novel" ("isbn","authorid","title") VALUES (103,3,'harry potter');
INSERT INTO "novel" ("isbn","authorid","title") VALUES (999,1,'blue book');
INSERT INTO "author" ("name","DOB","authorid") VALUES ('Joe','10/09/1950',1);
INSERT INTO "author" ("name","DOB","authorid") VALUES ('Jane','01/03/2001',2);
INSERT INTO "author" ("name","DOB","authorid") VALUES ('Jonh','16/10/2000',3);
COMMIT;
