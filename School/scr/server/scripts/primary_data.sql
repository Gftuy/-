INSERT INTO Object(object)
VALUES ('Математика'),
       ('Русский язык'),
       ('Физ-ра');
INSERT INTO Object(object)
VALUES ('Технология'),
       ('Химия'),
       ('Биология');
INSERT INTO Object(object)
VALUES ('Литература'),
       ('Родной язык'),
       ('Физика');

INSERT INTO Teacher(FIO, Address, Post, Classroom_teacher)
VALUES ('Киселева Ульяна Дмитриевна', 'Омская область, город Серебряные Пруды, бульвар Гоголя, 20',
        'Учитель литературы', '9б');
INSERT INTO Teacher(FIO, Address, Post, Classroom_teacher)
VALUES ('Лебедева Юлия Кирилловна', 'Омская область, город Серебряные Пруды, бульвар Гоголя, 100',
        'Учитель химии, биологии', '5в');
INSERT INTO Teacher(FIO, Address, Post, Classroom_teacher)
VALUES ('Григорьева Алиса Марковна', 'Омская область, город Серебряные Пруды, бульвар Гоголя, 69', 'Учитель матемтики',
        '6а');

INSERT INTO Times(Start_Time, End_Time)
VALUES (08:30:00),
       (14:10:00);
INSERT INTO Times(Start_Time, End_Time)
VALUES (15:00:00),
       (18:00:00);
INSERT INTO Times(Start_Time, End_Time)
VALUES (14:50:00),
       (16:10:00);

INSERT INTO Auditorium(Capacity)
VALUES (30);
INSERT INTO Auditorium(Capacity)
VALUES (35);
INSERT INTO Auditorium(Capacity)
VALUES (25);

INSERT INTO Worker(FIO, Post)
VALUES ('Яковлева Лидия Дмитриевна', 'Секретарь');
INSERT INTO Worker(FIO, Post)
VALUES ('Ковалева Полина Всеволодовна', 'Техничка');
INSERT INTO Worker(FIO, Post)
VALUES ('Софронова Полина Васильевна', 'Техничка');

INSERT INTO Additional_classes(Title, TeacherID, Data)
VALUES ('Математика', 1, '20.01.2023');
INSERT INTO Additional_classes(Title, TeacherID, Data)
VALUES ('Руский язык', 1, '20.01.2023');
INSERT INTO Additional_classes(Title, TeacherID, Data)
VALUES ('Химия', 2, '20.01.2023');

INSERT INTO Circle(Title, TeacherID, Data)
VALUES ('Футбол', 1, '20.01.2023');
INSERT INTO Circle(Title, TeacherID, Data)
VALUES ('Баскетбол', 1, '21.01.2023');
INSERT INTO Circle(Title, TeacherID, Data)
VALUES ('Волейбол', 1, '22.01.2023');

INSERT INTO Class(№Class, Quantity, Classroom_teacher)
VALUES ('9', '25', 'Киселева Ульяна Дмитриевна');
INSERT INTO Class(№Class, Quantity, Classroom_teacher)
VALUES ('5', '30', 'Лебедева Юлия Кирилловна');
INSERT INTO Class(№Class, Quantity, Classroom_teacher)
VALUES ('6', '29', 'Григорьева Алиса Марковна');

INSERT INTO Student(FIO, Address, id)
VALUES ('Лобанов Арсений Арсентьевич', 'Омская область, город Серебряные Пруды пл. Гоголя, 92', 1);
INSERT INTO Student(FIO, Address, id)
VALUES ('Медведев Владислав Васильевич', 'Омская область, город Серебряные Пруды пл. Гоголя, 94', 2);
INSERT INTO Student(FIO, Address, id)
VALUES ('Кузнецов Филипп Тимофеевич', 'Омская область, город Серебряные Пруды пл. Гоголя, 96', 3);

INSERT INTO Users(login, password, post_id)
VALUES ('admin', 'admin', 1);

INSERT INTO Schedule(Data, ID, ID, ID, ID, ID, ID)
VALUES ('20.01.2023', 1, 1, 1, 1, 1);
INSERT INTO Schedule(Data, ID, ID, ID, ID, ID, ID)
VALUES ('21.01.2023', 2, 2, 2, 2, 2);
INSERT INTO Schedule(Data, ID, ID, ID, ID, ID, ID)
VALUES ('22.01.2023', 3, 3, 3, 3, 3);
