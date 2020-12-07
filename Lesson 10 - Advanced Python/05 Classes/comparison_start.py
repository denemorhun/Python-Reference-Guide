# Use special methods to compare objects to each other


class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService

    # TODO: implement comparison functions by emp level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.seniority > other.seniority
        
    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.seniority < other.seniority

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.seniority == other.seniority


def main():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 90))
    dept.append(Employee("Rebecca", "Robinson", 5, 11))
    dept.append(Employee("Tyler", "Durden", 5, 12))

    # TODO: Who's more senior?
    print(dept[0] > dept[1])
    print(dept[1] > dept[0])

    print(dept[1] > dept[4])
    print(dept[3] > dept[4])

    # TODO: sort the items, uses these funcs, sorted would work
    emps = sorted(dept)
    for emp in emps:
        print(emp.fname, emp.lname, emp.seniority)


if __name__ == "__main__":
    main()
