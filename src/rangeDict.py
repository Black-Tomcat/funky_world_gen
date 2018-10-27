class RangeDict(dict):
    def __getitem__(self, item):
        if type(item) != range:
            for key in self:
                if list(key)[0] <= item < list(key)[-1] + 1:
                    return self[key]
        else:
            return super().__getitem__(item)