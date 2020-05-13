from model.abstract_dairy_product import AbstractDairyProduct


class Cheese(AbstractDairyProduct):

    def __init__(self, warranty_period_in_days, price_in_uah, producer, producing_country, fat_content_in_percentage,
                 weight_in_grams, name_of_cheese):
        super().__init__(self, warranty_period_in_days, price_in_uah, producer, producing_country,
                         fat_content_in_percentage)
        self.weight_in_grams = weight_in_grams
        self.name_of_cheese = name_of_cheese
