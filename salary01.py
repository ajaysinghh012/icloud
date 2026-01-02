emp1 = [("Ajay","Singh","T",200),
         ("Shivam","Negi","P",300),
         ("rahul","Tiwari","P",300),
         ("Vikash","Tanwar","P",300),
         ("manish","Rana","T",200)
         ]

list2 = []
for fname,lname,emp_type,salary_per_day in emp1:
    if emp_type == "P":
        salary_per_day = salary_per_day * 10
        print(f"name:{fname}{lname}\nsalary:{salary_per_day}")
        list2.append((fname, lname, emp_type, salary_per_day))
    else:
        list2.append((fname, lname, emp_type, salary_per_day))

print(list2)

