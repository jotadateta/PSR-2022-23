
class Input:
    def __init__(self,requested,received,duration):
        self.requested = requested
        self.received = received
        self.duration = duration
        
    def __str__(self):
        
        return "requested = " + str(self.requested) +  "received = " + str(self.received) + "duration = " + str(self.duration)
    
    
    def __repr__(self):
        
        return self.__str__() 
    
    