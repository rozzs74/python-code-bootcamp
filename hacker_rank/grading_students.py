
def gradingStudents(grades):
	no_students = len(grades)
	i = 0
	FAILING_GRADE_BASIS = 40
	ROUND_OFF_BASIS = 3
	ROUND_OFF_MULTIPLE = 5
	final_grade = []

	while no_students > 1:
		grade = grades[i]
		multiple_of_5 = (round((grade / ROUND_OFF_MULTIPLE) + 0.5) * 5)
		if multiple_of_5 >= FAILING_GRADE_BASIS:
			difference = (multiple_of_5 - grade)
			if difference < ROUND_OFF_BASIS and difference != ROUND_OFF_BASIS:
				print(multiple_of_5)
				final_grade.append(multiple_of_5)
			else:
				print(grade)
				final_grade.append(grade)
		else:
			final_grade.append(grade)
			print(grade)
		i += 1
		if i == no_students:
			return final_grade

result = gradingStudents([73,67,38,33])

