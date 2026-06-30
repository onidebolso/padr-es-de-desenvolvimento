from .models import Order
from .sem_strategy import calculate_total_without_strategy
from .strategy import Checkout, strategy_for


def format_money(value: float) -> str:
    return f"R$ {value:.2f}".replace(".", ",", 1)


def run_demo() -> None:
    orders = [
        Order("Ana", "comum", 100.0),
        Order("Bruno", "recorrente", 100.0),
        Order("Carla", "premium", 100.0),
    ]

    print("=== Demonstração sem Strategy ===")
    for order in orders:
        total = calculate_total_without_strategy(order)
        print(f"{order.customer_name} ({order.customer_type}): {format_money(total)}")

    print()
    print("=== Demonstração com Strategy ===")
    for order in orders:
        checkout = Checkout(strategy_for(order.customer_type))
        total = checkout.total(order)
        print(f"{order.customer_name} ({order.customer_type}): {format_money(total)}")


if __name__ == "__main__":
    run_demo()