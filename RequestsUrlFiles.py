import requests

with open('dataset_3378_3.txt') as f:
    url = f.read().strip() # https://stepic.org/media/attachments/course67/3.6.3/699991.txt
    print(url)
n = 0
while True:
    n += 1
    print(n, url)
    url = requests.get(url).text
    if url.startswith('We'): # Ищем текст в файле, котором начинается с "We"
        print(url)
        break
    url = "https://stepic.org/media/attachments/course67/3.6.3/" + url
