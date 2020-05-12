from model.ice_cream import IceCream
from typing import List


class DairyProductManager:

    def __init__(self, ice_cream_list: List[IceCream]):
        self.ice_cream_list = ice_cream_list

    def find_ice_creams_with_price_higher_than(self, price: float) -> List[IceCream]:
        """
        Returns list of all ice-creams with price higher than price given in method parametr

        >>> list_of_ice_cream = [IceCream( price_in_uah=20), IceCream( price_in_uah=15.5), IceCream( price_in_uah=22), IceCream( price_in_uah=28.5)]
        >>> manager = DairyProductManager(list_of_ice_cream)
        >>> manager.find_ice_creams_with_price_higher_than(200)
        []
        >>> manager.find_ice_creams_with_price_higher_than(20)
        [['0, 22, None, None, 0, None, 0'], ['0, 28.5, None, None, 0, None, 0']]
        >>> manager.find_ice_creams_with_price_higher_than(20)
        []
        """
        found_ice_creams = []
        for ice_cream in self.ice_cream_list:
            if ice_cream.price_in_uah > price:
                found_ice_creams.append([str(ice_cream)])
        return found_ice_creams


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
