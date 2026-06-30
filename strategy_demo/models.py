from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    customer_name: str
    customer_type: str
    amount: float