class Matrix(object):

    def __init___(self, matrix):
        self.data = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])

    def _check_matrix(self):
        for n in self.matrix[1::]:
            if len(n) != self.m:
                return False
        return True

    def raws(self, ln):
        pass

    def columns(self, ln):
        pass

    def sort_by(self, field, criteria, filter):
        pass

    @classmethod
    def SortedMatrix(cls, matrix):
        pass

    def filter_columns(self):
        pass

    def filter_raws(self, filter, on_field):
        pass

    @classmethod
    def Raws(cls, matrix, raws):
        pass

    @classmethod
    def Columns(cls, matrix, raws):
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
