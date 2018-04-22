drop database if exists marta;
create database marta;
use marta;

create table routes (
  route_id INTEGER primary key,
  route_name TEXT
);

create table stops (
  stop_id INTEGER primary key,
  stop_name TEXT
);

create table vehicles (
  vehicle_id INTEGER primary key
);

create table passenger_data (
  `index` INTEGER primary key,
  `date` date,
  route_id INTEGER,
  direction TEXT,
  stop_id INTEGER,
  on_number INTEGER,
  off_number INTEGER,
  vehicle_id INTEGER,

  foreign key (route_id) references routes(route_id),
  foreign key (stop_id) references stops(stop_id),
  foreign key (vehicle_id) references vehicles(vehicle_id)
);
