create table suppliers (
    supplier_id int auto_increment primary key,
    supplier_name varchar(100) not null,
    contact_person varchar(100),
    email varchar(100) unique,
    phone varchar(15),
    city varchar(50),
    state varchar(50)
);