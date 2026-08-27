select name as Customers from customers
Left join orders on customers.id=orders.customerId
where orders.customerId is NUll
