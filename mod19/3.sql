SELECT students.full_name FROM
(
SELECT teachers.teacher_id, AVG(assignments_grades.grade) as 'average_grade' FROM assignments_grades
LEFT JOIN assignments ON assignments_grades.assisgnment_id = assignments.assisgnment_id
LEFT JOIN teachers ON assignments.teacher_id=teachers.teacher_id
GROUP BY assignments.teacher_id
ORDER BY average_grade DESC
LIMIT 1
) as best
LEFT JOIN students_groups on students_groups.group_id=best.teacher_id
LEFT JOIN students on students.group_id=students_groups.group_id