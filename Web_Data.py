import urllib.request, urllib.parse, urllib.error
import json
import ssl
import webbrowser

serviceurl = 'http://google.com/finance'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(serviceurl, context=ctx)

Data = uh.read().decode()
Jason = json.loads(Data)

try:
        SectionIndex = Jason['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Options':
                    index = element['index']
                    Signal = -2
except:
        index = 0

if index == 0:
    ServiceURL = 'https://google.com/finance/options'
    uh = urllib.request.urlopen(ServiceURL, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)

    try:
        SectionIndex = Jason1['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Price':
                    index = element['index']
                    Signal = -1
    except:
        index = 0   

uh2 = urllib.request.urlopen(serviceurl2, context=ctx)
data2 = uh2.read().decode()
Jason2 = json.loads(data2)

print('\n')

SectionIndex2 = Jason2['parse']['wikitext']

x = SectionIndex2['*']
list = x.split("*")
list2 = list[0].split('\n')

for word in list2:
    if word.startswith('{| '):
        if Signal == -1:
            print('Options prices')
            webbrowser.open('https://google.com/finance/options')
            exit()

print('\n', 'Options','\n')
count = 0
for Set in list:
    if Set.startswith("''") or Set.startswith(" ''") or Set.startswith(" "):
        count = count + 1
        Set2 = Set.rstrip()
        Set3 = Set2.strip()
        pos = Set3.find('\n')
        pos2 = Set3.find('<ref>')
        if pos == -1 and pos2 == -1:
            print(count,'-',Set3)
        elif pos != -1:
            print(count,'-',Set3[0:pos])
        else:
            print(count,'-',Set3[0:pos2])

print('\n')      

if index == 0:
    serviceurl1 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'_(singer)'+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(serviceurl1, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)

    try:
        SectionIndex = Jason1['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Discography':
                    index = element['index']
                    Signal = 2
    except:
        index = 0      

if index == 0:
    serviceurl1 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NameURL+'_(musician)'+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(serviceurl1, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)

    try:
        SectionIndex = Jason1['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Discography':
                    index = element['index']
                    Signal = 3
    except:
        index = 0

if index == 0:
    NAME1 = NameURL.upper()
    serviceurl1 = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&page='+NAME1+'&prop=sections&disabletoc=1'
    uh = urllib.request.urlopen(serviceurl1, context=ctx)

    Data1 = uh.read().decode()
    Jason1 = json.loads(Data1)
    for x,y in Jason1.items():
        if x == 'error':
            print('\nName could not been found')
            exit()