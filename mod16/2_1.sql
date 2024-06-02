SELECT customer.full_name, manager.full_name, purchase_amount, date FROM "order"
LEFT JOIN customer ON "order".customer_id = customer.customer_id
LEFT JOIN manager ON "order".manager_id = manager.manager_id