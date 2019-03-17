
# coding: utf-8

# In[ ]:


class Employee:                        '''A sample Employee class'''    
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    
    def fullName(self):
        return f"{self.first} {self.last}"
    
    def __repr__(self):
        return "Employee('{self.first}', '{self.last}', '{self.pay}')"

