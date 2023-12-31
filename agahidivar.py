import requests
from bs4 import BeautifulSoup

# دریافت صفحه وب
url = "https://divar.ir/s/tehran"
page = requests.get(url)

# پردازش محتوای صفحه وب
soup = BeautifulSoup(page.content, "html.parser")

# استخراج آگهی‌های دارای تگ قیمت توافقی
ads = soup.find_all("div", {"class": "post-card__price-tag"})

# چاپ آگهی‌های استخراج شده
for ad in ads:
    if ad.text == "توافقی":
        print(ad.parent.parent.text.strip())
