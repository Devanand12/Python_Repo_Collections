
# coding: utf-8

# In[68]:


class Jungle:    
    def __init__(self, name):
        self.name = name
        print(self.name)
        
    def welcomeMessage(self):
        print("Hello %s, Welcome to the Jungle" %self.name)   
        
if __name__ == '__main__':
    j = Jungle("Gopinath")
    j.welcomeMessage()


# In[69]:


class RateJungle(Jungle):
  
    def __init__(self, name, rating):
        self.rating = rating        
        print(rating)
        super().__init__(name)
        
    def printRating(self):
        print("Thanks %s for your rating %d" %(self.name, self.rating))
        
r = RateJungle("Gopi", 3)
r.printRating()


# In[67]:


class listOfAnimals(RateJungle):
    
    def __init__(self, monkeys, name, rating):
        self.birds = []
        self.monkeys = monkeys
        RateJungle.name = name
        RateJungle.rating = rating
        
    def allAnimalList(self):
        print(self.birds, '\n', self.monkeys)
        
l =listOfAnimals('Ape', 'Gopinath', 4)
l.birds = ['Owl', 'Parrot']
l.welcomeMessage()
l.printRating()
l.allAnimalList()

