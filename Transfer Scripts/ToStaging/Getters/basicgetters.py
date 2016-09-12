
class BasicGetter:
    def __init__(self, *initargs, **initkwargs):
        self._datagetter = self._connect(*initargs, **initkwargs)

    def __call__(self, **callargs):
        return self._datagetter(**callargs)

    def _connect(self, *args, **kwargs):
        pass
