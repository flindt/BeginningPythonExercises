'''
Created on Jan 25, 2012

@author: pfl
'''
 #  Define states 
( LOCKED, UNLOCKED ) = (0, 1)
# Define events
( PAYED, PERSONPASSED, TICK) = (0,1,2)

class TurnstileStatemachine(object):
    '''
    simple example of how to implement a statemachine in python
    '''

    def __init__(self):
        '''
        Initialise state
        '''
        self._state = LOCKED
        
        
    def input(self, event):
        
        self._Do()
        pass
    
    
    def _OnEnter(self):
        pass
    
    def _OnExit(self):
        pass
    
    def _Do(self):
        if self._state==LOCKED:
            print(" Door is locked")
        elif self._state==UNLOCKED:
            print(" Door is open")

    
    
if __name__ == "__main__":
    myTurnstile = TurnstileStatemachine()
    
    myTurnstile.input(PAYED)
    myTurnstile.input(PERSONPASSED)
    