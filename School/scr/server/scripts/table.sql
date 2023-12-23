CREATE TABLE Object
(
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    object VARCHAR(50)
);

CREATE TABLE Teacher
(
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    FIO               VARCHAR(50),
    Address           VARCHAR(100),
    Post              VARCHAR(50),
    Classroom_teacher INTEGER
);

CREATE TABLE Times
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    Start_Time TIME,
    End_Time   TIME
);

CREATE TABLE Auditorium
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    Capacity INTEGER
);

CREATE TABLE Worker
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    FIO  VARCHAR(100),
    Post VARCHAR(100)
);

CREATE TABLE Additional_classes
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    Title     VARCHAR(100),
    TeacherID INTEGER,
    Data      DATE
);

CREATE TABLE Circle
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    Title     VARCHAR(100),
    TeacherId INTEGER,
    Data      Date
);
CREATE TABLE Class
(
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    №Class            INTEGER,
    Quantity          INTEGER,
    Classroom_teacher VARCHAR(100)
);

CREATE TABLE Student
(
    ID      INTEGER PRIMARY KEY AUTOINCREMENT,
    FIO     VARCHAR(100),
    Address VARCHAR(100),
    FOREIGN KEY (id)
        REFERENCES Class (id)
        ON DELETE NO ACTION
);

CREATE TABLE Users
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    login    VARCHAR(100),
    password VARCHAR(100),
    post_id  INTEGER,
    reg_date INT NOT NULL DEFAULT (strftime('%s', 'now')),
    FOREIGN KEY (post_id)
        REFERENCES Auditorium (id)
        ON DELETE NO ACTION
);

CREATE TABLE Schedule
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    Data Date,
    FOREIGN KEY (id)
        REFERENCES Class (ID)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (id)
        REFERENCES Auditorium (ID)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (id)
        REFERENCES Teacher (ID)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (id)
        REFERENCES Times (ID)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (id)
        REFERENCES Object (ID)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (id)
        REFERENCES Worker (ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);