from typing import Optional
from typing import Union

def find_product(product_id: int) -> Optional[str]:
    products = {
        1: "Rice",
        2: "Sugar",
    }

    return products.get(product_id)

print(find_product(1))
print(find_product(99))

# Union
def get_product(product_id: Union[int, str]) -> str:
    return f"Searching for product: {product_id}"


print(get_product(101))
print(get_product("RICE-001"))

# def get_product(product_id: int | str) -> str:
#    return f"Searching for product: {product_id}"
