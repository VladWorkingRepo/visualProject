from typing import NamedTuple, Dict, Union, TypeVar

from .exceptions import CantSetInitialCost, CantSetLoanTerm, CantSetInitialFee


class ToCalculateData(NamedTuple):
    time: int
    initial_cost: int
    interest_rate: float
    initial_fee: int


T = TypeVar('T', int, float, str)


class Calculator:
    """Calculating the value of the monthly payment for the client
        based on the data specified by him"""

    # Constant values used in the class for calculating payments
    _COUNT_MONTHS_IN_YEAR = 12
    _CONSTANT_VALUE_FORMULA = 100
    _SECOND_CONSTANT_VALUE_FORMULA = 1

    # Constant values used only in the "check_values" function
    # to check the data received from the client
    _MAX_INITIAL_COST = 1000000000
    _MIN_INITIAL_COST = 10000
    _MAX_TIME = 50
    _MIN_TIME = 2
    _MIN_INITIAL_FEE = 0

    def __init__(self, initial_cost, time, interest_rate, initial_fee):
        self.check_values(initial_cost, time, interest_rate, initial_fee)
        self.__calculator_data = ToCalculateData(
            initial_cost=initial_cost,
            time=time,
            interest_rate=interest_rate,
            initial_fee=initial_fee
        )

    @classmethod
    def check_values(cls, initial_cost, time, interest_rate, initial_fee) -> None:
        """Checks the data received from the client"""
        arguments_case = {
            'initial_cost': lambda x: isinstance(x, int),
            'time': lambda x: isinstance(x, int),
            'initial_fee': lambda x: isinstance(x, int),
            'interest_rate': lambda x: isinstance(x, float)
        }

        if any(arguments_case[key](value) is False for key, value in
               {
                   'initial_cost': initial_cost,
                   'time': time,
                   'initial_fee': initial_fee,
                   'interest_rate': interest_rate
               }.items()):
            raise ValueError

        if initial_cost < cls._MIN_INITIAL_COST or initial_cost >= cls._MAX_INITIAL_COST:
            raise CantSetInitialCost

        if time < cls._MIN_TIME or time >= cls._MAX_TIME:
            raise CantSetLoanTerm

        if initial_fee < cls._MIN_INITIAL_FEE or initial_fee >= initial_cost:
            raise CantSetInitialFee

    def get_calculator_values(self) -> Dict[str, Union[int, float]]:
        """Returns validated values passed by the client"""
        return self.__calculator_data._asdict()

    def _get_monthly_rate(self) -> float:
        """calculate monthly rate"""
        monthly_rate = self.__calculator_data.interest_rate / self._COUNT_MONTHS_IN_YEAR / \
            self._CONSTANT_VALUE_FORMULA
        final_value = round(monthly_rate, 3)
        return final_value

    def _get_total_cost(self) -> int:
        """calculates the total amount of the loan"""
        total_cost = self.__calculator_data.initial_cost - self.__calculator_data.initial_fee
        return total_cost

    def _annuity_payment_calculation(self) -> int:
        """Calculate annuity monthly payment"""
        total_rate = (self._SECOND_CONSTANT_VALUE_FORMULA + self._get_monthly_rate()) ** \
                     (self.__calculator_data.time * self._COUNT_MONTHS_IN_YEAR)

        monthly_payment = self._get_total_cost() * \
            self._get_monthly_rate() * \
            total_rate / (total_rate - self._SECOND_CONSTANT_VALUE_FORMULA)
        final_value = round(monthly_payment)
        return final_value

    def _differential_payment_calculation(self) -> int:
        """Calculate differential monthly payment"""
        monthly_debt_payment = self._get_total_cost() / \
            (self.__calculator_data.time * self._COUNT_MONTHS_IN_YEAR)
        percentage = self._get_total_cost() * self._get_monthly_rate()
        monthly_payment = monthly_debt_payment + percentage
        final_value = round(monthly_payment)
        return final_value

    def get_final_values(self) -> Dict[str, T]:
        """Allows you to get calculated values for annuity and differentiated monthly payments"""
        final_dict = {'annuity_payment': self._annuity_payment_calculation(),
                      'differential_payment': self._differential_payment_calculation(),
                      'interest_rate': self.__calculator_data.interest_rate}
        return final_dict
