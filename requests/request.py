import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
s = 'https://stepic.org/media/attachments/course67/3.6.3/'
while not (r.text[0] == 'W' and r.text[1] == 'e'):
    s = s + r.text.strip()
    r = requests.get(s)
    s = 'https://stepic.org/media/attachments/course67/3.6.3/'
    print(r.text)
w = open("file.txt", 'w')
w.write(r.text)
