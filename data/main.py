import sys
import json
import commands
import filename

def main():

    def baseurl(site):
        """ returns base url; site = DOM or INT
        """
        str_url     = "http://afs.ana.co.jp/fli/api/FlightStatus?airline=NH&"
        str_site    = "site=%s&" % (site)
        str_lang    = "lang=EN&"
        str_channel = "channel=PC&"
        base_str = str_url + str_site + str_lang + str_channel
        return base_str
    
    
    def callCurl_sn(site, date, flightno, tmpfile='json/bbb.json'):
        """
        >>> callCurl_f('DOM', '20180128', '38')
        """
        str_sndate = "sn.requestDate=%s&sn.flightNumber=%s&sn.isArrived=D" % (date, flightno)    
        myurl = baseurl(site) + str_sndate
        resp, status = commands.getstatusoutput("curl '%s' > %s" % (myurl, tmpfile))
    
    def callCurl_sa(site, date, dep, arr, tmpfile='json/ccc.json'):
        """
        >>> callCurl_d('DOM', '20180128', 'HND', 'IWJ')
        """
        str_sadate = "sa.requestDate=%s&sa.depAirportSelect=%s&sa.arrAirportSelect=%s&sa.isArrived=D" % (date, dep, arr)
        myurl = baseurl(site) + str_sadate
        resp, status = commands.getstatusoutput("curl '%s' > %s" % (myurl, tmpfile))
    
    
    
    def Flno():
        print "AIRLINE: NH"
        print "LANG: EN"
        site = raw_input("SITE: ")
        date = input("DATE: ")
        
        flightno = input("NH: ")
        jsonfile = 'json/' + filename.getFilename()
        
        callCurl_sn(site, date, flightno, jsonfile)
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
        
    
    def DepArr():
        print 'AIRLINE: NH'
        print 'LAMG: EN'
        site = raw_input("SITE: ") 
        date = input("DATE: ")
        
        dep = raw_input("DEP: ")
        arr = raw_input("ARR: ")
        jsonfile = 'json/' + filename.getFilename()
        
        callCurl_sa(site, date, dep, arr, jsonfile)
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
    
    
    
    
    print "FLNO:1 DEP ARR:2"
    sentaku = input()

    if sentaku == 1:
        Flno()
    if sentaku == 2:
        DepArr()
    else: 
        print("quit") 
    
