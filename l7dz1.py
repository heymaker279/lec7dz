class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.all_grades = []
    def rate_lec(self, lecturer, student, course, grade):
        '''Оценка лектора'''  
        if course in lecturer.courses_attached and course in student.courses_in_progress and 1 < grade <= 10:
            lecturer.all_grades.append(grade)            
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            elif course not in lecturer.grades:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'\n  Студент\nИмя: {self.name} \nФамилия:  {self.surname} \nСредняя оценка за домашнее задаие: {round(sum(self.all_grades) / len(self.all_grades), 1)} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'    
    def comparison_grades(self, other):
        '''Сравнение оценок'''
        if round(sum(self.all_grades) / len(self.all_grades), 1) > round(sum(other.all_grades) / len(other.all_grades), 1):
            print('\nСредняя оценка выше у студента: ' + self.name + ' ' + self.surname)
        else:
            print('\nСредняя оценка выше у студента: ' + other.name + ' ' + other.surname)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []   
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.all_grades = []
    def __str__(self):
        return f'\n  Лектор\nИмя: {self.name} \nФамилия:  {self.surname} \nСредняя оценка за лекции:  {round(sum(self.all_grades) / len(self.all_grades), 1)}'
    def comparison_grades(self, other):
        '''Сравнение оценок'''
        if round(sum(self.all_grades) / len(self.all_grades), 1) > round(sum(other.all_grades) / len(other.all_grades), 1):
            print('\nСредняя оценка выше у лектора : ' + self.name + ' ' + self.surname)
        else:
            print('\nСредняя оценка выше у лектора : ' + other.name + ' ' + other.surname)
class Rewiewer(Mentor):
    def rate_hw(self, student, course, grade):
        '''Оценка студента'''
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.all_grades.append(grade)
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'\n  Проверяющий\nИмя: {self.name} \nФамилия:  {self.surname}'

olga_student = Student('Ольга', 'Иванова', 'жен')
olga_student.courses_in_progress += 'Python', 'Git',
olga_student.finished_courses += 'Введение в программирование',
olga_student.finished_courses += 'java',

dmitriy_student = Student('Дмитрий', 'Иванов', 'муж')
dmitriy_student.courses_in_progress += 'Python',
dmitriy_student.courses_in_progress += 'Git',
dmitriy_student.finished_courses += 'Введение в программирование',

vladimir_rewiewer = Rewiewer('Владимир', 'Кузнецов')
vladimir_rewiewer.courses_attached += ['Python']

michail_rewiewer = Rewiewer('Михаил', 'Владимиров')
michail_rewiewer.courses_attached = ['Git']

svetlana_lecturer = Lecturer('Светлана', 'Андреева')
svetlana_lecturer.courses_attached += ['Git']

andrey_lecturer = Lecturer('Андрей', 'Васильев')
andrey_lecturer.courses_attached += ['Python']

vladimir_rewiewer.rate_hw(dmitriy_student, 'Python', 10)
vladimir_rewiewer.rate_hw(dmitriy_student, 'Python', 8)
vladimir_rewiewer.rate_hw(dmitriy_student, 'Python', 9)
michail_rewiewer.rate_hw(dmitriy_student, 'Git', 9)
michail_rewiewer.rate_hw(dmitriy_student, 'Git', 9)
michail_rewiewer.rate_hw(dmitriy_student, 'Git', 8)
vladimir_rewiewer.rate_hw(olga_student, 'Python', 10)
vladimir_rewiewer.rate_hw(olga_student, 'Python', 9)
vladimir_rewiewer.rate_hw(olga_student, 'Python', 5)
michail_rewiewer.rate_hw(olga_student, 'Git', 6)
michail_rewiewer.rate_hw(olga_student, 'Git', 8.4)
michail_rewiewer.rate_hw(olga_student, 'Git', 10)
olga_student.rate_lec(andrey_lecturer, olga_student,  'Python', 10)
olga_student.rate_lec(andrey_lecturer, olga_student,  'Python', 8.5)
olga_student.rate_lec(andrey_lecturer, olga_student,  'Python', 9.2)
olga_student.rate_lec(svetlana_lecturer, olga_student,  'Git', 8)
olga_student.rate_lec(svetlana_lecturer, olga_student,  'Git', 9)
olga_student.rate_lec(svetlana_lecturer, olga_student,  'Git', 7)

print(andrey_lecturer)
print(svetlana_lecturer)
print(vladimir_rewiewer)
print(michail_rewiewer)
print(olga_student)
print(dmitriy_student)
dmitriy_student.comparison_grades(olga_student)
andrey_lecturer.comparison_grades(svetlana_lecturer)

courses_list = ['Python', 'Git']
students_list = [olga_student, dmitriy_student]
lecturers_list = [svetlana_lecturer, andrey_lecturer]
def average_rating_students(students_list, courses_list):
    course_0 = []
    course_1 = []
    for course in courses_list:    
        for student in students_list:
            if course is courses_list[0] and courses_list[0] in student.grades.keys():
                course_0 += student.grades[courses_list[0]]
            elif course is courses_list[1] and courses_list[1] in student.grades.keys():
                course_1 += student.grades[courses_list[1]]            
    print(f'\nСредняя оценка среди студентов по курсу {courses_list[0]}: {round(sum(course_0) / len(course_0), 2)} \nСредняя оценка среди студентов по курсу {courses_list[1]}: {round(sum(course_1) / len(course_1), 2)} ')
average_rating_students(students_list, courses_list)

def average_rating_lecturer(lecturers_list, courses_list):
    course_0 = []
    course_1 = []
    for course in courses_list:    
        for lecturer in lecturers_list:
            if course is courses_list[0] and courses_list[0] in lecturer.grades.keys():
                course_0 += lecturer.grades[courses_list[0]]
            elif course is courses_list[1] and courses_list[1] in lecturer.grades.keys():
                course_1 += lecturer.grades[courses_list[1]]             
    print(f'\nСредняя оценка среди лекторов по курсу {courses_list[0]}: {round(sum(course_0) / len(course_0), 2)} \nСредняя оценка среди лекторов по курсу {courses_list[1]}: {round(sum(course_1) / len(course_1), 2)} ')
average_rating_lecturer(lecturers_list, courses_list)   