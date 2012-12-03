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
        
        
    def inputEvent(self, event):
        NewState = self._state
        
        # first check the state 
        if self._state == LOCKED:
            #then check the event
            if event == PAYED:
                NewState = UNLOCKED
            if event == PERSONPASSED:
                pass
            if event == TICK:
                pass
            
        # first check the state 
        if self._state == UNLOCKED:
            #then check the event
            if event == PAYED:
                pass
            if event == PERSONPASSED:
                NewState = LOCKED
                pass
            if event == TICK:
                pass            
            
            
        # if the state has changed OnExit and OnEnter must be called
        if self._state != NewState:
            self._OnExit()
            self._state = NewState
            self._OnEnter()
        
        # Do() allways gets called
        self._Do()
    
    # _OnEnter is where things that allways have to be done when entering a state is done
    def _OnEnter(self):
        if self._state==LOCKED:
            pass
        elif self._state==UNLOCKED:
            print(" Opening door")

    # _OnExit is where things that allways have to be done when exiting a state is done
    def _OnExit(self):
        if self._state==LOCKED:
            pass
        elif self._state==UNLOCKED:
            print(" closing door")
            pass
    
    def _Do(self):
        if self._state==LOCKED:
            print(" Door is locked")
        elif self._state==UNLOCKED:
            print(" Door is open")

    
    
if __name__ == "__main__":
    myTurnstile = TurnstileStatemachine()
    
    myTurnstile.inputEvent(PAYED)
    myTurnstile.inputEvent(PERSONPASSED)
    