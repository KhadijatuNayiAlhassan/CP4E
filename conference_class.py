class Conference:
    def __init__(self,name,company,state,email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    
    def getCompany(self):
        return self.company
    def setCompany(self,company):
        self.company = company
    
    def getState(self):
        return self.state
    def setState(self,state):
        self.state = state
    
    def getEmail(self):
        return self.email
    def setEmail(self,email):
        self.email = email
    
    def get_details():
        name = input("please enter your name: ")
        company = input("please enter the name of your company: ")
        state = input("please enter the state you come from: ")
        email = input("please enter your email address: ")
        details = name +"," +company+","+state+","+email
        return details
    get_details()
    file = open("conference_text.txt","w")
    file.write(self.details) 
    
    