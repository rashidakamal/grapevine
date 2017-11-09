import requests
from bs4 import BeautifulSoup
import config 

def get_body(article_url):
    
    api_key = config.nyt_key
    cookie = """_gab=GA1.2.2139500475.1419980777; mlUserID=55qJygdnHyim; MSFPC=ID=9e34584aaa774f7da03707f6d4d8f56f&CS=0&LV=201506; __gads=ID=050d3ea2e1a867ce:T=1434982065:S=ALNI_MZVCbevGTdKQFSD0wqV94cWIKnvNA; _sp_id.e092=91596143d1534b7f.1454391543.1.1454391753.1454391543; _cb_ls=1; WT_FPC=id=e14d0f2e-87e3-4db2-bed5-2483e108525f:lv=1456872893416:ss=1456872262823; _sp_id.ddc6=0475f58468b404a5.1436504343.213.1460074051.1459978985; pickleAdsCampaigns=[{"c":"1010","e":1462760898566,"v":1}]; afp_storedCookies=1279^cookie_afp_1279~1; ga_INT=GA1.2.1814193231.1420224626; _ga=GA1.2.1814193231.1420224626; __CT_Data=gpv=26&apv_202_www06=4&apv_330_www06=4&apv_342_www06=1&apv_343_www06=9&apv_377_www06=4; WRUID=0; HTML_ViewerId=5dd33cb7-3a72-59b0-b9b4-1c0454cf12a7; optimizelySegments=%7B%223007620980%22%3A%22search%22%2C%223013750536%22%3A%22false%22%2C%223028090192%22%3A%22gc%22%2C%223032570147%22%3A%22none%22%2C%223155680847%22%3A%22search%22%2C%223168910512%22%3A%22gc%22%2C%223181390897%22%3A%22false%22%2C%223190590338%22%3A%22none%22%2C%223315571554%22%3A%22search%22%2C%223321851195%22%3A%22false%22%2C%223334171090%22%3A%22pockethits%22%2C%223336921036%22%3A%22gc%22%2C%226333011659%22%3A%22true%22%7D; optimizelyBuckets=%7B%227854220743%22%3A%227839592187%22%2C%225355901213%22%3A%225361970061%22%7D; propensityEDU=Columbia; isEDU=true; OX_plg=swf|shk|pm; NYT_W2=New%20YorkNYUS|ChicagoILUS|London--UK|Los%20AngelesCAUS|San%20FranciscoCAUS|Tokyo--JP; nyt-d=101.000000000NAI00000s9Iny1/7GKH074oKi0a6miq0cAted0rCJSY1yT6Ca0f3nOM0NUY4r0F2cCa0f5WH/0zB0aL1w8JK20AOm0R0B4mTb0I9Ier0sFNe5074HOL1yD2ek0fDte5071XOR1y0cC00R2nG607201b1mT6bo1tONbz1Z01iR0C56Lo1zRmfy1ZGKHO@91192f88/2930c7b1; NYT-BCET=1486886360%7CVL7cQNC2Jbey694TE9OcIUt06Ko%3D%7CY%3BA%7CJ%2Bqpg5GVrA59%2BjIKKQylAVZGHJfddKB0VqiMjuAPNYY%3D; RMID=007f010063f2589fc17b00b1; __utmt=1; __utma=69104142.1814193231.1420224626.1485542687.1487191802.91; __utmb=69104142.1.10.1487191802; __utmc=69104142; __utmz=69104142.1485542687.90.55.utmcsr=nytimes.com|utmccn=(referral)|utmcmd=referral|utmcct=/; Kruxset=true; Kruxadx=qxk0hzyjh,pox3vefah; _gat_r2d2=1; mnet_session_depth=1%7C1487191806344; _cb=COYjR8Bcin9-CAqYKK; _chartbeat2=.1419780323834.1487191806804.0000000000010001.BZWBJpDZUfysCK0gGCze6U8CJtKW8; _cb_svref=null; _chartbeat4=t=YQxlsCAGAyvCuTmToB390AcB3AGjb&E=1&EE=1&x=0&c=0.45&y=7101&w=273; adxcl=l*416c4=6013964f:1|l*427aa=6013964f:1|l*44378=6013964f:1|t*45193=5e69c1cf:1455137670|l*3e8ac=6013964f:1|l*455af=6013964f:1|l*45033=6013964f:1|t*45271=6013964f:1458240385|l*45193=5e69c1cf:1; adxcs=s*44768=0:1; NYT-S=2UCzxVt7en6R/GInGg7WfslK21nN49ftAKyGDhk8iLFHPAcVtr40Hlq8fKcsu2C/Boy/ASfZxnNq9XRWCP0GoZZAl8iqcuoId0tWxMC2OaVr61Jxk/oZQOeN5c9XzW4ksDLrKt3RbswuUT/CHhTki.pquvbXoP.xJPi..w7rrwMcP7w7ZoeyPbdRc9wxaZbuwOEeNjq31NCTdQfrpp4LtEaFCo1nfA15lO1q9erKFJVLaoRuYWHBFz2000; nyt-m=0988128B4DFE7518B08616C914A721FE&e=i.1488326400&t=i.10&v=i.0&l=l.15.-1.-1.-1.-1.-1.-1.-1.-1.-1.-1.-1.-1.-1.-1.-1&n=i.2&g=i.0&rc=i.0&er=i.1484780775&vr=l.4.4.0.11.36&pr=l.4.6.0.11.36&vp=i.47&gf=l.10.-1.-1.-1.-1.-1.-1.-1.-1.-1.-1&ft=i.0&fv=i.0&gl=l.2.3583832805.4017480927&rl=l.1.-1&cav=i.2&imu=i.1&igu=i.1&prt=i.5&kid=i.1&ica=i.0&iue=i.1&ier=i.0&iub=i.0&ifv=i.0&igd=i.0&iga=i.0&imv=i.0&igf=i.0&iru=i.0&ird=i.0&ira=i.0&iir=i.1&abn=s.close_door_90_10_jun2016&abv=i.1&gb=l.3.0.3.1487203200; optimizelyEndUserId=oeu1436504342189r0.44754519080743194; walley=GA1.2.1814193231.1420224626; _sp_id.75b0=bb4c6516d4b7c65c.1461852869.151.1487191847.1485207214; _sp_ses.75b0=*; nyt-a=c11b7d83aae834933d9dff870b40fe93"""
    
    art_body = []

    head_data = { "Cookie": cookie,
                 "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",

                 "From":"rsk2161@columbia.edu"}

    response = requests.get(article_url,headers=head_data)    
    data = response.text

    soup = BeautifulSoup(data, 'html.parser')
    
    for item in soup.find_all("p", {"class":"story-content"}):
        art_body.append(item.text)
        
    if not art_body:
        
        for item in soup.find_all("p", {"class":"story-body-text"}):
            art_body.append(item.text)
            
    if not art_body:
        
        for item in soup.find_all("p", {"itemprop":"articleBody"}):
            art_body.append(item.text)
        
    return art_body