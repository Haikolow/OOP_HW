class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self):
        total = 0
        len_total = 0
        for row in list(self.grades.values()):
            total += sum(row)
            len_total += len(row)
        return round(total / len_total, 2)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n' \
              f'Средняя оценка за домашнее задание {self.average_score()} \n' \
              f'Курсы в процессе изучения {self.courses_in_progress} \n' \
              f'Завершенные курсы {self.finished_courses}'
        return res

    def __it__(self, other):
        if not isinstance(other, Student):
            return 'Это не студент'
        return self.average_score() < other.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_score(self):
        total = 0
        len_total = 0
        for row in list(self.grades.values()):
            total += sum(row)
            len_total += len(row)
        return round(total / len_total, 2)

    def __str__(self):
        res = f'Имя {self.name} \nФамилия {self.surname} \n' \
              f'Средняя оценка за лекции {self.average_score()}'
        return res

    def __it__(self, other):
        if not isinstance(other, Lecturer):
            return 'Это не лектор'
        return self.average_score() < other.average_score()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


student_1 = Student('Egor', 'Pupkin', 'm')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Fedor', 'Sidorov', 'm')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Petr', 'Petrov')
reviewer_1.courses_attached += ['Python', 'Git']

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 7)

reviewer_1.rate_hw(student_2, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Git', 6)
reviewer_1.rate_hw(student_2, 'Git', 8)

student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_1, 'Python', 9)
student_1.rate_lec(lecturer_1, 'Python', 9)

student_2.rate_lec(lecturer_1, 'Python', 10)
student_2.rate_lec(lecturer_1, 'Python', 10)
student_2.rate_lec(lecturer_1, 'Python', 7)

student_1.rate_lec(lecturer_1, 'Git', 7)
student_1.rate_lec(lecturer_1, 'Git', 6)
student_1.rate_lec(lecturer_1, 'Git', 9)

student_2.rate_lec(lecturer_1, 'Git', 9)
student_2.rate_lec(lecturer_1, 'Git', 8)
student_2.rate_lec(lecturer_1, 'Git', 7)

students_list = [student_1, student_2]
lecturers_list = [lecturer_1]

def average_score_students(students_list, course):
    sum_average = 0
    counter = 0
    for stud in students_list:
        if course in stud.grades:
            sum_average += sum(stud.grades[course])
            counter += len(stud.grades[course])
        else:
            return f'По данному курсу у студента нет оценок'
    return round(sum_average / counter, 2)


def average_score_lectors(lectors_list, course):
    sum_average = 0
    counter = 0
    for lector in lectors_list:
        if course in lector.grades:
            sum_average += sum(lector.grades[course])
            counter += len(lector.grades[course])
        else:
            return f'По даннмоу курсу еще не было лекций'
    return round(sum_average / counter, 2)

print(f'Студенты: \n{student_1} \n{student_2}')
print()
print(f'Лекторы: \n{lecturer_1}')
print()
print(f'Проверяющие: \n{reviewer_1}')
print()
print(average_score_lectors(lecturers_list, 'Python'))
print(average_score_students(students_list, 'Python'))
print(average_score_lectors(lecturers_list, 'Git'))
print(average_score_students(students_list, 'Git'))
