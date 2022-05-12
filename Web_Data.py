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

