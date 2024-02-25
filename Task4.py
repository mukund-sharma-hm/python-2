from faker import Faker
import openpyxl
import random

# Generate fake employee data and save it to an Excel file
def generate_fake_employee_data():
    fake = Faker()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Employee ID", "Employee Name", "Email", "Business Unit", "Salary"])
    for _ in range(random.randint(50, 100)):
        ws.append([
            fake.uuid4(),
            fake.name(),
            fake.email(),
            fake.random_element(elements=('HR', 'IT', 'Finance', 'Operations')),
            fake.random_int(min=30000, max=150000)
        ])
    wb.save("employee_details.xlsx")

    # Find employee with the highest salary
    def find_employee_with_highest_salary():
        wb = openpyxl.load_workbook("employee_details.xlsx")
        ws = wb.active
        max_salary = max(ws.iter_rows(min_row=2, min_col=5, values_only=True), key=lambda x: x[0])[0]
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=5, max_col=5, values_only=True):
            if row[0] == max_salary:
                return row[0]

    # Find the business unit with the highest aggregated salary
    def find_unit_with_highest_aggregated_salary():
        wb = openpyxl.load_workbook("employee_details.xlsx")
        ws = wb.active
        unit_salaries = {}
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=4, max_col=5, values_only=True):
            if len(row) >= 2:  # Check if the tuple has at least two elements
                if row[0] not in unit_salaries:
                    unit_salaries[row[0]] = row[1]
                else:
                    unit_salaries[row[0]] += row[1]
        if unit_salaries:
            return max(unit_salaries, key=unit_salaries.get)
        else:
            return None  # Return None if there are no unit salaries


    # Find the employee with the highest salary in each business unit
    def find_top_salary_per_unit():
        wb = openpyxl.load_workbook("employee_details.xlsx")
        ws = wb.active
        unit_salaries = {}
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=4, max_col=5, values_only=True):
            if row[0] not in unit_salaries:
                unit_salaries[row[0]] = [(row[1], row[2])]
            else:
                unit_salaries[row[0]].append((row[1], row[2]))
        top_salary_per_unit = {}
        for unit, salaries in unit_salaries.items():
            top_salary_per_unit[unit] = max(salaries, key=lambda x: x[0])
        return top_salary_per_unit

    # Delete the record of the employee with the least salary
    def delete_employee_with_least_salary():
        wb = openpyxl.load_workbook("employee_details.xlsx")
        ws = wb.active
        min_salary = min(ws.iter_rows(min_row=2, min_col=5, values_only=True), key=lambda x: x[0])[0]
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=5, max_col=5):
            if row[0].value == min_salary:
                ws.delete_rows(row[0].row)
                break
        wb.save("employee_details.xlsx")

    # Update the salary details of an employee
    def update_employee_salary(emp_id, new_salary):
        wb = openpyxl.load_workbook("employee_details.xlsx")
        ws = wb.active
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=5):
            if row[0].value == emp_id:
                row[4].value = new_salary
                break
        wb.save("employee_details.xlsx")

    
    print("Employee with the top salary:", find_employee_with_highest_salary())
    print("Business unit with the highest aggregated salary:", find_unit_with_highest_aggregated_salary())
    print("Top salary per unit:", find_top_salary_per_unit())
    delete_employee_with_least_salary()
    update_employee_salary(emp_id="ID123", new_salary=75000)


generate_fake_employee_data()
