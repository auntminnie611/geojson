import json
import ssl
import urllib.request,urllib.parse,urllib.error
urladdress= 'http://py4e-data.dr-chuck.net/json'

api_key='AIzaSyA70J7_qvIc067Tt6q2BEY1Fczz5pLIN0k'

#ignore cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    address=input('enter location:')
    if len(address)<1:
        break
    parms=dict()
    parms['address']=address
    if api_key is not False:
        parms['key']=api_key
        geourl=urladdress+urllib.parse.urlencode(parms)
        print('retrieving')
        uh=urllib.request.urlopen(geourl, context=ctx)

        data=uh.read().decode()
        print('retrieved', len(data), 'characters')

        try:
            js=json.loads(data)
        except:
            js=None
        print(js)    

        if not js or 'status' not in js or js['status']!= 'OK':
            print('******FAILURE TO RETRIEVE********')
        else:


            print(json.dumps(js, indent=6))
#print(len(data))
#print(data)
#info=json.loads(data)
#print(info,'*********************')
#print(info["comments"])
