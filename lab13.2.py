
class WORKER:
    __born = 0
    __experience = 0

    def __init__(self,b,e):
        self.born = int(b)
        self.experience = int(e)

    def CalcAge(self):
        age = 2024 - self.born
        return age

    def ShowYear(self):
        born = self.born
        return born
        print(born)

    def SetWork(self, add_exp):
        add_exp = int(add_exp)
        experience = self.experience + add_exp
        return experience

# 3 characters
worker_1 = WORKER(1986,7)
worker_2 = WORKER(1992, 4)
worker_3 = WORKER(2003, 2)

# sum of total experience and age
total_exp = worker_1.experience + worker_2.experience + worker_3.experience
total_age = worker_1.CalcAge() + worker_2.CalcAge() + worker_3.CalcAge()

print(f"\nЗагальний стаж працівників становить: {total_exp}.")
print(f"Загальний вік працівників становить: {total_age}.")