import requests
from dotenv import dotenv_values
from bs4 import BeautifulSoup
import mail_service
config = dotenv_values(".env")

response = requests.get(config.get("DOCTOR_URL"))
soup = BeautifulSoup(response.content, 'html.parser')
doctor_name = None

for row in soup.select('div.doctor-name'):
    doctor_name = row.find('h1', class_='heading-2').getText()
available = None
earliest = None
for row in soup.select('div.next-appointment'):
    earliest = row.find('small').getText()
    available = row.find('span').getText()

print("Doctor: ", doctor_name)
if available == "В момента няма свободни часове":
    print(available)
else:
    mail_service.send_email(
        "Superdoc: Doctor's appointment available",
        mail_service.load_html_file("doctor.html").render(doctor_name=doctor_name, earliest=earliest, available=available),
        config['RECEIVERS_SUPERDOC'].split(","),
    )
