class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.array = list.__init__(self, [x for x in range(self.b, (self.a + self.b), self.b) if x])
        self.length = len(self)

    def search(self, num):
        result = {}
        result['count'] = 0
        lo = 0
        hi = self.length - 1
        found = False

        while lo <= hi:
            mid = (lo + hi) // 2
            midval = self[mid]
            if midval == num:
                result['index'] = mid
                found = True
                return result
            else:
                if midval < num:
                    lo = mid + 1
                elif midval > num:
                    hi = mid - 1
        result['count'] += 1

        if found is False:
            result['index'] = -1
            return result


y = BinarySearch(40, 2)
# All the tests pass but this print statement logs {'count': 1, 'index': -1}
# instead of {'count': 3, 'index': -1} according to the tests
print (y.search(33))
