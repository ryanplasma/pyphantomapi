class PhantomBase():
    def __init__(self, phantom, _data):
        self._phantom = phantom
        if _data:
            for attribute, value in _data.items():
                setattr(self, attribute, value)
