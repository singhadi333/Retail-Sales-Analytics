create table customers (
    customer_id int auto_increment primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email_id varchar(100) unique not null,
    phone varchar(15),
    address varchar(255),
    city varchar(50),
    join_date date
);