SELECT customer.full_name FROM customer
WHERE NOT EXISTS(SELECT * FROM "order" 
WHERE "order".customer_id = customer.customer_id)