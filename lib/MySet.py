class MySet:

    #set up init method
    def __init__(self, list = []):
        #Store values passed in as keys,keys are unique,values are set to True
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True

    def has(self, value):
        #if value exists True is returned else false is returned
        return  value in self.dictionary

 #print my list
    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
        
    #add method allows you to add new element after initial elements are set after the initial set has been created so that the set is not static
    def add(self, value):
        self.dictionary[value] = True #add a value as a key to the dictionary
        return self    #return updated set
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    #empty the set completely
    def clear(self):
        self.dictionary.clear()
    
my_set = MySet([1,2,3,4])
print(my_set.has(2))
print(my_set.has(5))
my_set.add(5)
print(my_set.has(5))