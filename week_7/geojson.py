import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue
    
    # print json.dumps(js, indent=4)

    results = js['results'][0]
    
    # print json.dumps(results['address_components'], indent=4)
    
    for u in results['address_components']:
        if u['types'][0] == 'country' :
            country_code = u['short_name']
            
    if 'country_code' in locals():
        print "Country code for \'" + str(address) + "\' is " + str(country_code)
        del country_code
    else:
        print 'Country code does not exist for ' + str(address)
        
    
        

