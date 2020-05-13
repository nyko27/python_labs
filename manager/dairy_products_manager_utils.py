from model.ice_cream import IceCream
from typing import List
from model.sort_type import SortType


class DairyProductManagerUtils:

    def __init__(self, ice_cream_list: List[IceCream]):
        self.ice_cream_list = ice_cream_list

    def sort_by_warranty_period(self, sort_type: SortType) -> List[IceCream]:
        """
        Sorts list of ice-creams by warranty period

        >>> list_of_ice_cream = [IceCream( warranty_period_in_days=100), IceCream( warranty_period_in_days=120),\
                              IceCream( warranty_period_in_days=150),IceCream( warranty_period_in_days=80)]
        >>> util_manager=DairyProductManagerUtils(list_of_ice_cream)
        >>> ice_creams_sorted_by_warranty_period_ascending = util_manager.sort_by_warranty_period(SortType.ASCENDING)
        >>> [ice_cream.warranty_period_in_days for ice_cream in ice_creams_sorted_by_warranty_period_ascending]
        [80, 100, 120, 150]

        >>> ice_creams_sorted_by_warranty_period_descending = util_manager.sort_by_warranty_period(SortType.DESCENDING)
        >>> [ice_cream.warranty_period_in_days for ice_cream in ice_creams_sorted_by_warranty_period_descending]
        [150, 120, 100, 80]
        """

        if sort_type == SortType.ASCENDING:
            sorted_ice_creams = sorted(self.ice_cream_list, key=lambda ice_cream: ice_cream.warranty_period_in_days)
        elif sort_type == SortType.DESCENDING:
            sorted_ice_creams = sorted(self.ice_cream_list, key=lambda ice_cream: ice_cream.warranty_period_in_days,
                                       reverse=True)
        return sorted_ice_creams

    def sort_by_producer(self, sort_type: SortType) -> List[IceCream]:
        """
        Sorts ice-creams by name of their producer

        >>> list_of_ice_cream = [IceCream(producer="Limo"), IceCream(producer="Laska"),\
                              IceCream(producer="Rud"), IceCream(producer="Lasunka")]
        >>> util_manager=DairyProductManagerUtils(list_of_ice_cream)
        >>> ice_creams_sorted_by_producer_ascending = util_manager.sort_by_producer(SortType.ASCENDING)
        >>> [ice_cream.producer for ice_cream in ice_creams_sorted_by_producer_ascending]
        ['Laska', 'Lasunka', 'Limo', 'Rud']
         >>> ice_creams_sorted_by_producer_descending = util_manager.sort_by_producer(SortType.DESCENDING)
        >>> [ice_cream.producer for ice_cream in ice_creams_sorted_by_producer_descending]
        ['Rud', 'Limo', 'Lasunka', 'Laska']
        """
        if sort_type == SortType.ASCENDING:
            sorted_ice_creams = sorted(self.ice_cream_list, key=lambda ice_cream: ice_cream.producer)
        elif sort_type == SortType.DESCENDING:
            sorted_ice_creams = sorted(self.ice_cream_list, key=lambda ice_cream: ice_cream.producer,
                                       reverse=True)
        return sorted_ice_creams


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
