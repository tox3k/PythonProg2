SELECT AVG(assignments_grades.grade) FROM assignments
LEFT JOIN assignments_grades on assignments_grades.assisgnment_id=assignments.assisgnment_id
WHERE assignments.assignment_text REGEXP 'написать|прочитать'