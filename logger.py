import json
from alertatron import Alertatron


























class Logger():
    def __init__(self, api_key, system, filePath, current_time, admin_mode=True):
        self.api_key = api_key
        self.system = system
        self.admin_mode = admin_mode
        self.filePath = filePath
        self.rateLimit = 30
        self.current_time = current_time

        self.users = []

        with open(filePath) as json_file:
            self.tradingGroupsJson = json.load(json_file)
        
        if system not in self.tradingGroupsJson:
            raise Exception("System NOT IN Trading Groups.")
        

        self.alertatron = Alertatron(self.api_key)

        

    

    def getUsers(self):
        self.users = {}



        currentCap = ""
        currentGroupID = ""
        currentUsers = []

        for eachTradingGroup in self.tradingGroupsJson[self.system]:
            currentCap = eachTradingGroup
            currentGroupID = self.tradingGroupsJson[self.system][currentCap]

            if self.system not in self.users:
                self.users[self.system] = {}
            
            if currentCap not in self.users[self.system]:
                self.users[self.system][currentCap] = {"ID": currentGroupID, "Users": []}
            

            self.alertatron.get_clients(currentGroupID)
            

            
            

            





    