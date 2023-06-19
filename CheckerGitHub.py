from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import re
from urllib.error import HTTPError
                    #write your .txt here
fileWithlinks=open('Website_Links.txt','r') #Opens a txt file with links
UrlOfLinks=fileWithlinks.readlines() #Every link of in this file will be Line By Line
for item in UrlOfLinks: #Loop for Every link in file
    url = item  
    url = url.replace("\n","") #Replace "\n" with "" in file
    def check_url(url): #function which checks url, his links and status code for every link in file
        req = Request(url) #request url 
        html_page = urlopen(req) #opens a requested file from url

        soup = BeautifulSoup(html_page, "html.parser") #using bs4 for parsing

        links = [] #array for saving url of links
        status = [] #array for saving status codes of links
        print("URL Link's of ", url) 
        for link in soup.findAll('a'): #finding teg 'a' in every elements 
            href = link.get('href') #getting 'href'
            if href is not None:  #Если нет NONE внутри массива ссылок
                if href.startswith("http"):  #if href(link) starts with http, we continue loop
                    try: #try for finding url's with http, their status code and name url
                        response = urlopen(href) 
                        status_code = response.getcode()
                        def out_green(status_code,href):
                            print("\033[32m{}".format(status_code),' ',"\033[32m{}".format(href)) #print a string in green colour
                        out_green(status_code,href)
                    except HTTPError as e: #for catching errors 
                            status_code_error = e.code
                            def out_red(status_code_error,href):
                                print("\033[31m{}".format(status_code_error),' ',"\033[31m{}".format(href)) #print a string in red colour
                            out_red(status_code_error,href) 
                elif href.startswith("/"): #another condition when link starts with "/"
                    href = url + href #our link without http, so we include main "http://" to URI as a string
                    try:
                        response = urlopen(href)
                        status_code = response.getcode()
                        def out_green(status_code,href):
                            print("\033[32m{}".format(status_code),' ',"\033[32m{}".format(href)) #green colour
                        out_green(status_code,href)
                    except HTTPError as e: #for catching errors 
                            status_code_error = e.code


                            def out_red(status_code_error,text):
                                print("\033[31m{}".format(status_code_error),' ',"\033[31m{}".format(text)) #red colour
                            out_red(status_code_error,text)
        
    check_url(url) 
