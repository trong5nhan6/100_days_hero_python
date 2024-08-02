class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Employee(Person):
    def __init__(self, name, phone, annual_salary, year_of_starting_work):
        super().__init__(name, phone)
        self.annual_salary = annual_salary
        self.year_of_starting_work = year_of_starting_work


class StackEmployee:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.stack) == self.capacity:
            return True
        else:
            return False

    def pop(self):
        return self.stack.pop(-1)

    def push(self, element):
        return self.stack.append(element)

    def top(self):
        return self.stack[-1]
