from enum import Enum


class GroupBy(Enum):
    DAY = ('Day', '%Y-%m-%d' ,'date_y_m_d')
    WEEK = ('Week', '%Y-%m-%W', 'date_y_m_w')
    MONTH = ('Month', '%Y-%m', 'date_y_m')
    YEAR = ('Year', '%Y', 'date_y')
    
    def __init__(self, periode, format, column_name) -> None:
        self.periode = periode
        self.format = format
        self.column_name = column_name
