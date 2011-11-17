'''
Created on Nov 17, 2011

@author: pfl
'''


class Omelet:
    """ This class will create an Omelet
    """
    def __init__(self, kind = "cheese"):
        """ __init__(self, kind="cheese" )
        This initializes an Omelet. Default type is cheese
        """
        self.set_kind(kind)
        return
    
    def set_kind(self, kind):
        possible_ingredients = self.__known_kinds(kind)
        if possible_ingredients == False:
            return False
        else:
            self.kind = kind
            self.neede_ingredients = possible_ingredients

    def __known_kinds(self, kind):
        if kind == "cheese":
            return {"eggs":2, "milk":1, "cheese":1}
        else:
            return False

if __name__ == '__main__':
    Omelet()
    pass