import requests
from bs4 import BeautifulSoup
import mysql.connector

# مشخصات دیتابیس
db_config = {
    'user': 'USERNAME',
    'password': 'PASSWORD',
    'host': 'HOST',
    'database': 'DATABASE'
}

# اتصال به دیتابیس
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

# دریافت اطلاعات 200 صفحه‌ی اول
for i in range(1, 201):
    url = f'https://bama.ir/car/all-brands/all-models/all-trims?page={i}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # پردازش و ذخیره اطلاعات هر صفحه
    for car in soup.find_all('article', {'class': 'ad-list-item'}):
        title = car.find('h2').text.strip()
        price = car.find('p', {'class': 'cost'}).text.strip()
        year = car.find('span', {'class': 'year-label'}).text.strip()
        mileage = car.find('span', {'class': 'listdata'}).text.strip().split()[0]
        
        # ذخیره اطلاعات در دیتابیس
        query = ("INSERT INTO cars "
                 "(title, price, year, mileage) "
                 "VALUES (%s, %s, %s, %s)")
        data = (title, price, year, mileage)
        cursor.execute(query, data)
        cnx.commit()

# بستن اتصال به دیتابیس
cursor.close()
cnx.close()
import pandas as pd

# خواندن داده‌ها از فایل csv
df = pd.read_csv("car_data.csv")

# انتخاب ستون‌های مورد نیاز
X = df[['year', 'mileage']]
y = df['price']

# تقسیم داده‌ها به دو بخش آموزشی و تست
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ساخت مدل پیش‌بینی با الگوریتم رگرسیون خطی
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# پیش‌بینی قیمت با ورود داده‌های کاربر
year = int(input("Enter the year of the car: "))
mileage = int(input("Enter the mileage of the car: "))
price = model.predict([[year, mileage]])
print(f"The predicted price for a car with {year} year and {mileage} mileage is: {price[0]}")
