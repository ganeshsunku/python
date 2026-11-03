# Single inheritance
# Create:
# - Parent class Person.
# - Child class Employee.
# - Person should have a name.
# - Employee should have employee ID and department.
# - Use super().

class Person:
    def __init__(self, name):
        self.name=name

class Employee(Person):
    def __init__(self, name, emp_id, department):
        super().__init__(name)
        self.emp_id=emp_id
        self.department=department

emp=Employee("John", 101, "IT")
print("Name: ", emp.name)
print("EMPID: ", emp.emp_id)
print("DEPARTMENT: ", emp.department)



# Multiple inheritance
# Create two parent classes:
# - EmailNotification
# - SMSNotification
# Create a child class AlertSystem that inherits from both.


class EmailNotification:
    def email_notication(self):
        print("Email notification sent")

class SMSNotification:
    def sms_notification(self):
        print("SMS notification sent")

class AlertSystem(EmailNotification, SMSNotification):
    pass

alert=AlertSystem()
alert.email_notication()
alert.sms_notification()

