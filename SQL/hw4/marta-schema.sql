
drop database if exists marta;
create database marta;
use marta;

create table routes(
    route_id int primary key,
    route_name char(60)
);

create table stops(
    stop_id int primary key,
    stop_name char(60)
);

create table vehicles(
    vehicle_id int primary key
);

create table passenger_data(
    indexx int primary key,
    date_ char(10),
    route_id int,
    direction char(10),
    stop_id int,
    on_number int,
    off_number int,
    vehicle_id int,

    foreign key(stop_id) references stops(stop_id),
    foreign key(route_id) references routes(route_id)
);
