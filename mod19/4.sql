SELECT MIN(group_res.c) as 'MIN', MAX(group_res.c) as 'MAX', AVG(group_res.c) as 'AVG' FROM
(
SELECT students_groups.group_id ,COUNT(*) as 'c' FROM students_groups
LEFT JOIN assignments on assignments.group_id=students_groups.group_id
LEFT JOIN assignments_grades on assignments_grades.assisgnment_id=assignments.assisgnment_id
WHERE assignments_grades.date>assignments.due_date
GROUP BY students_groups.group_id
) as group_res