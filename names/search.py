class FindDuplicates:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = FindDuplicates(value)
            else:
                self.left.insert(value)

        if value > self.value:
            if not self.right:
                self.right = FindDuplicates(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            self.right.contains(target)
        else:
            self.left.contains(target)
