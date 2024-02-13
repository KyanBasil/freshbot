employees = [
	{"name": "Alice", "id": 1234, "skills": ["Cashier", "CS"]},
	{"name": "Bob", "id": 5678, "skills": ["CS"]},
	# ... more employees
]

daily_skill_needs = {
	"8:00 AM - 9:00 AM": ["Cashier"],
	"9:00 AM - 10:00 AM": ["Cashier", "CS"], 
	# ... covering your 8AM to 10PM timeframe
}
def assign_employees_to_zones(employees, daily_skill_needs):
	assignments = {}

	for hour_block, needed_skills in daily_skill_needs.items(): 
		for skill in needed_skills:  
			for employee in employees:
				if skill in employee["skills"]:
					# Before assignment, let's check our 'assignments' log:
					if hour_block not in assignments:
						assignments[hour_block] = {}  # Create  entry for hour if first time
					if skill not in assignments[hour_block]:
						assignments[hour_block][skill] = employee['name'] # Make assignment!
					print(assignments) 

 
	# Logic to assign employees for this 'hour_block' and its 'needed_skills' will go here
 
print(employees) 
print(daily_skill_needs)

assign_employees_to_zones(employees, daily_skill_needs)  # Currently  does nothing
