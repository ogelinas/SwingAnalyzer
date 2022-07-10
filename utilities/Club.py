from enum import Enum


class Club(Enum):
    
    DRIVER = ('Driver', 'driver')
    WOOD_3 = ('3 Wood', 'wood')
    HYBRIDE_3 = ('3 Hybrid', 'hybrid')
    HYBRIDE_4 = ('4 Hybrid', 'hybrid')
    IRON_4 = ('4 Iron', 'iron')
    IRON_5 = ('5 Iron', 'iron')
    IRON_6 = ('6 Iron', 'iron')
    IRON_7 = ('7 Iron', 'iron')
    IRON_8 = ('8 Iron', 'iron')
    IRON_9 = ('9 Iron', 'iron')
    WEDGE_PITCHING = ('Pitching Wedge', 'wedge')
    WEDGE_GAP = ('Gap Wedge', 'wedge')
    WEDGE_SAND = ('Sand Wedge', 'wedge')
    WEDGE_LOB = ('Lob Wedge', 'wedge')
    PUTTER = ('Putter', 'putter')

    def __init__(self, text, familly) -> None:
        self.text = text
        self.familly = familly

    def __repr__(self) -> str:
        # return super().__repr__()
        return self.text

    def __str__(self) -> str:
        # return super().__str__()
        return self.text