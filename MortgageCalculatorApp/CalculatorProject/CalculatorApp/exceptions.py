class CantSetInitialCost(Exception):
    """The value for the "Initial cost" parameter cannot exceed "100 000 000"
    and cannot be less than "100 000"""


class CantSetLoanTerm(Exception):
    """Parameter "time" should not be less than 2 and more than 50"""


class CantSetInitialFee(Exception):
    """The parameter "Initial fee" cannot be negative and cannot be greater
    than or equal to the Initial cost value"""
