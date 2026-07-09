create table returns (
    return_id int auto_increment primary key,
    order_item_id int not null,
    return_date datetime not null,
    return_reason varchar(100) not null,
    refund_amount decimal(10,2) not null,
    return_status varchar(30) not null,

    foreign key (order_item_id)
        references order_items(order_item_id)
);