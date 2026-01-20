import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"

response = requests.get(URL)

if response.status_code != 200:
    print("Failed to load page")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

job_cards = soup.find_all("div", class_="card-content")

jobs = []

for job in job_cards:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")
    link = job.find("a", string="Apply")

    job_title = title.text.strip() if title else "N/A"
    company_name = company.text.strip() if company else "N/A"
    job_location = location.text.strip() if location else "N/A"
    job_url = link["href"] if link else "N/A"

    jobs.append([job_title, company_name, job_location, job_url])

with open("job_listings.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Company", "Location", "Job URL"])
    writer.writerows(jobs)

print("Job listings saved successfully.")

