SELECT students.full_name, AVG(grade) FROM assignments_grades
LEFT JOIN students ON students.student_id = assignments_grades.student_id
GROUP BY assignments_grades.student_id
ORDER BY AVG(grade) DESC
LIMIT 10