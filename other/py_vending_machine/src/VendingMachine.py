
# Fields defining events
( COIN_1, COIN_2, COIN_5, COIN_10, COIN_20, PRODUCTSELECT, TICK_10SEC, CANCELBUTTON) = (0,1,2,3,4,5,6,7)

# Fields defining states
( IDLE, SALE) = (0,1)

#Field defining products
( COLA, FANTA) = (0,1)



class VendingSM(object):
    '''
    This class implements a statemachine for controlling a Vending Machine
    '''
    
    def __init__(self):
        self._state = IDLE
        self._credit = 0
        self._Do()

    
    def _PrintCredit(self):
        if self._credit == 0:
            print("Please insert coins.")
        else:
            print("You have put in %i DKK"%self._credit)
    
    
    def inputEvent(self, event, options=None):
        NewState = self._state
        
        if self._state == IDLE:
            if event == COIN_1:
                self._credit += 1
            if event == COIN_2:
                self._credit += 2
            if event == COIN_5:
                self._credit += 5
            if event == COIN_10:
                self._credit += 10
            if event == COIN_20:
                self._credit += 20
            
            if event == PRODUCTSELECT:
                NewState = SALE
        
        if self._state == SALE:
            pass
        
        if NewState != self._state:
            self._state = NewState    
        
        self._Do()

    def _Do(self):
        if self._state == IDLE:
            print( "Temperature of our drinks 11C")
            self._PrintCredit()
    
    def getCredit(self):
        return self._credit
        pass

    
    def getState(self):
        return self._state
    
    
    
    
    
    
        
        
        


