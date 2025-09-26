class SweetShop:
    def __init__(self):
        self.sweets = {}  # store sweet info like {"Ladoo": {"price":10, "stock":100}}

    def add_sweet(self, name, price, stock):
        self.sweets[name] = {"price": price, "stock": stock}

    def place_order(self, customer, order_items):
        """
        customer: string, customer name
        order_items: dict, sweet_name -> quantity
        """
        total = 0
        for sweet, qty in order_items.items():
            if sweet not in self.sweets:
                raise ValueError(f"{sweet} not available")
            if self.sweets[sweet]["stock"] < qty:
                raise ValueError(f"Not enough stock for {sweet}")
            total += self.sweets[sweet]["price"] * qty
            self.sweets[sweet]["stock"] -= qty
        return total
