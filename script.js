// --- Data ---

fetch('employees.json')
  .then(response => response.json()) // Parse the data as JSON
  .then(data => {
	// Here, 'data' holds the parsed JSON, i.e., your employees array
	employees = data; // Replace your placeholder or hard-coded employees array

	// Now you can proceed with processCSVData as normal!
	processCSVData(csvData);

	//  Other scheduling logic might occur here, or in its own function 
  })
  .catch(error => {
	console.error('Error loading employees.json:', error);
  });

// --- Functions ---

// Handles CSV file uploads
function handleFileUpload(event) {
  // Keep File Retrieval Here
  let file = event.target.files[0]; 
  let reader = new FileReader(); 
  reader.readAsText(file); 

  // Process CSV and Schedule Updates
  reader.onload = function() {
	let csvData = reader.result; 
	processAndSchedule(csvData); // Let's make a dedicated function for this!
  };
}

function processAndSchedule(csvData) {
  let updatedEmployees = processCSVData(csvData);

  // Placeholder for future scheduling logic - we'll call functions from  logic.js?
  // Maybe:  const finalSchedule = performScheduleMatching(updatedEmployees); 

  uploadStatus.textContent = "Schedule Updated!";  
}

	let file = event.target.files[0]; 
	  let reader = new FileReader(); 
	  reader.readAsText(file); 

	// After the file is loaded:
	reader.onload = function() {
		let csvData = reader.result; 
		
		// 2. Show Loading Indicator 
		uploadStatus.textContent = "Processing CSV, please wait..."; // Or a loader image, etc.

		processCSVData(csvData); 
	};


// Processes uploaded CSV data
function processCSVData(csvData) {
	let rows = csvData.split("\n"); 

					for (let i = 1; i < rows.length; i++) { 
						let cells = rows[i].split(",");

						const employeeId = cells[0];
						const timeIn = cells[1];
						const timeOut = cells[2];

						// Find matching employee in your hardcoded 'employees' array
						const existingEmployee = findEmployeeById(employeeId);

						if (existingEmployee) {
						  // Only update if the employee exists in your hardcoded data
						  existingEmployee.timeIn = timeIn;
						  existingEmployee.timeOut = timeOut;
						} else {
						  // Ignore any IDs not found in your 'employees' array
						}
					  }
					}
					
			return employees;  // Add to end to provide result of  the work
		}
	}

}

// Generates a CSV string from current employee data
function generateCSV() { 
	let csvString = "Employee Name, Start Time, Assigned Zone\n"; 
	for (let i = 0; i < employees.length; i++) {
		let employee = employees[i];
		let row = employee.name + "," + employee.startTime + "," + employee.zone + "\n";
		csvString += row; 
	}
	return csvString; 
}

// Triggers a CSV file download 
function downloadCSV() { 
	let csvData = generateCSV(); 
	let blob = new Blob([csvData], { type: 'text/csv;charset=utf-8;' }); 

	// Create a temporary download link
	let url = window.URL.createObjectURL(blob);
	let link = document.createElement('a');
	link.href = url;
	link.download = 'schedule.csv';
	link.click(); // Simulate a click on the link 

	window.URL.revokeObjectURL(url); // Clean up
}

// --- Event Listeners (Connecting buttons to actions) ---
	document.addEventListener('DOMContentLoaded', function() {
		// File Upload Button
		let fileInput = document.getElementById("scheduleUpload");
		fileInput.addEventListener("change", handleFileUpload); 
		// Download Button
		let downloadButton = document.getElementById("downloadBtn");
		downloadButton.addEventListener("click", downloadCSV);
	});

function handleFileUpload(event) { 
//  ... (Upload your file) ...

reader.onload = function() {
	let csvData = reader.result; 

	// Get processed, up-to-date employees  
	let updatedEmployees = processCSVData(csvData);

	uploadStatus.textContent = "Schedule Updated!"; 
};
