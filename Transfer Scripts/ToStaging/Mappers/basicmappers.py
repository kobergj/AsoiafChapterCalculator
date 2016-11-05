
class Mapper:
    def __init__(self, outmodel):
        self.outmodel = outmodel

    def __call__(self, inmodel):
        # Map InModel to OutModel
        pass

class ListMapper(Mapper):
    def __call__(self, maplist, model):
        outmodels = []
        for descr in maplist:

            args = self.extract_args(descr, model)

            outmodels.append(self.outmodel(*args))

        return outmodels
