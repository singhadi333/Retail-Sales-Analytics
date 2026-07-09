create table orders (
    order_id int auto_increment primary key,
    customer_id int not null,
    store_id int not null,
    employee_id int not null,
    order_date datetime not null,
    order_status varchar(30) not null,
    shipping_address varchar(255) not null,
    total_amount decimal(10,2) not null,

    foreign key (customer_id)
        references customers(customer_id),

    foreign key (store_id)
        references stores(store_id),

    foreign key (employee_id)
        references employees(employee_id)
);