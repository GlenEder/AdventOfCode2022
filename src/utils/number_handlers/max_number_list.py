
class MaxNumberList():
    """
    Number list that keeps only the largest numbers added to it
    Use add(n) to insert new numbers (auto checks if number should be added)
    """
    def __init__(self, size):
        self.length = size
        self.nums = [0] * size

    def add(self, n):
        if n > self.nums[self.length - 1]:
            self.nums.append(n)
            self.nums.sort(reverse=True)
            self.nums = self.nums[0:self.length]

    def sum(self):
        return sum(self.nums)

    def max(self):
        return self.nums[0]

    def reinit(self, numlist):
        self.nums = numlist
        self.nums.sort(reverse=True)
        self.length = len(self.nums)