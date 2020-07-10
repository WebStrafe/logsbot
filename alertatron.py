import requests
import time



class User():
    def __init__(self, id, name, contact, validKeys, isActive, isOnGracePeriod, canTrade, subscriptionExpiresAt):
        self.id = id
        self.name = name
        self.contact = contact
        self.validKeys = validKeys
        self.isActive = isActive
        self.isOnGracePeriod = isOnGracePeriod
        self.canTrade = canTrade
        self.subscriptionExpiresAt = subscriptionExpiresAt










class Alertatron():
    def __init__(self, api_key):
        self.api_key = api_key

        self.url = "https://alertatron.com/pa"

        self.headers = {
            "authorization": f"Bearer {self.api_key}",
            "accept": "application/json",
            "content-type": "application/json"
        }
    


    def check_limit(self, response, responseURL):
        self.currentLimit = int(response.headers["X-RateLimit-Remaining"])

        if self.currentLimit == 0 and "Retry-After" in response.headers:

            print(f"Retrying in {response.headers['Retry-After']} Seconds.\n")
            time.sleep(int(response.headers["Retry-After"]) + 1)

            response = requests.get(responseURL, headers=self.headers)
            self.currentLimit = int(response.headers['X-RateLimit-Remaining'])

            print(response.headers)

            return response
        else:
            print(response.headers)
            return response

    



    def get_clients(self, trading_group_id):  

        data = f"trading_group_id={trading_group_id}"


        # if self.currentLimit == 0:
        #     print("sleeping")
        #     time.sleep(32)

        responseURL = f'{self.url}/clients?{data}'

        firstResponse = requests.get(responseURL, headers=self.headers)

        response = self.check_limit(firstResponse, responseURL)

        # if self.currentLimit == 0 and "Retry-After" in response.headers:

        #     print(f"Retrying in {response.headers['Retry-After']} Seconds.\n")
        #     time.sleep(int(response.headers["Retry-After"]) + 1)

        #     response = requests.get(f'{self.url}/clients?{data}', headers=self.headers)
        #     self.currentLimit = int(response.headers["X-RateLimit-Remaining"])
        
        print(self.currentLimit)

        # self.currentLimit = response.headers["X-RateLimit-Remaining"]
