/*
 * Author: Julian Sprugasci
 * All right reserved. Copyright © SAM TREVANO 2020.
 * Version: 14.02.2020
 */
 
drop database if exists School_Hours;
create database if not exists School_Hours;

use School_Hours;

/*
 * This table contains all the present tables.
 * @code: the classroom code.
 * @name: the classroom name.
 */
drop table if exists `classroom`;
create table if not exists `classroom` (

    `code` int primary key,
    `name` varchar(16) unique not null
    
);


/*
 * This table contains the schoolhours of the current day.
 * @id: the schoolhour id.
 * @start_time: the start time of the subject.
 * @end_time: the end time of the subject.
 * @teacher: the teacher name and surname.
 * @day: the current day.
 * @school_subject: the current school subject.
 */
drop table if exists `school_hour`;
create table if not exists `school_hour` (
	
    `id` int primary key auto_increment,
    `classroom_id` int references day(`classroom_code`),
    `start_time` time not null,
    `end_time` time not null,
    `teacher` varchar (32),
    `day` date not null,
    `school_subject` varchar(32)

);

insert into classroom(code, name) values (0, "247 (B-202)");
insert into classroom(code, name) values (1, "328 (A-325)");
insert into classroom(code, name) values (2, "246 (B-203)");
insert into classroom(code, name) values (3, "243 (B-208)");

insert into school_hour(classroom_id, start_time, end_time, teacher, day, school_subject) values 
(0, time("08:20"), time("09:50"), "Elisa Statti", date("2020-02-13"), "Economia e Diritto"),
(1, time("10:05"), time("10:50"), "Antonini Elena", date("2020-02-13"), "Italiano"),
(1, time("10:50"), time("11:35"), "Ivancev Wladislaw", date("2020-02-13"), "Chimica"),
(2, time("13:15"), time("14:45"), "Giussani Sebastiano", date("2020-02-13"), "Fisica"),
(3, time("15:00"), time("16:30"), "Pomponio Filomena", date("2020-02-13"), "Inglese");


select school_subject from school_hour where current_time() between start_time and end_time;







