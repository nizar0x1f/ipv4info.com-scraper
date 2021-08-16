import requests,itertools
from bs4 import BeautifulSoup
import urllib3
import time
import logging,csv
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # to disable annying tls errors

isExist = os.path.exists("output")
if not isExist: 
  os.makedirs("output")



header = '''
 _              ___ _        __                          
(_)            /   (_)      / _|                           
 _ _ ____   __/ /| |_ _ __ | |_ ___   ___ ___  _ __ ___     
| | '_ \ \ / / /_| | | '_ \|  _/ _ \ / __/ _ \| '_ ` _ \ 
| | |_) \ V /\___  | | | | | || (_) | (_| (_) | | | | | |
|_| .__/ \_/     |_/_|_| |_|_| \___(_)___\___/|_| |_| |_|
  | |  scraper    by @nizar0x1f                                       
  |_|                                                                                                           
'''


def get_pages(start):
    data = []
    urls = []
    v = 0
    next_val = ""
    for i, _ in enumerate(iter(bool, True)):
        v = v + 1
        print(v)
        if v == 1:
            r = requests.get(start)
            soup = BeautifulSoup(r.content, 'html5lib') 
            next = soup.find('a', text = 'Next page')
            table = soup.find("table",attrs = {'class':'TB2'})
            count = 0
            
            for row in table.findAll("tr"):
                count = count + 1
                if count > 3:
                    cols = row.findAll("td")
                    cols = [ele.text.strip() for ele in cols]
                    data.append([ele for ele in cols if ele])

            for val in data:
                pass
                print(val)
            try:
                next_val = next['href']
                url = "http://ipv4info.com" + next_val
                print(next_val)
            except:
                break
            
        elif v < 99999:
            try:
                print(url)
                r = requests.get(url)
                soup = BeautifulSoup(r.text, 'html5lib') 
                next = soup.find('a', text = 'Next page')
                next = next['href']
                table = soup.find("table",attrs = {'class':'TB2'})
                count = 0
                for row in table.findAll("tr"):
                    count = count + 1
                    if count > 3:
                        cols = row.findAll("td")
                        cols = [ele.text.strip() for ele in cols]
                        data.append([ele for ele in cols if ele])

                for val in data:
                    pass
                    print(val)
                url = "http://ipv4info.com" + next
                urls.append(next_val)
                print(next_val)
            except:
                break
    
    return data
    


def main():
    data = get_pages(input("Enter starting url : "))
    cn = 0
    
    for el in data:   # to clean the list  
        cn =+ 1
        for e in el:
            errs=["Previous page","window.adsbygoogle",".push({});","Next page","adsbygoogle"]
            if any(err in e for err in errs):
                data.pop(cn)
    with open("output/" + input("\n Where do you want to save the output :\t"),"a") as out:
        write = csv.writer(out)
        write.writerows(data)

    print("Done")

if __name__ == "__main__":
    print(header)
    main()
    



    
    
    
