import requests
from concurrent.futures import ThreadPoolExecutor
import time

url = 'http://127.0.0.1:52389/api/items/'

def send_request():
    response = requests.get(url)
    print(response.status_code)

start_time = time.time()

with ThreadPoolExecutor(max_workers=5000) as executor:
    futures = [executor.submit(send_request) for _ in range(5000)]

end_time = time.time()

total_time = end_time - start_time
print(f"Total time taken: {total_time} seconds")
