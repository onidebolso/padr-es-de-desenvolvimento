from dataclasses import dataclass
from typing import Protocol

from .models import Order


class DiscountStrategy(Protocol):
    def calculate(self, amount: float) -> float:
        """Calcula o total após o desconto."""


@dataclass(frozen=True)
class NoDiscount:
    def calculate(self, amount: float) -> float:
        return amount


@dataclass(frozen=True)
class RecurringCustomerDiscount:
    def calculate(self, amount: float) -> float:
        return amount * 0.90


@dataclass(frozen=True)
class PremiumCustomerDiscount:
    def calculate(self, amount: float) -> float:
        return amount * 0.80


@dataclass
class Checkout:
    strategy: DiscountStrategy

    def total(self, order: Order) -> float:
        return self.strategy.calculate(order.amount)


def strategy_for(customer_type: str) -> DiscountStrategy:
    if customer_type == "comum":
        return NoDiscount()
    if customer_type == "recorrente":
        return RecurringCustomerDiscount()
    if customer_type == "premium":
        return PremiumCustomerDiscount()
    raise ValueError(f"Tipo de cliente desconhecido: {customer_type}")