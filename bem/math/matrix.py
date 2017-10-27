

class Matrix(object):

    @property
    def cnt(self):
        return self.data

    @property
    def matrix(self):
        return Matrix(self.cnt)

    def __init___(self, matrix):
        """
        """
        self.data = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

    def _check_matrix(self):
        """
        """
        for n in self.matrix[1::]:
            if len(n) != self.m:
                return False
        return True

    def raws(self, dln=[]):
        """
        """
        for i in dln:
            yield self.data[i]

    def columns(self, dln=[]):
        """
        """
        for i in self.data:
            yield [i[k] for k in dln]

    def sort_by(self, field, up=True, key=None):
        if up:
            return sorted(self.matrix, key=key)
        else:
            return sorted(self.matrix, key=key)[::-1]

    def filter_raws(self, bool_filter, field):
        """
        """
        for line in self.matrix:
            if bool_filter(line[field]):
                yield line


    def echelon_raws(self, ech_filter, field):
        """
        """
        d = dict()
        for line in self.matrix:
            a = ech_filter(line[field])
            if a == 0 or a is None:
                continue
            else:
                d[a] = line
        return d


    @classmethod
    def SortedMatrix(cls, matrix):
        """
        """
        pass

    @classmethod
    def Raws(cls, matrix, *args, **kwargs):
        """
        """
        pass

    @classmethod
    def Columns(cls, matrix, *args, **kwargs):
        """
        """
        pass

    @classmethod
    def Filter(cls, matrix):
        pass

    @classmethod
    def Echelon(cls):
        pass


class BemMatrix(Matrix):

    def __init__(self, matrix):
        Matrix.__init__(self, matrix)

    def _get_raws_after_date():
        pass

    def _get_raws_before_date():
        pass

    @classmethod
    def BeforeDate(cls):
        pass

    @classmethod
    def AfterDate(cls):
        pass
