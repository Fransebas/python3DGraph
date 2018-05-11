import numpy as np

class Face():

    def __init__(self, a, b, c):
        """

        :param a: is a numpy 3 vector
        :param b: is a numpy 3 vector
        :param c: is a numpy 3 vector
        """
        self.a, self.b, self.c = np.array(a), np.array(b), np.array(c)


    def getNormal(self):
        a1 = self.a - self.b
        a2 = self.a - self.c

        return np.cross(a1, a2)
