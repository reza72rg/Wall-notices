
import requests
from bs4 import BeautifulSoup


url = 'https://divar.ir/s/tehran'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
objs = soup.find_all('div',{'class':"post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46"})
x = ['توافقی' , 'پرداخت توافقی','اجاره: توافقی']
for obj in objs:
    try:
        title = obj.find('h2', {'class': 'kt-post-card__title'}).text.strip()
        lable  = obj.find('div', {'class': 'kt-post-card__description'}).text.strip() 
        if lable in x:
            print(title)
    except:
        pass
