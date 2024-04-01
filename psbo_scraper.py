import requests
import mail_service
from dotenv import dotenv_values
from bs4 import BeautifulSoup

config = dotenv_values(".env")
session = requests.Session()

login = session.post('https://psbo.uni-sofia.bg/payments/login',
                     data=[
                         ('username', config['PSBO_USERNAME']),
                         ('password', config['PSBO_PASSWORD']),
                         ('fn', config['PSBO_FN']),
                     ])

response = session.get('https://psbo.uni-sofia.bg/payments/preview/unpaid')
soup = BeautifulSoup(response.content, 'html.parser')
finalString = ""
mail_threshold = config['PSBO_MAIL_THRESHOLD']
print(response.status_code)
for row in soup.select('tbody'):
    finalString += row.find('td', class_='no').getText()

if finalString != "":
    sumToPay = (finalString.replace('\n', ' ').
                replace(' ', '').
                replace('лв.', '').
                replace(',', '.'))
    if float(sumToPay) >= float(mail_threshold):
        mail_service.send_email(
            "PSBO: Payments needed",
            mail_service.load_html_file("psbo.html").render(sumToPay=sumToPay),
            config['RECEIVERS_PSBO'].split(","),
        )
else:
    for row in soup.select('tbody'):
        for row1 in row.select('tr'):
            for row2 in row1.select('td'):
                finalString += row2.getText().replace('\n', ' ')

# if finalString.find("Няма задължения, по които да се започне плащане"):
#     mail_service.send_email(
#         "PSBO: No payments needed",
#         mail_service.load_html_file("psbo.html").render(sumToPay="0"),
#         config['RECEIVERS_PSBO'].split(","),
#     )
