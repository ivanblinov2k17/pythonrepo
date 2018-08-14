import requests
import re
f = open("input.txt", 'rt')
s = []
for line in f:
    s.append(line)
res1 = requests.get(s[0])
print(s[0])
print(res1.text)
#res2 = re.findall('https://\w+?>', res1.content)
#print(res2)
#for i in res2:

#print(res.status_code)
#print(res.headers['Content-Type'])
#print(res.content)
