class Employee:
    def getdata(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def showdata(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def get_manager(self):
        self.getdata()

    def show_manager(self):
        self.showdata()


managers = []

for i in range(10):
    print("\nEnter details of Manager", i+1)
    m = Manager()
    m.get_manager()
    managers.append(m)

print("\nManager Details")

for i in managers:
    i.show_manager()
    print()
