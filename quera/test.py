import requests
import threading
import time
def fetch_url(url):
    response = requests.get(url)
    print(f'URL: {url}, length: {len(response.text)}')
start_time = time.time() # زمان شروع اجرا
urls = [
'https://www.digikala.com/',
'https://snapp.ir/',
'https://www.aparat.com/',
'https://divar.ir/',
'https://shaparak.ir/',
'https://namnak.com/',
'https://www.digikala.com/',
'https://snapp.ir/',
'https://www.aparat.com/',
'https://divar.ir/',
'https://shaparak.ir/',
'https://namnak.com/',
]
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()
end_time = time.time() # زمان پایان اجرا
execution_time = end_time - start_time # محاسبه مدت زمان اجرا به صورت دقیق
print(f'run time with thread: {execution_time} s')