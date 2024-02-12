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
	for position in shift["positions"]:  # Iterate through needed positions
		for employee in employees:
			# ... add availability check as before ...
			if position in employee["skills"]:  # Match the needed position
				matched_employees.append({ 
					'shift': shift['name'],  
					'position': position, 
					'employee': employee 
				})
				break  # Position filled, move on to the next 
	return matched_employees 


morning_shift = shifts[0]
matched_employees, shift_name = find_matching_employees(morning_shift)  # Capture both values
print("------ Debugging Info ------")
print("Shift:", shift_name)
print("Matched Employees:", matched_employees) 
