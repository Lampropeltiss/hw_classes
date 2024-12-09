from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0
        self.mark_sum = 0
        self.mark_counter = 0

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_grade}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}\n"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade == other.average_grade
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade < other.average_grade
        return NotImplemented

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            lecturer.mark_sum += grade
            lecturer.mark_counter += 1
            lecturer.average_grade = round(lecturer.mark_sum / lecturer.mark_counter, 1)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0
        self.mark_sum = 0
        self.mark_counter = 0

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.average_grade}\n"

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade == other.average_grade
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade < other.average_grade
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.mark_sum += grade
            student.mark_counter += 1
            student.average_grade = round(student.mark_sum / student.mark_counter, 1)
        else:
            return 'Ошибка'


cool_student_1 = Student('First', 'Student', 'your_gender')
cool_student_1.courses_in_progress += ['Python']
cool_student_1.courses_in_progress += ['Git']
cool_student_1.finished_courses += ["Введение в программирование"]

cool_student_2 = Student('Second', 'Student', 'gender')
cool_student_2.courses_in_progress += ['Python']
cool_student_2.courses_in_progress += ['ООП']

cool_lecturer_1 = Lecturer('First', 'Lecturer')
cool_lecturer_1.courses_attached += ['Python', 'Git']

cool_lecturer_2 = Lecturer('Second', 'Lecturer')
cool_lecturer_2.courses_attached += ['Python', 'ООП']

cool_reviewer = Reviewer('Some', 'Reviewer')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(cool_student_1, 'Python', 8)
cool_reviewer.rate_hw(cool_student_1, 'Python', 9)
cool_reviewer.rate_hw(cool_student_1, 'Python', 10)

cool_reviewer.rate_hw(cool_student_2, 'Python', 7)
cool_reviewer.rate_hw(cool_student_2, 'Python', 9)
cool_reviewer.rate_hw(cool_student_2, 'Python', 9)

cool_student_1.rate_lecture(cool_lecturer_1, 'Python', 8)
cool_student_1.rate_lecture(cool_lecturer_1, 'Git', 10)
cool_student_2.rate_lecture(cool_lecturer_2, 'Python', 9)
cool_student_2.rate_lecture(cool_lecturer_2, 'ООП', 9)


print(cool_student_1)
print(cool_student_2)
print(cool_lecturer_1)
print(cool_lecturer_2)
print(cool_reviewer)


print(f"student_1 ({cool_student_1.average_grade}) > student_2 ({cool_student_2.average_grade}):",
      f"{cool_student_1 > cool_student_2}")
print(f"student_1 ({cool_student_1.average_grade}) < student_2 ({cool_student_2.average_grade}):",
      f"{cool_student_1 < cool_student_2}")
print(f"student_1 ({cool_student_1.average_grade}) = student_2 ({cool_student_2.average_grade}):",
      f"{cool_student_1 == cool_student_2}")

print()
print(f"lecturer_1 ({cool_lecturer_1.average_grade}) > lecturer_2 ({cool_lecturer_2.average_grade}):",
      f"{cool_lecturer_1 > cool_lecturer_2}")
print(f"lecturer_1 ({cool_lecturer_1.average_grade}) >= lecturer_2 ({cool_lecturer_2.average_grade}):",
      f"{cool_lecturer_1 >= cool_lecturer_2}")
print(f"lecturer_1 ({cool_lecturer_1.average_grade}) == lecturer_2 ({cool_lecturer_2.average_grade}):",
      f"{cool_lecturer_1 == cool_lecturer_2}")
