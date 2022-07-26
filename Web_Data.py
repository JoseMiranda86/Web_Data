from optparse import Option
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
        
while True:
    address = input('\n'+'Enter location: ')
    typeofbusiness = input('\n'+'Provide the type of business to search: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':

        print('Location can not be found. Try again')
        continue

    lat = str(js['results'][0]['geometry']['location']['lat'])
    lng = str(js['results'][0]['geometry']['location']['lng'])
    webbrowser.open('https://www.google.com/maps/search/'+typeofbusiness+'/@'+lat+','+lng+',15z/data=!3m1!4b1','\n')
    exit()