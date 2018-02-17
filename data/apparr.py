
import sys
import json
import commands
import filename

print 'AIRLINE:NH'
print 'LAMG:EN'


site = raw_input("SITE:") 
date = input("DATE:")
dep = raw_input("DEP:")
arr = raw_input("ARR:")
#jsonfile = 'json/ccc.json'
jsonfile = 'json/' + filename.getFilename()


def callCurl(dep, arr, date, tmpfile='json/ccc.json'):
  myurl = "http://afs.ana.co.jp/fli/api/FlightStatus?airline=NH&site=DOM&lang=EN&channel=PC&sa.requestDate=%s&sa.depAirportSelect=%s&sa.arrAirportSelect=%s&sa.isArrived=D" % (date, dep, arr)
  resp, status = commands.getstatusoutput("curl '%s' > %s" % (myurl, tmpfile))
  

callCurl(dep, arr, date, jsonfile)
f = open(jsonfile, 'r')
#f = open('json/20180128_202216.json', 'r')
jsonData = json.load(f)
print json.dumps(jsonData, sort_keys=True, indent=2)

entry = jsonData['data']['SearchAirport']['data']['fsList']
#print len(entry), entry
for flights in range(len(entry)):
    print "------------------------------------------------"
    #print entry[flights]
    entdic = entry[flights]
    for k in entdic.keys():
        print "%-20s: %s" % (k, entdic[k])

#print jsonData['data']['SearchAirport']['data']['fsList'][0]['depAirportCode']
#print jsonData['data']['SearchFlightNumber']['data']['fsList'][0]['arrAirportCode']
#print jsonData['data']['SearchFlightNumber']['data']['fsList']  #['depAirport']

