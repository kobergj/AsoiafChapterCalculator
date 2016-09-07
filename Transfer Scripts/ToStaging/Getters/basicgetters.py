
class BasicGetter:
    def __init__(self, **initargs):
        self._datagetter = self._connect(**initargs)

    def __call__(self, **callargs):
        return self._datagetter(**callargs)

    def _connect(self, **initargs):
        pass
