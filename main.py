employees = [] 
employees.append({"name": "Alice", "availability": ["Monday", "Wednesday", "Friday"], "skills": ["CHR"]})
employees.append({"name": "Bob", "availability": ["Monday", "Tuesday","Wednesday", "Thursday", "Friday"], "shift_preference": "Evening", "skills": ["CS"]}) 

# ... add more employees as needed
# Display employee information
for employee in employees:
	print("Name:", employee["name"])
	print("Availability:", employee["availability"])
	if "shift_preference" in employee:  # Check if this key exists 
		print("Shift Preference:", employee["shift_preference"])
	print("------")  # Print a separator between employees 

shifts = [
	{
		"name": "Morning Shift",
		"start_time": "8:00 AM",
		"end_time": "4:00 PM",
		"positions": ["CHR", "CS", "ENT", "ALC"],
		"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	},
	# ... define "Evening Shift" similarly
]


def find_matching_employees(shift):
    matched_employees = []
    for position in shift["positions"]: 
        for employee in employees:
            if all(day in employee["availability"] for day in shift["days"]):
                if position in employee["skills"]:
                    matched_employees.append({
                        'shift': shift['name'],
                        'position': position,
                        'employee': employee
                    })
                    break # Now exits only the inner loop
    return matched_employees # Now executes after both loops finish




morning_shift = shifts[0]
matched_employees, shift_name = find_matching_employees(morning_shift)  # Capture both values
print("------ Debugging Info ------")
print("Shift:", shift_name)
print("Matched Employees:", matched_employees) 
