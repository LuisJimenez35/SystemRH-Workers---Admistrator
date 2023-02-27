create database if not exists rhdb

create table if not exists users (
    Usuario varchar(50),
    Email varchar(50),
    SecurityQuestion varchar(50),
    Pass varchar(50),
    primary key(Usuario)
)

create table if not exists trabajadores (
    Dniwork int,
    FullName varchar(50),
    FullLastName varchar(50),
    Birthday varchar(50),
    Location varchar(50),
    DateOfHire varchar(50),
    Position varchar(50),
    Cellphone varchar(50),
    Email varchar(50),
    Salary int,
    primary key (Dniwork)
)
