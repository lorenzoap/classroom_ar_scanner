drop database if exists Orari;

create database Orari;

use Orari;

drop table if exists Aula;
drop table if exists Docente;
drop table if exists Corso;
drop table if exists Classe;

create table Docente(
	IdDocente int primary key,
    Cognome varchar(50),
    Nome varchar(50)
);

create table Corso(
	IdCorso int primary key,
    Nome varchar(100),
    OraInizio datetime,
    OraFine datetime,
    IdDocente int not null,
    foreign key (IdDocente) references Docente(IdDocente)
		on update cascade
        on delete cascade
);

create table Aula(
	IdAula int primary key,
    Numero varchar(20),
    IdCorso int not null,
    foreign key (IdCorso) references Corso(IdCorso)
		on update cascade
        on delete cascade
);

create table Classe(
	IdClasse int primary key,
    Nome varchar(50),
    IdCorso int not null,
    foreign key (IdCorso) references Corso(IdCorso)
		on update cascade
        on delete cascade
);

#Test
select Numero from Aula where IdCorso = (select IdCorso from Corso where IdDocente = 1);

