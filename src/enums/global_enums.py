from enum import Enum


class GlobalErrorMassages(Enum):
    WRONG_STATUS_CODE = "Receiver status code is not equal to expected"
    WRONG_ELEMENT_COUNT = "Number of items is not to expected"