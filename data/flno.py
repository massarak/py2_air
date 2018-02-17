
import sys
import json
import commands
import filename

print "AIRLINE:NH"
print "LANG:EN"


site = raw_input("SITE:")
date = input("DATE:")
flightno = input("NH:")
#jsonfile = 'json/bbb.json'
jsonfile = 'json/' + filename.getFilename()


def callCurl(site, flightno, date, tmpfile='json/bbb.json'):
    myurl = "http://afs.ana.co.jp/fli/api/FlightStatus?airline=NH&site=%s&lang=EN&channel=PC&sn.requestDate=%s&sn.flightNumber=%s&sn.isArrived=D" % (site, date, flightno)
    resp, status = commands.getstatusoutput("curl '%s' > %s" % (myurl, tmpfile))
  

callCurl(site, flightno, date, jsonfile)
f = open(jsonfile, 'r')
jsonData = json.load(f)
print json.dumps(jsonData, sort_keys=True, indent=2)

entry = jsonData['data']['SearchFlightNumber']['data']['fsList']
#print len(entry), entry
for flights in range(len(entry)):
    print "------------------------------------------------"
    #print entry[flights]
    entdic = entry[flights]
    for k in entdic.keys():
        print "%-20s: %s" % (k, entdic[k])


#print jsonData['data']['SearchFlightNumber']['data']['fsList'][0]['depAirportCode']
#print jsonData['data']['SearchFlightNumber']['data']['fsList'][0]['arrAirportCode']
#print jsonData['data']['SearchFlightNumber']['data']['fsList']  #['depAirport']

