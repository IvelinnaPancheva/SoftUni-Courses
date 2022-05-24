class Catalogue:
    products = []

    def __init__(self, name:str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [prod for prod in Catalogue.products if prod[0] == first_letter]

    def __repr__(self):
        to_return_string = f"Items in the {self.name} catalogue:\n"
        to_return_string += "\n".join(sorted(Catalogue.products))
        return to_return_string


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)