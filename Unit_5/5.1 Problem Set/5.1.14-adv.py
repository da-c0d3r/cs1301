#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        self.meat = self.set_meat(meat)
        self.to_go = self.set_to_go(to_go)
        self.rice = self.set_rice(rice)
        self.beans = self.set_beans(beans)
        self.extra_meat = self.set_extra_meat(extra_meat)
        self.guacamole = self.set_guacamole(guacamole)
        self.cheese = self.set_cheese(cheese)
        self.pico = self.set_pico(pico)
        self.corn = self.set_corn(corn)

    # setters
    def set_meat(self, meat):
        valid = ["chicken", "pork", "steak", "tofu"]
        if meat in valid:
            self.meat = meat
        else:
            self.meat = False
        return self.meat
    def set_to_go(self, to_go):
        if type(to_go) != bool:
            self.to_go = False
        else:
            self.to_go = to_go
        return self.to_go
    def set_rice(self, rice):
        valid = ["brown", "white"]
        if rice in valid:
            self.rice = rice
        else:
            self.rice = False
        return self.rice
    def set_beans(self, beans):
        valid = ["black", "pinto"]  
        if beans in valid:
            self.beans = beans
        else:
            self.beans = False
        return self.beans
    def set_extra_meat(self, extra_meat):
        if type(extra_meat) != bool:
            self.extra_meat = False
        else:
            self.extra_meat = extra_meat
        return self.extra_meat
    def set_guacamole(self, guacamole): 
        if type(guacamole) != bool:
            self.guacamole = False
        else:
            self.guacamole = guacamole
        return self.guacamole
    def set_cheese(self, cheese):
        if type(cheese) != bool:
            self.cheese = False
        else:
            self.cheese = cheese
        return self.cheese
    def set_pico(self, pico):    
        if type(pico) != bool:
            self.pico = False
        else:
            self.pico = pico     
        return self.pico      
    def set_corn(self, corn):
        if type(corn) != bool:
            self.corn = False
        else:
            self.corn = corn
        return self.corn

    # getters
    def get_meat(self):
        return self.meat
    def get_to_go(self):
        return self.to_go
    def get_rice(self):
        return self.rice
    def get_beans(self):
        return self.beans
    def get_extra_meat(self):
        return self.extra_meat
    def get_guacamole(self):
        return self.guacamole
    def get_cheese(self):
        return self.cheese
    def get_pico(self):
        return self.pico
    def get_corn(self):
        return self.corn

    def get_cost(self):
        cost = 5.0
        meater = ["chicken", "pork", "tofu"]
        
        if self.meat in meater:
            cost += 1.00
        elif self.meat == "steak":
            cost += 1.50
        if (self.extra_meat == True) and (self.meat != False):    
            cost += 1.00
        if self.guacamole:
            cost += 0.75
        return cost

#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())

