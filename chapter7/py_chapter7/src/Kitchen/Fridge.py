class Fridge:
    """This class implements a fridge where ingredients can be
    added and removed individually, or in groups.  
    The fridge will retain a count of every ingredient added or removed,
    and will raise an error if a sufficient quantity of an ingredient 
    isn't present.
    Methods:
    has(food_name [, quantity]) - checks if the string food_name is in the fridge.  Quantity will be set to 1 if you don't specify a number.
    has_various(foods) - checks if enough of every food in the dictionary is in the fridge
    add_one(food_name) - adds a single food_name to the fridge
    add_many(food_dict) - adds a whole dictionary filled with food
    get_one(food_name) - takes out a single food_name from the fridge
    get_many(food_dict) - takes out a whole dictionary worth of food.
    get_ingredients(food) - If passed an object that has the __ingredients__ 
            method, get_many will invoke this to get the list of ingredients.
    """
    
    def __init__(self, items={}):
        """Optionally pass in an initial dictionary of items"""
        if type(items) != type({}):
            raise TypeError("Fridge requires a dictionary but was given %s" % type(items))
        self.items = items
        return


    def __add_multi(self, food_name, quantity):
        """
        __add_multi(food_name, quantity) - adds more than one of a 
        food item. Returns the number of items added
        
        This should only be used internally, after the type checking has been
        done
        """
        if (not food_name in self.items):
            self.items[food_name] = 0
            
        self.items[food_name] = self.items[food_name] + quantity

      def add_one(self, food_name):
        """
        add_one(food_name) - adds a single food_name to the fridge
        returns True
        Raises a TypeError if food_name is not a string.
        """
        if type(food_name) != type(""):
            raise TypeError, "add_one requires a string, given a %s" % type(food_name)
        else:
            self.__add_multi(food_name, 1)
        
        return True
        
    def add_many(self, food_dict):
        """
        add_many(food_dict) - adds a whole dictionary filled with food as keys and
            quantities as values.
        returns a dictionary with the removed food.
        raises a TypeError if food_dict is not a dictionary
        returns False if there is not enough food in the fridge.
        """
        
        if type(food_dict) != type({}):
            raise TypeError("add_many requires a dictionary, got a %s" % food_dict)
        
        for item in food_dict.keys():
            self.__add_multi(item, food_dict[item])
        return


   def has(self, food_name, quantity=1):
        """
        has(food_name, [quantity]) - checks if the string food_name is in the fridge.  Quantity defaults to 1
        Returns True if there is enough, False otherwise.
        """
        
        return self.has_various({food_name:quantity})
        
    def has_various(self, foods):
        """
        has_various(foods) determines if the dictionary food_name
            has enough of every element to satisfy a request.
        returns True if there's enough, False if there's not or if an element does
        not exist.
        """
        
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        except KeyError:
            return False

def __get_multi(self, food_name, quantity):
        """
        _get_multi(food_name, quantity) - removes more than one of a 
        food item. Returns the number of items removed
        returns False if there isn't enough food_name in the fridge.
        This should only be used internally, after the type checking has been
        done
        """
        
        try:
            if (self.items[food_name] is None):
                return False;
            
            if (quantity > self.items[food_name]):
                return False;
            self.items[food_name] = self.items[food_name] - quantity
        except KeyError:
            return False
        return quantity


    def get_one(self, food_name):
        """
        get_one(food_name) - takes out a single food_name from the fridge
        returns a dictionary with the food:1 as a result, or False if there wasn't
        enough in the fridge.
        """

        if type(food_name) != type(""):
            raise TypeError("get_one requires a string, given a %s" % type(food_name))
        else:
            result = self.__get_multi(food_name, 1)
        return result

    def get_many(self, food_dict):
        """
        get_many(food_dict) - takes out a whole dictionary worth of food.
        returns a dictionary with all of the ingredients
        returns False if there are not enough ingredients or if a dictionary 
        isn't provided.
        """
        
        if self.has_various(food_dict):
            foods_removed = {}
            for item in food_dict.keys():
                foods_removed[item] = self.__get_multi(item, food_dict[item])
            return foods_removed
        
    def get_ingredients(self, food):
        """
        get_ingredients(food) - If passed an object that has the __ingredients__ 
            method, get_many will invoke this to get the list of ingredients.
        """
        try:
            ingredients = self.get_many(food.__ingredients__())
        except AttributeError:
            return False
        
        if ingredients != False:
            return ingredients
