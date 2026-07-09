create table products (
    product_id int auto_increment primary key,
    product_name varchar(100) not null,
    category_id int not null,
    supplier_id int not null,
    brand varchar(50),
    cost_price decimal(10,2) not null,
    selling_price decimal(10,2) not null,
    stock_quantity int not null,
    reorder_level int default 10,
    date_added date not null,
    is_active boolean default true,

    foreign key (category_id)
        references categories(category_id),
        
	foreign key (supplier_id)
		references suppliers(supplier_id)
);