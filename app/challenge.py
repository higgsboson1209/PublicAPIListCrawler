#importing all the necessary libraries
import urllib
import time
from firebase import firebase
import requests

#opening a firebase connection
firebase = firebase.FirebaseApplication("https://postman-api-4245b-default-rtdb.firebaseio.com/",None)

#Class with functions to use OOPS Concepts and get data neatly for future references
class Get_Data:

    #Defines the basic urls which can be modified later
    def __init__(self):
        self.base_url="https://public-apis-api.herokuapp.com/api/v1"
        self.auth_url=self.base_url+"/auth/token"
        self.category_url=self.base_url+'/apis/categories?page='
        self.data_url=self.base_url+'/apis/entry?'

    #Defines Function to generate an auth token
    def Get_Auth_Token(self):
        token=requests.get(self.auth_url)
        token =token.json()
        auth_token=token['token']
        headers = {'Authorization': 'Bearer '+ str(auth_token)}
        return headers


    #Defines Function to get categories of API
    def Get_Api_Categories(self,page_number,headers):
        page_number=str(page_number)
        cat_url=self.category_url+page_number
        category_request=requests.get(cat_url,headers=headers)
        return category_request

    #Define Function to get API's of further Categories
    def Get_Api_Data(self,parameters,headers):
        dat_url=self.data_url+str(urllib.parse.urlencode(parameters))
        data_requests=requests.get(dat_url,headers=headers)
        return data_requests

def main():
    Data_requests=Get_Data()
    #A variable that is used to come over rate limiting
    Number_Of_Requests=0

    #Used to handle paginated data for categories
    max_calls=2*10**6
    for i in range(1,max_calls):

        headers=Data_requests.Get_Auth_Token()
        Number_Of_Requests+=1
        request2 = Data_requests.Get_Api_Categories(i,headers)
        list_of_categories=request2.json()
        Number_Of_Requests+=1
        #We break out of the loop once we have gone through all the categories
        if (i-1)*10+len(list_of_categories['categories'])>list_of_categories['count']:
            break
        if not 'categories' in list_of_categories:
            continue
        if len(list_of_categories['categories'])==0:
            continue
        for category in (list_of_categories['categories']):
            #Used to handle paginated data for each API Category
            for j in range(1,2*10**6):
                parameters={'page':j,'category':category}
                #Stop the code for one minute once 10 requests have been made to the server to overcome rate limitation
                #Can be modified later to make it more efficient
                if Number_Of_Requests==9:
                    time.sleep(60)
                    headers=Data_requests.Get_Auth_Token()
                    Number_Of_Requests=1

                request3=Data_requests.Get_Api_Data(parameters,headers)

                Number_Of_Requests+=1

                request3=request3.json()
                print("------------------------------------------------------")
                print(request3)
                print("------------------------------------------------------")
                if 'count' not in request3:
                    break
                if request3['count']==0:
                    break
                #We break out of this loop once all API's of a category have been added to our database
                if (j-1)*10 + len(request3['categories'])>request3['count']:
                    break
                #Going through the api data one by one and pushing them as rows to my firebase
                for api in request3['categories']:
                    firebase.post("/API-DATA",api)


if __name__=="__main__":
    main()

