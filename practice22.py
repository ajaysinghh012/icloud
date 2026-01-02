employees =[
    ("Ajay","Singh","P",10,300),
    ("Mahavir","Singh","T",20,300),
    ("Mohan","sukla","P",15,300),
]

for first_name, last_name, emp_type, no_of_days, salary_per_day in employees:
    if emp_type == "P":
        salary_per_day += 50
    salary = salary_per_day * no_of_days
    print(f"Name: {first_name} {last_name} Salary: {salary}")

class Item:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

def gst(items):
    total = 0
    for item in items:
        if item.category == 'Medicine':
            total += item.cost * 10

item = [
    (

)]

    return total

print(gst([
    ()
]))