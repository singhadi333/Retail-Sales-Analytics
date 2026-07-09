create table payments (
    payment_id int auto_increment primary key,
    order_id int not null,
    amount decimal(10,2) not null,
    payment_method varchar(30) not null,
    payment_status varchar(30) not null,
    payment_date datetime not null,
    transaction_id varchar(100) unique,

    foreign key (order_id)
        references orders(order_id)
);