-- SQL-команды для создания таблиц

create table employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(20) NOT NULL,
    last_name varchar(30) NOT NULL,
	title varchar(20) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

create table customers
(
    customer_id varchar(20) PRIMARY KEY,
    company_name varchar(50) NOT NULL,
    contact_name varchar(30) NOT NULL
);

create table orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(20) REFERENCES customers(customer_id),
    employee_id int REFERENCES employees(employee_id),
	order_date date NOT NULL,
	ship_city varchar(30) NOT NULL
);
