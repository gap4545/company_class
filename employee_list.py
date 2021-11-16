# Hierarchy of employees using classes and subclasses
# Create a hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. 
# Every one's pay is calculated differently, research a bit about it.
# After you've established an employee hierarchy, create a Company class that allows you to manage the employees. 
# You should be able to hire, fire and raise employees.

#



class Employee():

    def __init__(self, name, percent):

        self.name = name
        self.percent = percent / 100
        self.salary = 0

    def __str__(self):

        return (f'Employee Name: {self.name}\nHourly Wage: ${self.salary}')
    
class HourlyEmployee(Employee):

    def __init__(self, name, percent):

        super().__init__(name, percent)
        self.average_hourly = 20
        self.salary = self.average_hourly * self.percent
    def __str__(self):

        return (f'Employee Name: {self.name}\nSalary: ${self.salary}')
    
    def adjust_salary(self, percent_paid):

        self.percent = percent_paid / 100
        self.salary = (self.average_hourly * self.percent)

class SalariedEmployee(Employee):

    def __init__(self, name, percent):

        super().__init__(name, percent)
        self.average_salary = 56000
        self.salary = self.average_salary * self.percent

    def __str__(self):

        return (f'Employee Name : {self.name}\nSalary: ${self.salary}')
    
    def adjust_salary(self, percent):

        self.percent = percent / 100
        self.salary = self.average_salary * self.percent

class Manager(Employee):

    def __init__(self, name, percent):

        super().__init__(name, percent)
        self.average_salary = 93000
        self.salary = self.average_salary * self.percent

    def __str__(self):

        return (f'Employee Name : {self.name}\nSalary: ${self.salary}')

    def adjust_salary(self, percent):

        self.percent = percent / 100
        self.salary = self.average_salary * self.percent

class Executive(Employee):

    def __init__(self, name, percent):

        super().__init__(name, percent)
        self.average_salary = 220000
        self.salary = self.average_salary * self.percent
    
    def __str__(self):

        return (f'Employee Name : {self.name}\nSalary: ${self.salary}')

    def adjust_salary(self, percent):

        self.percent = percent / 100
        self.salary = self.average_salary * self.percent

class Company():

    def __init__(self):

        self.employee_dict = {}
    
    def __str__(self):

        string = ''
        x = 1
        for i in self.employee_dict.values():
            string += f'{x}: {i.name}'
            x += 1
        return f'Employee list:\n{string}'

    def add_employee(self):

        id = len(self.employee_dict) + 1
        name = input("Please input employee's name.\n")
        while True:

            percent_paid = input('Please input the percent of salary for employee.(Numbers only)\n')
            if percent_paid.isnumeric():
                percent_paid = int(percent_paid)
            else:
                print('Invalid entry. Please enter a number.\n')
            employee_type = input("Please select employee's position:\n1: Hourly Employee\n2: Salaried Employee\n3: Manager\n4: Executive\n")
            if employee_type.isnumeric():
                if 0<int(employee_type)<5:
                    employee_type = int(employee_type)
                    break
                else:
                    print('Invalid entry. Please enter a number')
            else:
                print('Invalid entry. Please enter a number.\n')
        name = name.lower()
        if employee_type == 1:
            self.employee_dict[id] = HourlyEmployee(name, percent_paid)
            print("Employee added to records.")
        elif employee_type == 2:
            self.employee_dict[id] = SalariedEmployee(name, percent_paid)
            print("Employee added to records.")
        elif employee_type == 3:
            self.employee_dict[id] = Manager(name, percent_paid)
            print("Employee added to records.")
        elif employee_type == 4:
            self.employee_dict[id] = Executive(name, percent_paid)
            print("Employee added to records.")

        return None

    def remove_employee(self):

        while True:
            name = input('Please input employee ID to be removed from the employee list.(q to quit)\n')
            if name.isnumeric():
                if int(name) in self.employee_dict.keys():
                    del self.employee_dict[int(name)]
                    print('Employee removed from records.')
                    break
            elif name.lower() == 'q':
                break
            else:
                print('Please enter a valid employee ID.')

def ini_object():

    global joe, bill, jim, meg, employee_list
    joe = Executive('Joe', 90)
    bill = Manager('Bill', 70)
    jim = SalariedEmployee('Jim', 88)
    meg = HourlyEmployee('Meg', 87)

    employee_list = [[1, joe],[2, bill],[3, jim],[4, meg]]

    return None

def company_input():

    while True:

        action = input('Please select an option:\n1: List companies\n2: Access company\n3: Add company\n4: Delete company\n5: Exit\n')
        if action.isnumeric():
            if int(action) in [1, 2, 3, 4, 5]:
                return int(action)
            else:
                print('Please make a valid selection.')
        else:
            print('Please make a valid selection.')

def company_actions():

    global company_dict
    action = company_input()
    action = int(action)
    if action == 1:
        for i in company_dict.keys():
            print(i)
            return action

    elif action == 2:

        while True:
            company_selected = input('Please enter company name to access.(q to quit)\n')
            if company_selected.lower() in company_dict.keys():
                return company_selected
            elif company_selected.lower() == 'q':
                return action
            else:
                print('Please select a valid company')

    elif action == 3:

        while True:
            to_add = input('Enter company name to be added.(q to quit.)\n')
            if to_add.lower() not in company_dict.keys():
                company_dict[to_add.lower()] = Company()
                print('Company added to records.')
                return action
            elif to_add[0].lower() == 'q':
                return action
            else:
                print('Company name already in records. Please delete or enter different company name.')

    elif action == 4:
        
        while True:
            to_del = input('Enter company name to be deleted.(q to quit)\n')
            if to_del.lower() in company_dict.keys():
                del company_dict[to_del]
                print('Company removed from records.')
                return action
            elif to_del.lower() == 'q':
                return action
            else:
                print('Please select a valid company.')
    else:
        return action

def view_employee(company_name):
    
    company = company_dict[company_name]

    while True:
        print(company)
        select_id = input('Please enter employee ID.(q to quit)\n')
        if select_id.isnumeric():
            select_id = int(select_id)
            if select_id in company.employee_dict.keys():
                print(company.employee_dict[select_id])
                break
            else:
                print('Please enter a valid employee ID.')
        elif select_id.lower() == 'q':
            break
        else:
            print('Please enter a valid employee ID.')

def employee_input(company_name):

    company = company_dict[company_name]
    while True:
        action = input('Please select an option.\n1: View employee info\n2: Add employee\n3: Remove employee\n4: Adjust percent of salary paid\n5: Main Menu\n')
        if action.isnumeric() and int(action) in [1,2,3,4,5]:
            action = int(action)
            if action == 1:
                view_employee(company_name)
            elif action == 2:
                company.add_employee()
            elif action == 3:
                company.remove_employee()
            elif action == 4:
                adjust_employee_salary(company_name)
            else:
                return action

def adjust_employee_salary(company_name):

    company = company_dict[company_name]
    while True:
        id = input('Enter employee ID to adjust salary.\n')
        new_percent = input('Input new percent of average to be paid.\n')
        if id.isnumeric() and new_percent.isnumeric():
            id = int(id)
            new_percent = int(new_percent)
            if id in company.employee_dict.keys():
                company.employee_dict[id].adjust_salary(new_percent)
                print('Employee salary has been adjusted.')
                break
            else:
                print('Please enter a valid employee ID.')
        else:
            print('Please enter a valid employee ID.')
                
company_dict = {}

# ini_object()
# wawa = Company()
# print(wawa)
# wawa.add_employee()
# print(wawa)
# wawa.remove_employee()
# print(wawa)
import dill
if __name__ == '__main__':

    dill.load_session('company_list.pkl')
    active = True

    while active == True:

        action1 = company_actions()
        if str(action1) in company_dict.keys():
            action2 = employee_input(str(action1))
        elif action1 == 5:
            active = False
        elif action1 != 5:
            continue
        else:
            print('How did we get here')
            break
    
    dill.dump_session('company_list.pkl')


            

