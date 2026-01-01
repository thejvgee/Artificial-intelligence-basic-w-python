class Map(dict):
    def __init__(self, init=None):
        if init is not None:
            self.__dict__.update(init)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, val):
        self.__dict__[key] = val

    def __delitem__(self, key):
        try:
            del self.__dict__[key]
        except KeyError:
            print(f"'{key}' utgatai tulhuur oldsngu!")

    def __contains__(self, key):
        return key in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def find_min(self):
        min_key = min(self.__dict__.keys())
        print(f"Хамгийн бага оноотой улс: {self.__dict__[min_key]} ({min_key})")

    def find_max(self):
        max_key = max(self.__dict__.keys())
        print(f"Хамгийн их оноотой улс: {self.__dict__[max_key]} ({max_key})")

    def find_it(self, k):
        lessK = [key for key in self.__dict__.keys() if k > int(key)]
        if lessK:
            max_lessK = max(lessK)
            print(f"{k}-с бага хамгийн их утга: {self.__dict__[max_lessK]} ({max_lessK})")
        else:
            print(f"Тухайн утгаас бага утга олдсонгүй.")

    def iter(self):
        for k in sorted(self.__dict__.keys()):
            print(k)
m = Map()
m.__setitem__(1712, 'Brazil')
m.__setitem__(1765, 'Belgium')
m.__setitem__(1633, 'France')
print(m.__repr__())

m.find_min()
m.find_max()
m.find_it(1734)
m.iter()