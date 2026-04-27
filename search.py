import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Start the Bot
driver = webdriver.Chrome()
print("Opening OpenToWorkRemote...")
driver.get("https://www.opentoworkremote.com/")

# 2. Wait for the JavaScript and job listings to fully load
time.sleep(5) 

# 3. Find ALL the job containers on the page (Notice the 's' in elements!)
# NOTE: You must change "insert-job-card-class" to the real class you find via Inspect Element
job_cards = driver.find_elements(By.CLASS_NAME, "job-post-info")

print(f"Success! Found {len(job_cards)} jobs on the page.")

extracted_jobs = []

# 4. Loop through every single job card one by one
for card in job_cards:
    try:
        # We search INSIDE the specific card, not the whole page
        # Update these class names based on your Inspect Element reconnaissance
        title = card.find_element(By.CLASS_NAME, "ContentJobs-module__JDk1ha__jobTitle").text
        company = card.find_element(By.CLASS_NAME, "ContentJobs-module__JDk1ha__companyHeader").text
        details = card.find_element(By.CLASS_NAME, "ContentJobs-module__JDk1ha__jobDetails").text
        # Save the data into a dictionary
        job_data = {
            "title": title,
            "company": company,
            "details": details
        }
        extracted_jobs.append(job_data)
        
    except Exception as e:
        # If a job card is missing a field (like salary), we just skip it and keep going!
        continue

# 5. Save everything to your JSON database
with open('remote_jobs_database.json', 'w') as file:
    json.dump(extracted_jobs, file, indent=4)

# 6. Close down the robot
driver.quit()
print("Data extraction complete! Check your JSON file.")