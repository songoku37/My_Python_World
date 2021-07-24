class MyClass3:
    def __init__(self):
        self.value = 0

    def get(self):
        return self.value


c = MyClass3()
c.get()  # 출력 : 0


class MyClass4:
    def __init__(self, name, nic, birthday):
        self.name = name
        self.nick = nic
        self.birthday = birthday

m1 = MyClass4('이열', '해안선', '1995-4-3')
