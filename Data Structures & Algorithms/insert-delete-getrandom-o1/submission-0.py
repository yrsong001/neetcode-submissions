import random
class RandomizedSet(object):
    # A set gives you insert/remove but not random. A list gives you B but not A (lookup is O(n)).
    # We need both.
    # Dict with val become a list?
    # combo of dict and list let random become O(1)
    def __init__(self):
        # return []
        self.nums = [] # list would give index to val
        self.val_to_idx = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_idx:
            return False
        else:
            self.val_to_idx[val] = len(self.nums)
            self.nums.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # Removing from the middle of a list is O(n) — everything shifts.
        # O(1) trick:  instead of removing from the middle, swap the target with the last element, then remove the last.
        if val in self.val_to_idx:
            last = self.nums[-1] # after swap it changes
            self.nums[self.val_to_idx[val]], self.nums[-1] = self.nums[-1], self.nums[self.val_to_idx[val]]
            self.val_to_idx[last] = self.val_to_idx[val] 
            self.nums.pop()
            del self.val_to_idx[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        # inside a class, always use self.
        # Without self., Python thinks it's a local variable (disappears after the function ends)
        return random.choice(self.nums) ## always need!


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()