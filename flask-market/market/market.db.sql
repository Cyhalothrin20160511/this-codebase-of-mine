BEGIN TRANSACTION;
DROP TABLE IF EXISTS "user";
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(30) NOT NULL,
	"email_address"	VARCHAR(50) NOT NULL,
	"password_hash"	VARCHAR(60) NOT NULL,
	"budget"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	UNIQUE("username"),
	UNIQUE("email_address")
);
DROP TABLE IF EXISTS "item";
CREATE TABLE IF NOT EXISTS "item" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(30) NOT NULL,
	"price"	INTEGER NOT NULL,
	"barcode"	VARCHAR(12) NOT NULL,
	"description"	VARCHAR(1024) NOT NULL,
	"owner"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("owner") REFERENCES "user"("id"),
	UNIQUE("name"),
	UNIQUE("description"),
	UNIQUE("barcode")
);
INSERT INTO "user" VALUES (1,'jsc','jsc@jsc.com','123456',1000);
INSERT INTO "user" VALUES (2,'Cyhalothrin20160511','Cyhalothrin20160511@gmail.com','$2b$12$1S3V9PLuEHGtoyXHrrXk2ekm.uafKy8WVKHbR7JR6EC0qoUQq.52m',-800);
INSERT INTO "item" VALUES (1,'IPhone 10',500,'846154104831','desc',1);
INSERT INTO "item" VALUES (2,'Laptop',600,'321912987542','description',NULL);
COMMIT;
