import requests

with open('dataset_3378_2-2.txt') as f:
    url = f.read().strip()
    print(url)
r = requests.get(url)
lines = r.text.splitlines()
print(len(lines))

'''
url = 'site.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)
print(r.url)
'''

'''
len(open('file.txt').readlines())
'''