class Stack(object):
    def __init__(self) -> None:
        self.inner_list = []

    def append(self, item) -> None:
        self.inner_list.append(item)
        
    def __getitem__(self, val):
        tmp_list = []
        for i in range(val[0]):
            tmp_list.insert(0, self.inner_list[val[1]].pop(0))
        if val[-1]:
            tmp_list.reverse()
        for element in tmp_list:
            self.inner_list[val[-2]].insert(0, element)
        return val, self.inner_list[val[-2]], self.inner_list[val[1]]
    
    def get_last_indeces(self):
        tmp_list = []
        for l in self.inner_list:
            tmp_list.append(l[0])
        return tmp_list.copy()

    def __str__(self) -> str:
        return f"{self.inner_list}"

    def __repr__(self) -> str:
        return self.__str__()
