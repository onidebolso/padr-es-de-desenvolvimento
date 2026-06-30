from .models import Order


def calculate_total_without_strategy(order: Order) -> float:
    discount_rate = 0.0

    if order.customer_type == "comum":
        discount_rate = 0.0
    elif order.customer_type == "recorrente":
        discount_rate = 0.10
    elif order.customer_type == "premium":
        discount_rate = 0.20
    else:
        raise ValueError(f"Tipo de cliente desconhecido: {order.customer_type}")

    discount = order.amount * discount_rate
    return order.amount - discount