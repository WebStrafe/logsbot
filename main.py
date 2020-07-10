import os
from os import path
from logger import *
from datetime import datetime
from dateutil import relativedelta
import time

dir_path = os.path.dirname(os.path.realpath(__file__))





def main():
    apiKey = "itH9WsnTTb494PyZHnccR57zDiKYywO5blq0C8KiFwtjeMPLCjiBOQRZctRS"
    jsonFilePath = f"{dir_path}/data.json"

    currentTime = datetime.utcnow()

    currentTime = currentTime - relativedelta.relativedelta(minute=5)

    currentTimeString = currentTime.strftime("%Y-%m-%dT%H:%M:%S")



    logger = Logger(apiKey, "A", jsonFilePath, currentTimeString)
    for _ in range(0, 65):
        time.sleep(0.55)
        logger.getUsers()



    pass
    # getUsers = UserRetriever("itH9WsnTTb494PyZHnccR57zDiKYywO5blq0C8KiFwtjeMPLCjiBOQRZctRS")
    # # getUsers.get_trading_groups()
    # # getUsers.get_clients("1829a6c1-ed4d-4102-b9bc-e315fa55e2dc")
    # getUsers.get_entries_test("cd00f4f8-a855-4758-818b-8abbb4a29da1", "2020-07-09T14:20:00")









if __name__ == "__main__":
    main()