monthly_mb = 10
no_of_months = 3
total_mb = monthly_mb * (no_of_months + 1)

for i in range(no_of_months):
    used = 5
    total_mb = total_mb - used
print(total_mb)



# monthly_MB = int(input("how much data you get in one month"))
# n = int(input("number of months"))
# excess = 0
#
# for i in range(n):
#     how1 = int(input(f"how much MB you used{i+1}"))
#     excess = excess + monthly_MB- how1
# print(excess + monthly_MB)

