from typing import List, Dict, NamedTuple, TypeVar

from .Calculator import Calculator, FinalData
from .models import Banks


T = TypeVar('T', int, float, str)


class FullDataUser(NamedTuple):
    bank_name: str
    annuity_payment: int
    differential_payment: int
    interest_rate: float


def calculation_annuity_and_differentiated_payments(
        initial_cost: int, time: int,
        interest_rate: float, initial_fee: int) -> FinalData:
    """Calculates annuity payment and differential payment values"""
    calculated_values = Calculator(initial_cost, time, interest_rate, initial_fee)
    result = calculated_values.get_final_values()
    return result


def data_for_client(validate_data: dict) -> List[Dict[str, T]]:
    """Accepts data checked by the serializer as input, Returns the final value for the client"""
    banks = Banks.objects.all()

    data_list_to_client = []
    for bank in banks:
        basic_information_for_client = calculation_annuity_and_differentiated_payments(
            initial_cost=validate_data['total_cost'],
            time=validate_data['time'],
            initial_fee=validate_data['initial_fee'],
            interest_rate=bank.interest_rate)

        full_information_for_client = FullDataUser(
            bank_name=bank.bank_name,
            annuity_payment=basic_information_for_client.annuity_payment,
            differential_payment=basic_information_for_client.differential_payment,
            interest_rate=basic_information_for_client.interest_rate)

        prepared_data = full_information_for_client._asdict()
        data_list_to_client.append(prepared_data)

    return data_list_to_client
