create table order_items (
    order_item_id int auto_increment primary key,
    order_id int not null,
    product_id int not null,
    quantity int not null,
    unit_price decimal(10,2) not null,
    discount decimal(10,2) default 0,

    foreign key (order_id)
        references orders(order_id),

    foreign key (product_id)
        references products(product_id)
);