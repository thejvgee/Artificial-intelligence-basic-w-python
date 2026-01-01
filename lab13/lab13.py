class Map(dict):
    def __init__(self,init = None):
        if init is not None:
            self.__dict__.update(init)
    
    def __getitem__(self,key):
        return self.__dict__[key]
    
    def __setitem__(self,key,val):
        self.__dict__[key] = val

    def __delitem__(self,key):
        try:
            del self.__dict__[key]
        except KeyError:
            print(f"'{key}' utgatai tulhuur oldsngu!")

    def __contains__(self,key):
        return key in self.__dict__
    
    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return self.__dict__
    
m = Map()
m.__setitem__('MNG','Mongolia')
m.__setitem__('CHN','China')
m.__setitem__('RUS','Russia')
m.__setitem__('GER','Germany')
print(m.__repr__())

m.__delitem__('ITA')
m.__delitem__('CHN')

print(m.__repr__())

m.__contains__('KOR')

print(m.__repr__())