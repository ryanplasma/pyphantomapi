from .base import PhantomBase


class Asset(PhantomBase):
    def __init__(self, phantom, _data):
        super().__init__(phantom, _data)
