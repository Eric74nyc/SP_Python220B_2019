"""Furniture class"""

from inventory_management.inventory_class import Inventory


class Furniture(Inventory):
    """Class to hold all furniture inventory"""

    def __init__(self, product_code, description, market_price,
                 rental_price, material, size):
        # Creates common instance variables from the parent class
        Inventory.__init__(self, product_code, description,
                           market_price, rental_price)
        self.material = material
        self.size = size

    def return_as_dictionary(self):
        """Return all inventory with furniture as a dictionary"""
        output_dict = Inventory.return_as_dictionary(self)
        output_dict['material'] = self.material
        output_dict['size'] = self.size

        return output_dict
