employees = [
	{"name": "Alice", "id": 1234, "skills": ["Cashier", "CS"], "start": "8:00 AM", "end": "9:30 AM"},
	{"name": "Bob", "id": 5678, "skills": ["CS"], "start": "8:30 AM", "end": "10:00 AM"},
	{"name": "Charlie", "id": 9101, "skills": ["Cashier", "CS"], "start": "8:00 AM", "end": "10:00 AM"},
]

daily_skill_needs = {
	"8:00 AM - 9:00 AM": ["Cashier"],
	"9:00 AM - 10:00 AM": ["Cashier", "CS"], 
	# ... covering your 8AM to 10PM timeframe
}
def assign_employees_to_zones(employees, daily_skill_needs):
	assignments = {} # This needs to be at the function's start
	# ... 
	for hour_block, needed_skills in daily_skill_needs.items(): 
		print(f"--- Starting Hour: {hour_block} ---")  # Mark each hour's checks
		for skill in needed_skills:  
			for employee in employees:
					if skill in employee["skills"] and is_employee_available_during(employee, hour_block):
						print(f"{employee['name']} CAN fullfill {skill} during {hour_block}")  # Still diagnostic print as before
					# Before assignment checks:
					if hour_block not in assignments:
						assignments[hour_block] = {} 
						if skill not in assignments[hour_block]: 
							assignments[hour_block][skill] = employee['name'] 
							break  # Exit the 'skill' loop - employee assigned for this hour
def is_employee_available_during(employee, hour_block):
	return employee['start'] <= hour_block and employee['end'] > hour_block
	
return assignments 


schedule = assign_employees_to_zones(employees, daily_skill_needs)  # Capture output
print(schedule)

	# Logic to assign employees for this 'hour_block' and its 'needed_skills' will go here


