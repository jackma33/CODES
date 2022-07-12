from pymongo import MongoClient

# print(db['users'].insert_one({'user': 'Anon'}))


class BotDataBase():
    def __init__(self):
        dbString = "mongodb+srv://naabo:qJidZsUX45ExMmGn@cluster0.o17vh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        mongo = MongoClient(dbString)
        db = mongo['naaboBot']

        self.blacklist = db['blacklist']
        self.whitelist = db['whitelist']
        self.warnedusers = db['warnedUsers']

    def addWanrnedUser(self, id):
        user = self.warnedusers.find_one({'userId': id})
        if user == None:
            self.warnedusers.insert_one({'userId': id, 'warnings': 0})
            return 0
        else:
            if user['warnings'] == 5:
                self.blacklist.insert_one({'userId': id})
                return -1

            self.warnedusers.update_one(
                {'userId': id}, {'$inc': {'warnings': 1}})
            return user['warnings'] + 1

    def removeWarnedUser(self, id):
        user = self.blacklist.find_one({'userId': id})
        if user != None:
            self.blacklist.delete_one({'userId': id})

        self.warnedusers.delete_one({'userId': id})

    def addToBlackList(self, id):
        user = self.blacklist.find_one({'userId': id})
        if user != None:
            return "User already Blocked"
        self.blacklist.insert_one({'userId': id})
        return "User Blocked"

    def removeFromBlacklist(self, id):
        user = self.blacklist.find_one({'userId': id})
        if user == None:
            return "This User is not in Blacklist"

        self.blacklist.delete_one({'userId': id})
        return "User Unblocked"

    def checkIfBlackListed(self, id):
        user = self.blacklist.find_one({'userId': id})
        if user == None:
            return False
        else:
            return True

    def addToWhiteList(self, id):
        user = self.warnedusers.find_one({'userId': id})

        if self.checkIfBlackListed(id) == True:
            self.removeFromBlacklist(id)

        if user != None:
            self.warnedusers.delete_one({'userId': id})

        if self.warnedusers.find_one({'userId': id}) != None:
            self.warnedusers.delete_one({'userId': id})

        self.whitelist.insert_one({'userId': id})
        return True

    def deleteFromWhitelist(self, id):
        user = self.whitelist.find_one({'userId': id})
        if user == None:
            return False

        self.whitelist.delete_one({'userId': id})
        return True

    def checkIfWhiteListed(self, id):
        user = self.whitelist.find_one({'userId': id})
        if user == None:
            return False
        else:
            return True
