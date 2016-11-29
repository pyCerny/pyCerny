from BeautifulSoup import BeautifulSoup
import urllib2

#file2 = open('vetyF.txt', 'w+')

try:
    web_page = urllib2.urlopen("http://msekce.karlin.mff.cuni.cz/~rcerny/analyzaIII2016.html")

    soup = BeautifulSoup(web_page)

    string = str(soup)
    string = string.replace(':', ',').replace('Prednaska', ',').replace('<',',').replace('>',',')

    dic = string.split(',')

    for num in range(0, len(dic)):
        s = '(S)'
        t = '(T)'

        if s in dic[num]:
            #file2.write(dic[num] + '\n')
            print(dic[num])+ '\n'
        elif t in dic[num]:
            #file2.write(dic[num] + '\n')
            print(dic[num]) + '\n'

except urllib2.HTTPError:
    print("httperror, i cri evritim :(")

