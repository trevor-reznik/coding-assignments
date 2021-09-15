def grade_info(grades):
    max_grade = 0
    min_grade = 100
    sum_grades = 0
    for _ in grades:
      if _ > max_grade:
        max_grade = _ 
      if _ < min_grade:
        min_grade = _
      sum_grades += _
    avg_grade = sum_grades / float(len(grades))
    return max_grade, min_grade, avg_grade