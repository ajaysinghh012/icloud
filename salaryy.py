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
