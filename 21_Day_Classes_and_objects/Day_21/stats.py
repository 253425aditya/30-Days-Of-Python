
class statistics:
    def __init__(self,age):
        self.age = age

    def count(self):
        return(len(self.age))

    def sum(self):
        return sum(self.age)

    def min(self):
        return min(self.age)

    def max(self):
        return max(self.age)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum()/self.count()

    def median(self):
        s = sorted(self.age, reverse=True)
        return s[len(s)//2]

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
