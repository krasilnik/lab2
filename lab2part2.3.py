# The class GROUP contains a sequence of instances of the class STUDENT.
# The class STUDENT contains the student's
# name, surname, record book number and grades.
# Determine the required attributes-data and attributes-methods in classes GROUP
# and STUDENT. Find the average score of each student. Output to the standard output
# stream the five students with the highest average score.
# Assume that there can be no more than 20 students in a group, as well
# as students with the same name and surname.

max = 20

class Student:
    def __init__(self, name, surname, rb_number, *grades):
        self.name = name
        self.surname = surname
        self.rb_number = rb_number
        self.grades = grades

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name's type must be sting")
        if not name:
            raise ValueError("Please enter the student's name")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Surname's type must be sting")
        if not surname:
            raise ValueError("Please enter the student's surname")
        self.__surname = surname

    @property
    def rb_number(self):
        return self.__rb_numnber

    @rb_number.setter
    def rb_number(self, rb_number):
        if not isinstance(rb_number, int):
            raise TypeError("Record book's type must be int")
        self.__rb_number = rb_number

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(index, int) for index in grades):
            raise TypeError("Grade's type must be int")
        if not all(grades):
            raise ValueError("Grades sequence cannot be empty!")
        self.__grades = grades

    @property
    def average_score(self):
        return round(sum(self.grades) / len(self.grades), 1)

    def __str__(self) -> str:
        return f'Name: {self.name}\nSurname: {self.surname}\nRecord book number: {(self.rb_number)}\n' \
               f'Grades: {self.grades}\nAverage: {self.average_score}\n\n'

class Group:

    def __init__(self, *students):
        self.students = students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, list_of_students):
        if not list_of_students:
            raise ValueError("Group cannot be empty!")
        if len(list_of_students) > max:
            raise ValueError("Group must contain less than 20 students")
        if isinstance(all(list_of_students), Student):
            raise TypeError("Students must be Student type")
        if self.duplicates(list_of_students):
            raise ValueError("Group cannot have students with the same names and surnames")
        self.__students = list(list_of_students)

    def best_student(self):
        self.students.sort(key=lambda x: x.average_score, reverse=True)

    @staticmethod
    def duplicates(list_of_students):
        counter = 0
        names = set()
        for i in list_of_students:
            names.add(i.name + i.surname)
            counter += 1
        if counter > len(names):
            return True
        return False

    def __str__(self):
        field = ""
        for index in self.students[:5]:
            field += str(index) + "\n"
        return f'{field}'



s1 = Student('Ivan', 'Krasilnik', 3, 2, 5, 4, 5, 4, 1)
s2 = Student('Danil', 'Stanus', 3, 4, 2, 5, 1, 3, 2)
s3 = Student('Dima', 'Peresh', 1, 3, 1, 4, 2, 3, 4)
s4 = Student('Victor', 'Madzigon', 3, 2, 3, 5, 5, 5, 5)
s5 = Student('Vladimir', 'Colin', 2, 3, 2, 4, 1, 4, 5)
group = Group(s1, s2, s3, s4, s5)
group.best_student()
print(group)




