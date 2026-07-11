from python.node import Node
from python.employee import Employee

# kelas LinkedList
class LinkedList:
# ============INISIASI=====================
    def __init__(self):
        self.head = None

# ===========HELPER========================

    #helper _is valid attribute
    def _is_valid_attribute(self, attribute):
        return attribute in Employee.EXPECTED_TYPES
    #helper _is valid value
    def _validate_value(self, attribute, value):
        expected_type = Employee.EXPECTED_TYPES.get(attribute)

        if expected_type is None:
            return False

        return isinstance(value, expected_type)
    #helper insert between
    def _insert_between(self, previous, current, data):
        new_node = Node(data)
        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            previous.next = new_node
            new_node.next = current
    #helper remove node
    def _remove_node(self, previous, current):
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

# ===========LOW LEVEL API=================

    #method append
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    #method display
    def display(self, limit=None):
        if self.head is None:
            print("Linked list kosong")
            return
        TABLE_WIDTH = 110
        print("=" * TABLE_WIDTH)
        print(
            f"{'No':<4}"
            f"{'Year':<6}"
            f"{'Exp':<6}"
            f"{'Type':<12}"
            f"{'Job Title':<30}"
            f"{'Salary':>12}"
            f"{'Res':>8}"
            f"{'Remote':>10}"
            f"{'Company':>10}"
        )
        print("=" * TABLE_WIDTH)

        current = self.head
        no = 1

        while current:
            employee = current.data

            print(
            f"{no:<4}"
            f"{employee.work_year:<6}"
            f"{employee.experience_level:<6}"
            f"{employee.employment_type:<12}"
            f"{employee.job_title:<30}"
            f"{employee.salary_in_usd:>12}"
            f"{employee.employee_residence:>8}"
            f"{employee.remote_ratio:>10}"
            f"{employee.company_location:>10}"
            )
            if limit is not None and no >= limit:
                break

            current = current.next
            no += 1

        print("=" * TABLE_WIDTH)
        print(f"Total data ditampilkan : {no}")
    #method length
    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next

        return count
    #method delete by index (by row)
    def delete_by_index(self, index):
        if index < 0:
            return False
        current = self.head
        previous = None
        count = 0
        while current:
            if count == index:
                self._remove_node(previous, current)
                return True
            previous = current
            current = current.next
            count += 1
        return False
    #method insert before
    def insert_before_by_index(self, index, data):
        if index < 0:
            return False
        current = self.head
        previous = None
        count = 0
        while current:
            if count == index:
                self._insert_between(previous, current, data)
                return True
            previous = current
            current = current.next
            count += 1
        return False
    #method insert_after
    def insert_after_by_index(self, index, data):
        if index < 0:
            return False
        current = self.head
        count = 0
        while current:
            if count == index:
                self._insert_between(current, current.next, data)
                return True
            current = current.next
            count += 1
        return False
    #method update by index
    def update_by_index(self, index, attribute, value):
        if index < 0:
            return False

        current = self.head
        count = 0

        while current:
            if count == index:
                if not self._is_valid_attribute(attribute):
                    print(f"Atribut'{attribute}' tidak dikenal.")
                    return False

                if not self._validate_value(attribute, value):
                        expected_type = Employee.EXPECTED_TYPES.get(attribute)
                        print(f"{attribute} harus bertipe {expected_type.__name__}")
                        return False

                old_value = getattr(current.data, attribute)
                setattr(current.data, attribute, value)

                print(f"{attribute} berhasil diubah dari {old_value} menjadi {value}")
                return True

            current = current.next
            count += 1

        print("Data tidak ditemukan")
        return False
    
# ============HIGH LEVEL API================

    #method find by
    def find_by(self, attribute, value):
        if not self._is_valid_attribute(attribute):
            print("Attribute tidak dikenal")
            return None

        current = self.head

        while current:
            employee = current.data
            if getattr(employee,attribute) == value:
                return employee

            current = current.next

        return None
    #method filter by
    def filter_by(self, attribute, value):
        filtered_list = LinkedList()
        current = self.head

        if not self._is_valid_attribute(attribute):
            print("Attribute tidak dikenal")
            return filtered_list

        while current:
            employee = current.data
            if getattr(employee, attribute) == value:
                filtered_list.append(employee)
            current = current.next
        return filtered_list
    #method update all by
    def update_all_by(self, attribute, value, target_attribute, new_value):
        if not self._is_valid_attribute(attribute):
            print(f"Atribut'{attribute}' tidak dikenal.")
            return 0

        if not self._is_valid_attribute(target_attribute):
            print(f"Atribut '{target_attribute}' tidak dikenal.")
            return 0

        if not self._validate_value(target_attribute, new_value):
            expected_type = Employee.EXPECTED_TYPES.get(target_attribute)
            print(f"{target_attribute} harus bertipe {expected_type.__name__}")
            return 0

        current = self.head
        updated = 0

        while current:
            employee = current.data

            if getattr(employee, attribute) == value:
                setattr(employee, target_attribute, new_value)
                updated += 1

            current = current.next

        return updated
    #method remove all by
    def remove_all_by(self, attribute, value):
        if not self._is_valid_attribute(attribute):
            print("Attribute tidak dikenal")
            return 0

        previous = None
        current = self.head
        deleted = 0

        while current:
            employee = current.data
            if getattr(employee, attribute) == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                deleted += 1
                current = current.next
            else:
                previous = current
                current = current.next

        return deleted
    
# ============STATISTIC API================  

# ============LEVEL 1 (BASIC)================  

    #method count
    def count(self):
        total = 0
        current = self.head

        while current is not None:
            total += 1
            current = current.next

        return total
    #method total salary
    def total_salary(self):
        total = 0
        current = self.head

        while current is not None:
            total += current.data.salary_in_usd
            current = current.next

        return total
    #method average salary
    def average_salary(self):
        if self.count() == 0:
            return 0

        return self.total_salary() / self.count()
    #method highest salary
    def highest_salary(self):
        if self.head is None:
            return None

        current = self.head
        highest = current.data

        while current is not None:
            if current.data.salary_in_usd > highest.salary_in_usd:
                highest = current.data

            current = current.next

        return highest
    #method lowest salary
    def lowest_salary(self):
        if self.head is None:
            return None

        current = self.head
        lowest = current.data

        while current is not None:
            if current.data.salary_in_usd < lowest.salary_in_usd:
                lowest = current.data

            current = current.next

        return lowest

# ============LEVEL 2 (GROUPING)================ 

    #method count by
    def count_by(self, attribute):

        result = {}

        current = self.head

        while current is not None:

            key = getattr(current.data, attribute)

            if key in result:
                result[key] += 1
            else:
                result[key] = 1

            current = current.next

        return result        
    #method total salary by
    def total_salary_by(self, attribute):

        result = {}

        current = self.head

        while current is not None:

            key = getattr(current.data, attribute)

            if key in result:
                result[key] += current.data.salary_in_usd
            else:
                result[key] = current.data.salary_in_usd

            current = current.next

        return result
    #method average salary by
    def average_salary_by(self, attribute):

        total_salary = self.total_salary_by(attribute)
        total_count = self.count_by(attribute)

        result = {}

        for key in total_salary:
            result[key] = total_salary[key] / total_count[key]

        return result

# ============LEVEL 3 (ADVANCE)================ 

    #method highest salary by
    def highest_salary_by(self, attribute):

        result = {}

        current = self.head

        while current is not None:

            key = getattr(current.data, attribute)

            if key not in result:
                result[key] = current.data

            elif current.data.salary_in_usd > result[key].salary_in_usd:
                result[key] = current.data

            current = current.next

        return result
    #method lowest salary by
    def lowest_salary_by(self, attribute):
    
        result = {}
    
        current = self.head
    
        while current is not None:
    
            key = getattr(current.data, attribute)
    
            if key not in result:
                result[key] = current.data
    
            elif current.data.salary_in_usd < result[key].salary_in_usd:
                result[key] = current.data
    
            current = current.next
    
        return result
    #method salary distribution
    def salary_distribution(self, interval=100000):

        result = {}

        current = self.head

        while current is not None:

            salary = current.data.salary_in_usd

            lower = (salary // interval) * interval
            upper = lower + interval

            bucket = f"{lower // 1000}K-{upper // 1000}K"

            if bucket in result:
                result[bucket] += 1
            else:
                result[bucket] = 1

            current = current.next

        return result

