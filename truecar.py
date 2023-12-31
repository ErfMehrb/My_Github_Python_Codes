import requests
from bs4 import BeautifulSoup
import sqlite3

# دریافت اطلاعات ماشین مورد نظر از کاربر
car_name = input("Enter the car model: ")

# درخواست برای دریافت اطلاعات از سایت Truecar
url = f"https://www.truecar.com/used-cars-for-sale/listings/{car_name}/location-san-francisco-ca/?sort[]=best_match"
response = requests.get(url)

# پردازش محتوای صفحه وب با کتابخانه BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# استخراج اطلاعات قیمت و میزان کارکرد ماشین از صفحه وب
cars = soup.find_all("div", {"class": "vehicle-card__info"})

# ایجاد یک دیتابیس جدید
conn = sqlite3.connect("cars.db")
c = conn.cursor()

# ایجاد جدول برای ذخیره اطلاعات ماشین‌ها
c.execute("""CREATE TABLE IF NOT EXISTS cars (
            car_name TEXT,
            price TEXT,
            mileage TEXT
            )""")

# اضافه کردن اطلاعات ماشین‌ها به دیتابیس
for i, car in enumerate(cars[:20]):
    price = car.find("div", {"class": "vehicle-card__price"}).text.strip()
    mileage = car.find("div", {"class": "vehicle-card__mileage"}).text.strip()
    c.execute("INSERT INTO cars VALUES (?, ?, ?)", (car_name, price, mileage))
    print(f"Car {i+1}: {price}, {mileage}")

# ذخیره تغییرات در دیتابیس و بستن ارتباط
conn.commit()
conn.close()
