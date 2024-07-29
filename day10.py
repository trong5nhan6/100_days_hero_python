class Staff:
    def __init__(self, name, age, address, salary, total_time):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.total_time = total_time

    def show_info(self):
        print(
            f'name: {self.name} age: {self.age} address: {self.address} salary: {self.salary} total_time: {self.total_time}')

    def calculate_bonus(self):
        if self.total_time >= 200:
            bonus = self.salary * 0.2
        elif self.total_time >= 100:
            bonus = self.salary * 0.1
        else:
            bonus = self.salary * 0
        return bonus


staff_A = Staff(name='John', age=30, address='36 street',
                salary=30, total_time=300)
staff_B = Staff(name='Mei', age=38, address='54 street',
                salary=50, total_time=199)
staff_C = Staff(name='Tom', age=22, address='92 street',
                salary=10, total_time=99)
print(staff_A.calculate_bonus())
print(staff_B.calculate_bonus())
print(staff_C.calculate_bonus())
