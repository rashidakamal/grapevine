import requests
from bs4 import BeautifulSoup
import math
import time
import NYTPage
import config 

global errors
errors = []

def get_data(phrase, datastore=[], startyear=2016, endyear=2016):
    
    key = config.nyt_key
    source = "The%20New%20York%20Times"
    
    # months = list(range(1, 13))
    start_month = "0101"
#     end_month = "0630"
    end_month = "0131"
    
    api_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=%22"+ str(phrase) + "%22" +"&api-key=" + key + "&fq=source:('" + source + "')" + "&begin_date=" + str(startyear) + str(start_month) + "&end_date=" + str(endyear) + str(end_month)


    response_prime = requests.get(api_url)    
    data_prime = response_prime.json()

    
    results_count = data_prime['response']['meta']['hits']
    print("**number of results: ", results_count)
    pages = (math.ceil(results_count / 10))
    
    time.sleep(0.3) 
    
    print("need to scrape", pages, "pages")
    print("__"*10)

    # for p in range(0,pages):     
    for p in range(0,3):    

        api_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=%22"+ str(phrase) + "%22&api-key=" + key + "&fq=source:('" + source + "')" + "&begin_date=" + str(startyear) + str(start_month) + "&end_date=" + str(endyear) + str(end_month) + "&page=" + str(p)

        content = requests.get(api_url)
        print(content.status_code)
        
        # Handle 403 bug and other errors 
        if content.status_code != 200:
            print("failed on:", api_url)
            
            api_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=%22"+ str(phrase) + "%22&fl=web_url" + "&api-key=" + key + "&fq=source:('" + source + "')" + "&begin_date=" + str(startyear) + str(start_month) + "&end_date=" + str(endyear) + str(end_month) + "&page=" + str(p)
            content = requests.get(api_url)
            data = content.json()
            
        else:
            
            data = content.json()

        if data.get("response"):

            print("NUMBER OF DOCS:", len(data["response"]["docs"]))

            for d in data["response"]["docs"]:
                
                d["body"] = NYTPage.get_body(d['web_url'])
                datastore.append(d)
                print("added data point from page: ", p)
                time.sleep(0.1)


            print("scraped page", p)
            print("__"*20)

        else:
            
            errors.append(p)
            print("Didn't see response for page: ", p)
            print("__"*20)

        del data
            
        time.sleep(0.5)
        
    return datastore, errors




