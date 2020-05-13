from model.abstract_dairy_product import AbstractDairyProduct


class IceCream(AbstractDairyProduct):

    def __init__(self, warranty_period_in_days=0, price_in_uah=0, producer=None, producing_country=None,
                 fat_content_in_percentage=0, name_of_taste=None, weight_in_grams=0):
        super().__init__(warranty_period_in_days, price_in_uah, producer, producing_country, fat_content_in_percentage)
        self.name_of_taste = name_of_taste
        self.weight_in_grams = weight_in_grams

    def __str__(self):
        return f"{self.warranty_period_in_days}, {self.price_in_uah}, {self.producer}, {self.producing_country}," \
               f"{self.fat_content_in_percentage}, {self.name_of_taste}, {self.weight_in_grams}"
