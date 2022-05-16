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
            for x, y in element.items():
                if y == 'Options':
                    index = element['index']
except:
        index = 0

if index == 0:
    ServiceURL = 'https://google.com/finance/options'
    uh = urllib.request.urlopen(ServiceURL, context=ctx)

    Data = uh.read().decode()
    Jason = json.loads(Data)

    try:
        SectionIndex = Jason['parse']['sections']
        for element in SectionIndex:
            for a, b in element.items():
                if b == 'Price':
                    index = element['index']
                    Signal = -1
    except:
        index = 0   

uh2 = urllib.request.urlopen(ServiceURL, context=ctx)
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
