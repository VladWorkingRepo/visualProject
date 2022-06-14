# Mortgage offer calculator
___

This project will allow calculating the final monthly mortgage payment for a number of banks
based on the mortgage interest rate they set

### Used technology stack:
- Django
- Django REST framework

The work of the program is organized in such a way that the client in the request indicates the 
***amount of the loan***, ***the amount of the down payment***, ***the desired loan term***.

Example of data sent by the client:

    {
        "total_cost": "5000000",
        "initial_fee": "500000",
        "time": "10"
    }

The data received from the client is processed in a certain way, 
in response the client receives data about ***interest rate***, ***bank name***, 
***differentiated monthly payment***, ***annuity monthly payment***.

Example of a response to a customer request:

    [
        {
            "interest_rate": 6.45,
            "bank_name": "N Bank",
            "differential_payment": 61688,
            "annuity_payment": 50982
        },
        {
            "interest_rate": 6.0,
            "bank_name": "Another Bank",
            "differential_payment": 60000,
            "annuity_payment": 49959
        },
        {
            "interest_rate": 5.6,
            "bank_name": "Some Bank",
            "differential_payment": 58500,
            "annuity_payment": 49060
        }
    ]