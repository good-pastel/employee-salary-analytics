import csv



from python.employee import Employee

def load_employees(filename):

    employees = []

    with open(filename, mode="r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            employee = Employee(
                int(row["work_year"]),
                row["experience_level"],
                row["employment_type"],
                row["job_title"],
                int(row["salary_in_usd"]),
                row["employee_residence"],
                int(row["remote_ratio"]),
                row["company_location"],
            )

            employees.append(employee)

    return employees
