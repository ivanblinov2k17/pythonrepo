import requests, bs4
import datetime

def find_url(faculty, level, name_of_group):
    url = 'https://timetable.spbu.ru'
    url_start = 'https://timetable.spbu.ru'
    type_of_lesson = 'Normal'
    s = requests.get(url)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    li = b.select('.list-group-item')
    a = []
    for i in range(len(li)):
        a.append(li[i].select('a'))
    href_faculty = ''
    for i in a:
        if i[0].string == faculty:
            href_faculty = i[0]['href']
    if href_faculty != '':
        url += href_faculty
        s2 = requests.get(url)
        b = bs4.BeautifulSoup(s2.text, "html.parser")
        panel = b.select('.panel-title')
        a = []
        parameter = ''
        for i in panel:
            a.append(i.select('a'))
        for i in a:
            if i[0].string.find(level) != -1:
                parameter = i[0]['href']
        if parameter != '':
            s3 = requests.get(url + parameter)
            b = bs4.BeautifulSoup(s3.text, "html.parser")
            column = b.select('.col-sm-1')
            a = []
            href_group = ''
            for i in column:
                a.append(i.select('a'))
            for i in a:
                if i != []:
                    if i[0]['title'].find(name_of_group) != -1:
                        href_group = i[0]['href']
            if href_group != '':
                url = url_start + href_group
                s4 = requests.get(url)
                b = bs4.BeautifulSoup(s4.text, "html.parser")
                tile = b.select('.tile')
                column = []
                for i in tile:
                    column.append(i.select('.col-sm-4'))
                href_final = ''
                for i in range(len(column)):
                    if column[i][0].string.find(name_of_group) != -1:
                        if type_of_lesson == 'Normal':
                            if tile[i]['onclick'].find('Primary') != -1:
                                href_final = tile[i]['onclick']
                        else:
                            if tile[i]['onclick'].find('Attestation') != -1:
                                href_final = tile[i]['onclick']
                if href_final != '':
                    url = url_start + href_final[href_final.find("\'") + 1:len(href_final) - 1]
                    return(url)
                else:
                    raise NameError
            else:
                raise NameError
        else:
            raise NameError
    else:
        raise NameError

def para_now(url):
    time = datetime.datetime.now()
    s = requests.get(url)
    b = bs4.BeautifulSoup(s.text, 'html.parser')

fac = 'Applied Mathematics and Control Processes'
lvl = 'Bachelor Studies'
group = '17.Б08-пу'
para_now(find_url(fac,lvl,group))
