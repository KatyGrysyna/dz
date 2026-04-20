class GroupOverflowError(Exception):
    def __init__(self, group_number, max_size=10):
        self.group_number = group_number
        self.max_size = max_size
        super().__init__(
            f'Неможливо додати студента до групи {group_number}: '
            f'перевищено максимальну кількість студентів ({max_size}).'
        )


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}, Ticket: {self.record_book}'


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupOverflowError(self.number, self.MAX_STUDENTS)
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

# --- Тест на перевищення ліміту групи ---
# У групі вже є 1 студент (Jobs), тому додаємо ще 9, щоб досягти ліміту в 10
for i in range(9):
    gr.add_student(Student('Male', 20 + i, f'Name{i}', f'LastName{i}', f'AN{200 + i}'))

assert len(gr.group) == 10, 'Test3: у групі має бути рівно 10 студентів'

# Спроба додати 11-го студента має викликати GroupOverflowError
extra_student = Student('Female', 22, 'Extra', 'Student', 'AN999')
exception_caught = False
try:
    gr.add_student(extra_student)
except GroupOverflowError as e:
    exception_caught = True
    print(f'{e}')

assert exception_caught is True, 'Test4: має бути викинутий GroupOverflowError'
assert len(gr.group) == 10, 'Test5: кількість студентів не повинна змінитися після невдалої спроби'

