employees = [
	{"name": "Alice", "id": 1234, "skills": ["Cashier", "CS"], "start": "8:00", "end": "9:30"},
	{"name": "Bob", "id": 5678, "skills": ["CS"], "start": "8:30", "end": "10:00"},
	{"name": "Charlie", "id": 9101, "skills": ["Cashier", "CS"], "start": "8:00", "end": "10:00"},
]

daily_skill_needs = {
	"8:00 - 9:00": ["Cashier"],
	"9:00 - 10:00": ["Cashier", "CS"], 
}

SKILL_PRIORITY = ['CS', 'Cashier'] 

def assign_employees_to_zones(employees, daily_skill_needs):
	assignments = {}
	assigned_roles = {} 

	for hour_block, needed_skills in daily_skill_needs.items():
		print(f"Needed Skills: {needed_skills}")
		print(f"--- Starting Hour: {hour_block} ---")

		for skill in needed_skills:
			skill_already_filled = skill in assignments.get(hour_block, {})
			if hour_block not in assignments:
				assignments[hour_block] = {}
			if not skill_already_filled:
				if skill not in assignments[hour_block]:  
					for employee in employees:
						if employee['name'] in assigned_roles and assigned_roles[employee['name']][0] == hour_block:
							continue 

						# Prioritization Check (Modified Approach)
						if len(assignments[hour_block]) > 0: 
							prioritize_existing = False
							for existing_skill in assignments[hour_block]: 
								existing_priority = SKILL_PRIORITY.index(existing_skill)
								if SKILL_PRIORITY.index(skill) <= existing_priority: 
									prioritize_existing = True 
									break 

							if not prioritize_existing: 
								if SKILL_PRIORITY.index(skill) < SKILL_PRIORITY.index("Cashier"): 
									print(f"Considering (with relaxed priority)  {employee['name']} (Skills: {employee['skills']}) for {skill} in hour {hour_block}") 
									if is_employee_available_during(employee, hour_block):
										print(f"{employee['name']} IS available at start of {hour_block}") 
										if not is_employee_available_by_end(employee, hour_block): 
											print(f"{employee['name']} not available due to early shift end")
											continue 
										assignments[hour_block][skill] = employee['name'] 
						else:
							if is_employee_available_during(employee, hour_block):
								print(f"{employee['name']} IS available at start of {hour_block}")
								if not is_employee_available_by_end(employee, hour_block):
									print(f"{employee['name']} not available due to early shift end")
									continue

						assigned_roles[employee['name']] = (hour_block, skill) 
						break  
	return assignments

def is_employee_available_during(employee, hour_block):
	start_hour, start_minute = map(int, employee['start'].split(":"))
	end_hour, end_minute = map(int, employee['end'].split(":"))
	hour_block_start, hour_block_end = map(int, hour_block.split("-")[0].split(":")) 

	return hour_block_start >= start_hour and hour_block_end <= end_hour 

def is_employee_available_by_end(employee, hour_block):
	start_hour, start_minute = map(int, employee['start'].split(":"))
	end_hour, end_minute = map(int, employee['end'].split(":"))
	hour_block_start, hour_block_end = map(int, hour_block.split("-")[0].split(":")) 

	return end_hour > hour_block_end 

schedule = assign_employees_to_zones(employees, daily_skill_needs)
