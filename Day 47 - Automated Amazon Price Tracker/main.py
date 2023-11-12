import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
# finding the price of the product in the a-price-whole class
price = soup.find('span', class_='aok-offscreen').getText()
# removing the $ sign from the price
price_without_currency = price.split("$")[1]
# converting the price to float
price_as_float = float(price_without_currency)

# title of the product
product_title = soup.find(id="productTitle").getText().strip()

# email notification when the price is below 100

BUY_PRICE = 130
EMAIL = os.environ.get("YOUR_EMAIL_ADDRESS")
PASSWORD = os.environ.get("YOUR_EMAIL_PASSWORD")
EMAIL_TO = os.environ.get("EMAIL_TO")

if price_as_float < BUY_PRICE:
    message = (f"Subject: Amazon Price Alert!\n\n"
               f"Hey there,\n"
               f"The {product_title} you were looking for is now {price_as_float}\n"
               f"You can buy it at: {URL}")
    # sending email

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL_TO,
            msg=message.encode('utf-8')
        )
