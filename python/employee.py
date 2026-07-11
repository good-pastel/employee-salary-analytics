class Employee:

    EXPECTED_TYPES = {
        "work_year": int,
        "experience_level": str,
        "employment_type": str,
        "job_title": str,
        "salary_in_usd": int,
        "employee_residence": str,
        "remote_ratio": int,
        "company_location": str,
    }

    def __init__(
            self,
            work_year,
            experience_level,
            employment_type,
            job_title,
            salary_in_usd,
            employee_residence,
            remote_ratio,
            company_location,
    ):
       self.work_year = work_year
       self.experience_level = experience_level
       self.employment_type = employment_type
       self.job_title = job_title
       self.salary_in_usd = salary_in_usd
       self.employee_residence = employee_residence
       self.remote_ratio = remote_ratio
       self.company_location = company_location

    def __str__(self):
        return (f"Work Year: {self.work_year} | Experience Level: {self.experience_level} | Employment Type: {self.employment_type} | Job Title: {self.job_title} | Salary in USD: {self.salary_in_usd} | Employee Residence: {self.employee_residence} | Remote Ratio: {self.remote_ratio} | Company Location: {self.company_location}")

    def display(self):
        print("=" * 80)
        print(f"Work Year           : {self.work_year}")
        print(f"Experience Level    : {self.experience_level}")
        print(f"Employment Type     : {self.employment_type}")
        print(f"Job Title           : {self.job_title}")
        print(f"Salary in USD       : {self.salary_in_usd}")
        print(f"Residence           : {self.employee_residence}")
        print(f"Remote Ratio        : {self.remote_ratio}")
        print(f"Company Location    : {self.company_location}")
        print("=" * 80)