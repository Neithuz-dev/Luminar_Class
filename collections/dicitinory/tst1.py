employee = {"id":"Em001","name":"adhil","age": 45}
employee["prof"] = "data analytics"
print(employee)

employee["age"] = 56
# print(employee)

# print(employee.keys())
# print(employee.values())
# print(employee.items())

# for key,val in employee.items():
#     print(key,",",val)
# print(employee.get("skill", 0))
employee.update({"exp":2})
print(employee)

employee.pop("exp")
print(employee)
print('-'*100)
new_emp = employee.copy()
print(new_emp)

new_emp.clear()
print(new_emp)