class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<Person {} {}>'.format(self.name, self.phone)

class Employee(Person):
    def __init__(self, name, phone, position, salary):
        Person.__init__(self, name, phone)
        self.position = position
        self.salary = salary


class Employee2(Person):
    def __init__(self, name, phone, position, salary):
        super().__init__(name, phone)
        self.position = position
        self.salary = salary

    def __repr__(self):
        return '<Person {} {} {} {}>'.format(self.name, self.phone, self.position, self.salary)


m1 = Employee('손창희', 5565, '대리', 200)
print(m1)  # 출력 : <Person 손창희 5565>
m2 = Employee2('손창희', 5565, '대리', 200)
print(m2) # 출력 : <Person 손창희 5565 대리 200>
