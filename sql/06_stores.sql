create table stores (
    store_id int auto_increment primary key,
    store_name varchar(100) not null,
    city varchar(50) not null,
    state varchar(50) not null,
    contact_no varchar(15),
    opening_date date not null
);