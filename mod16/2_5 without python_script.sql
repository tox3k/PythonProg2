SELECT DISTINCT c1.customer_id, c2.customer_id FROM customer as c1
CROSS JOIN customer as c2
WHERE c1.manager_id=c2.manager_id AND c1.city = c2.city AND c1.manager_id IS NOT NULL and c1.customer_id < c2.customer_id
ORDER BY c1.customer_id, c2.customer_id