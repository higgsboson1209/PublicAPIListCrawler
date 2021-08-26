from app import app
import urllib
import time
import math
from app import firebase
from app import requests
@app.route('/')
@app.route('/index',methods=['GET'])
# @app.route('/submit',methods=['GET','POST'])
# def submit():
    # new_data={"name":"Saksham"}
    # 
    # return "Thank You"
def index():

    count=0
    for i in range(1,2*10**6):
        token = requests.get("https://public-apis-api.herokuapp.com/api/v1/auth/token")

        token =token.json()

        auth_token=(token['token'])

        headers = {
        'Authorization': 'Bearer '+ str(auth_token)
        }
        request2 = requests.get('https://public-apis-api.herokuapp.com/api/v1/apis/categories?page='+str(i),headers=headers)
        x=request2.json()
        count+=1
        if (i-1)*10+len(x['categories'])>x['count']:
            break
        if not 'categories' in x:
            continue
        if len(x['categories'])==0:
            continue
        for cat in (x['categories']):
            for j in range(1,2*10**6):
                parameters={'page':j,'category':cat}
                url=f'https://public-apis-api.herokuapp.com/api/v1/apis/entry?{urllib.parse.urlencode(parameters)}'
                print(url)
                if count==9:
                    time.sleep(60)
                    count=0

                request3=requests.get(url,headers=headers)
                
                count+=1

                request3=request3.json()
                if request3['count']==0:
                    break
                if (j-1)*10 + len(request3['categories'])>request3['count']:
                    break
                

                for item in request3['categories']:
                    print(item)
                    firebase.post("/something",item)

    return "Thanksear"


