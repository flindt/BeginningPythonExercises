
class Recipe:
    """
    This class houses recipes for use by the Omelette class
    """
    
    def __init__(self):
        self.set_default_recipes()
        return
    
    def set_default_recipes(self):
        self.recipes = {"cheese" : {"eggs":2, "milk":1, "cheese":1},
                        "mushroom" : {"eggs":2, "milk":1, "cheese":1, "mushroom":2},
                        "onion" : {"eggs":2, "milk":1, "cheese":1, "onion":1}}
    
    def get(self, name):
        """
        get(name) - returns a dictionary that contains the ingredients needed to
        make the omelette in name.
        When name isn't known, returns False
        """
        try:
            recipe = self.recipes[name]
            return recipe
        except KeyError:
            return False
    
    def create(self, name, ingredients):
        """
        create(name, ingredients) - adds the omelette named "name" with the ingredients
        "ingredients" which is a dictionary.
        """
        
        self.recipes[name] = ingredients
    
if __name__ == '__main__':
    r = Recipe()
    if r.recipes != {"cheese" : {"eggs":2, "milk":1, "cheese":1}, 
                        "mushroom" : {"eggs":2, "milk":1, "cheese":1, "mushroom":2}, 
                        "onion" : {"eggs":2, "milk":1, "cheese":1, "onion":1}}:
        print("Failed: the default recipes is not the correct list")
    cheese_omelette = r.get("cheese")
    if cheese_omelette != {"eggs":2, "milk":1, "cheese":1}:
        print("Failed: the ingredients for a cheese omelette are wrong")
    western_ingredients = {"eggs":2, "milk":1, "cheese":1, "ham":1, "peppers":1, "onion":1}
    r.create("western", western_ingredients)
    if r.get("western") != western_ingredients:
        print("Failed to set the ingredients for the western")
        
        
