#verify if 2 values had same memory location
course_name = "Python bootcamp"
course_title = course_name
some_value = 46
another_value = 45
result_value = another_value + 1

#IS
print(f"course_title {course_title} is some_value {some_value}: ", course_title is some_value)
#false

print(f"some_value {some_value} is result_value {result_value}: ", some_value is result_value)
#false

print(f"course_name {course_name} is course_title {course_title}: ", course_name is course_title)
#true

#IS NOT
print(f"course_name {course_name} is NOT course_title {course_title}: ", course_name is not course_title)
#false
