class GroupLimitError(Exception):
    """Виняток, якщо група перевищує 10 студентів."""
    def __init__(self, message="Досягнуто ліміт студентів у групі (максимум 10)."):
        self.message = message
        super().__init__(self.message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} років"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Залікова книжка: {self.record_book}"

    def __eq__(self, other):
        return (self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.record_book == other.record_book)

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupLimitError()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Група: {self.number}\n{all_students}'



gr = Group('PD1')

students = [
    Student('Male', 20, 'John', 'Doe', 'AN101'),
    Student('Female', 21, 'Alice', 'Smith', 'AN102'),
    Student('Male', 22, 'Bob', 'Brown', 'AN103'),
    Student('Female', 23, 'Emma', 'White', 'AN104'),
    Student('Male', 24, 'Mike', 'Black', 'AN105'),
    Student('Female', 25, 'Olivia', 'Green', 'AN106'),
    Student('Male', 26, 'David', 'Blue', 'AN107'),
    Student('Female', 27, 'Sophia', 'Red', 'AN108'),
    Student('Male', 28, 'Chris', 'Gray', 'AN109'),
    Student('Female', 29, 'Emily', 'Yellow', 'AN110'),
    Student('Male', 30, 'Steve', 'Jobs', 'AN111')  # 11-й студент
]


for student in students:
    try:
        gr.add_student(student)
        print(f"✅ Додано: {student.first_name} {student.last_name}")
    except GroupLimitError as e:
        print(f"❌ Неможливо додати {student.first_name} {student.last_name}: {e}")


print("\nСписок студентів у групі:")
print(gr)
