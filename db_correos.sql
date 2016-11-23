PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE USUARIO(    correo TEXT NOT NULL,	contra TEXT NOT NULL,	apellidoPatU TEXT NOT NULL,	apellidoMatU TEXT,    nombresU TEXT NOT NULL,	PRIMARY KEY(correo));
INSERT INTO "USUARIO" VALUES('q','q','RO','BO','JD');
CREATE TABLE CONTACTO(	contacto_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	email TEXT NOT NULL,	registra TEXT NOT NULL,	apellidoPatC TEXT NOT NULL,	apellidoMatC TEXT,	nombresC TEXT NOT NULL,	FOREIGN KEY(registra) REFERENCES USUARIO ( correo )    );
INSERT INTO "CONTACTO" VALUES(1,'jose@gmail.com','q','Perez','Lopez','Jose');
INSERT INTO "CONTACTO" VALUES(2,'ana@gmail.com','q','Gomez',NULL,'Ana');
INSERT INTO "CONTACTO" VALUES(3,'juan@gmail.com','q','j','j','j');
CREATE TABLE CORREO(	correo_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	fecha NUMERIC NOT NULL,	hora NUMERIC NOT NULL,	de TEXT NOT NULL,	para TEXT NOT NULL,    para_id INTEGER NOT NULL, 	texto TEXT,	asunto TEXT,	adjunto TEXT,    eliminado BOOLEAN NOT NULL,	FOREIGN KEY(`de`) REFERENCES USUARIO ( correo ),	FOREIGN KEY(`para_id`) REFERENCES CONTACTO ( contacto_id ));
INSERT INTO "CORREO" VALUES(1,'21/11/2016','21:28:42','q','ana@gmail.com',2,'ANA','a','a',0);
INSERT INTO "CORREO" VALUES(2,'21/11/2016','21:28:57','q','jose@gmail.com',1,'Jose C:
	Hola','Saludo',NULL,0);
INSERT INTO "CORREO" VALUES(3,'21/11/2016','21:36:34','q','ana@gmail.com',2,'...¿?...',NULL,NULL,0);
CREATE TABLE CORREO_E(	correo_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	fecha NUMERIC NOT NULL,	hora NUMERIC NOT NULL,	de TEXT NOT NULL,	para TEXT NOT NULL,    para_id INTEGER NOT NULL, 	texto TEXT,	asunto TEXT,	adjunto TEXT,    eliminado BOOLEAN NOT NULL,	FOREIGN KEY(`de`) REFERENCES USUARIO ( correo ),	FOREIGN KEY(`para_id`) REFERENCES CONTACTO ( contacto_id ));
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('CONTACTO',3);
INSERT INTO "sqlite_sequence" VALUES('CORREO',3);
COMMIT;
