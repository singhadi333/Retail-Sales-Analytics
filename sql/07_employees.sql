create table employees (
    employee_id int auto_increment primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(100) unique not null,
    phone varchar(15),
    store_id int not null,
    position varchar(50) not null,
    salary decimal(10,2) not null,
    joining_date date not null,

    foreign key (store_id)
        references stores(store_id)
);