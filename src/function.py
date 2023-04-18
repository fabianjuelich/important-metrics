from enum import StrEnum, auto, Enum

class Function(StrEnum):
    COMPANY_OVERVIEW = 'OVERVIEW'
    INCOME_STATEMENT = auto()
    BALANCE_SHEET = auto()
    CASH_FLOW = auto()