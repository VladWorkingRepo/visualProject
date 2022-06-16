from unittest import TestCase

from CalculatorApp.Calculator import Calculator, FinalData
from CalculatorApp.exceptions import CantSetInitialCost, CantSetLoanTerm, CantSetInitialFee


class TestCalculatorArguments(TestCase):
    def test_arguments_type(self):
        """The test checks the data type of the all arguments."""
        arguments_case = [
            {
                'initial_cost': '10000000',
                'time': 5,
                'initial_fee': 1000000,
                'interest_rate': 5.6
            },
            {
                'initial_cost': 10000000,
                'time': '5',
                'initial_fee': 1000000,
                'interest_rate': 5.6
            },
            {
                'initial_cost': 10000000,
                'time': 5,
                'initial_fee': '1000000',
                'interest_rate': 5.6},

        ]
        for arguments in arguments_case:
            with self.assertRaises(ValueError):
                Calculator(**arguments)

    def test_argument_initial_cost_max_value(self):
        """The test checks the maximum allowed value for an argument initial_cost"""
        with self.assertRaises(CantSetInitialCost):
            Calculator(
                initial_cost=9000000000,
                time=5,
                initial_fee=1000000,
                interest_rate=5.6)

    def test_argument_initial_cost_min_value(self):
        """The test checks the minimum allowed value for an argument initial_cost"""
        with self.assertRaises(CantSetInitialCost):
            Calculator(
                initial_cost=10,
                time=5,
                initial_fee=0,
                interest_rate=5.6)

    def test_argument_time_max_value(self):
        """The test checks the maximum allowed value for an argument time"""
        with self.assertRaises(CantSetLoanTerm):
            Calculator(
                initial_cost=10000000,
                time=50,
                initial_fee=1000000,
                interest_rate=5.6)

    def test_argument_time_min_value(self):
        """The test checks the minimum allowed value for an argument time"""
        with self.assertRaises(CantSetLoanTerm):
            Calculator(
                initial_cost=10000000,
                time=1,
                initial_fee=1000000,
                interest_rate=5.6)

    def test_argument_initial_fee_max_value(self):
        """The test checks the maximum allowed value for an argument initial_fee"""
        with self.assertRaises(CantSetInitialFee):
            Calculator(
                initial_cost=10000000,
                time=10,
                initial_fee=90000000,
                interest_rate=5.6)

    def test_argument_initial_fee_min_value(self):
        """The test checks the minimum allowed value for an argument initial_fee"""
        with self.assertRaises(CantSetInitialFee):
            Calculator(
                initial_cost=10000000,
                time=10,
                initial_fee=-1,
                interest_rate=5.6)


class TestCalculatorMethods(TestCase):
    def setUp(self):
        self.calculator = Calculator(
            initial_cost=1000000,
            time=5,
            initial_fee=250000,
            interest_rate=4.0)

    def test_get_final_values(self):
        """The test checks what the get_final_values method should return.
        It is this method that returns the prepared data structure
        that is used further in the program."""
        tested_result = self.calculator.get_final_values()
        expected_result = FinalData(
            annuity_payment=13677,
            differential_payment=14750, interest_rate=4.0)
        self.assertEqual(expected_result, tested_result)

    def test_differential_payment_calculation(self):
        """The test checks the return value with the _differential_payment_calculation method.
        This value will also be present in the final tuple that
        must be sent to the client upon his request."""
        tested_result = self.calculator._differential_payment_calculation()
        self.assertEqual(14750, tested_result)

    def test_annuity_payment_calculation(self):
        """The test checks the calculation of the final value that will be present in
        the final named tuple that should be given to the client as a response to his request"""
        annuity_payment = self.calculator._annuity_payment_calculation()
        expected_value = 13677
        self.assertEqual(expected_value, annuity_payment)

    def test_get_total_cost_value(self):
        """This test checks the value returned by the _get_total_cost method.
        The final value returned by the method is rounded it will always be an integer"""
        total_cost = self.calculator._get_total_cost()
        expected_value = 750000
        self.assertEqual(expected_value, total_cost)

    def test_get_monthly_rate_value(self):
        """The test checks the values returned by the _get_monthly_rate method.
        Due to the nature of the formula used, the return value will always be
        a floating point value."""
        monthly_rate = self.calculator._get_monthly_rate()
        expected_value = 0.003
        self.assertEqual(expected_value, monthly_rate)

    def test_get_calculator_values(self):
        """The test checks what values should be obtained as a result of
        calling the get_calculator_values method.
        This method returns a dictionary obtained from a named tuple"""
        calculator_values = self.calculator.get_calculator_values()
        expected_value = {'time': 5, 'initial_cost': 1000000,
                          'interest_rate': 4.0, 'initial_fee': 250000}
        self.assertEqual(expected_value, calculator_values)
