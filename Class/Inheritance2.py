class Person:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<Person {} {}>'.format(self.name, self.phone)


class Employee(Person):
    def __init__(self, name, phone, position, salary):
        super().__init__(name, phone)
        self.position = position
        self.salary = salary

    def __repr__(self):
        s = super().__repr__()
        return s + '<Person {} {}>'.format(self.position, self.salary)


m1 = Employee('손창희', 5565, '대리', 200)
print(m1)  # 출력 : <Person 손창희 5565><Person 대리 200>

