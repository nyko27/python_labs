from model.abstract_dairy_product import AbstractDairyProduct


class Milk(AbstractDairyProduct):

    def __init__(self, warranty_period_in_days, price_in_uah, producer, producing_country, fat_content_in_percentage,
                 volume_in_litres, acidity_in_ph):
        super().__init__(warranty_period_in_days, price_in_uah, producer, producing_country, fat_content_in_percentage)
        self.volume_in_litres = volume_in_litres
        self.acidity_in_ph = acidity_in_ph
