from python.linked_list import LinkedList
from python.csv_loader import load_employees



employees = load_employees("ds_salaries.csv")

ll = LinkedList()

for employee in employees:
    ll.append(employee)

result = ll.highest_salary_by("experience_level")

print(result["SE"].job_title)
print(result["SE"].salary_in_usd)
print(result["SE"].experience_level)
print(result["SE"].work_year)

distribution = ll.salary_distribution()

for bucket, total in distribution.items():
    print(f"{bucket} : {total}")