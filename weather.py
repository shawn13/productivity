# -*- coding: UTF-8 -*-
import urllib2
import re

provice=raw_input('input you provice: ')
city=raw_input("input city: ")
url = "http://qq.ip138.com/weather/"+provice+"/"+city+".htm"
#url = "http://qq.ip138.com/weather/anhui/HuoShan.htm"

class Weather():
        def __init__(self):
                pass

        def getHtml(self, url):
                req = urllib2.Request(url)
                res = urllib2.urlopen(req)
                html = res.read()
                res.close()
                return html

        def getWeather(self, html):
                patterndate = re.compile(">(\d{4}-\d{1,2}-\d{1,2} .+)<")
                date = patterndate.findall(html)

                patternweather = re.compile("(.+)")
                weather = patternweather.findall(html)

                patterntemperature = re.compile("([-]?\d{1,2}.+)")
                temperature = patterntemperature.findall(html)

                if len(date) == 0:
                        print "Cannot get city's weather you input"
                        return
                for i in range(len(date)):
                        print "%s" % date[i], "\t%s" % weather[i], "\t%s" % temperature[i]

if __name__ == "__main__":
        weather = Weather()
        weather.getWeather(weather.getHtml(url))