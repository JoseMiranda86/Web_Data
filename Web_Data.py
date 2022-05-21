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

dictio = []

for element in SectionIndex:
    for a, b in element.items():
        if b == 'Price':
            dictio[b] = a

print dictio

for word in list2:
    if word.startswith('{| '):
        if Signal == -1:
            print(diction[0])
            webbrowser.open('https://google.com/finance/options/+'diction[0]'')
            exit()