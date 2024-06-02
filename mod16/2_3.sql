SELECT "order".order_no,manager.full_name, customer.full_name FROM "order"
LEFT JOIN manager ON manager.manager_id = "order".manager_id
LEFT JOIN customer ON customer.customer_id = "order".customer_id
WHERE NOT customer.city = manager.city