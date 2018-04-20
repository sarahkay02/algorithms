
class edge():
    # constructor
    def __init__(self, frm, to, weight):
        self.frm = frm
        self.to = to
        self.weight = weight

    # methods
    def getFrm(self):
        return self.frm

    def getTo(self):
        return self.to

    def getWeight(self):
        return self.weight

    def __str__(self):
        # 3 for right-alignment (3 digits in these numbers)
        # .5 for 5 digits for weight (float)
        return '%3d --> %3d    %.5f' % (self.frm, self.to, self.weight)
