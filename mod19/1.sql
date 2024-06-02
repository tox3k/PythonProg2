SELECT full_name, MIN(average_grade) FROM
(
SELECT teachers.full_name, AVG(assignments_grades.grade) as 'average_grade' FROM assignments_grades
LEFT JOIN assignments ON assignments_grades.assisgnment_id = assignments.assisgnment_id
LEFT JOIN teachers ON assignments.teacher_id=teachers.teacher_id
GROUP BY assignments.teacher_id
ORDER BY average_grade
)