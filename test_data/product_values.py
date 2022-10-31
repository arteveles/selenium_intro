from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d")
_product = [
    (f"test_product_{now}")
]


def product_name():
    return _product
