

class AbstractDairyProduct():

    def __init__(self, warranty_period_in_days=0, price_in_uah: float = 0, producer=None, producing_country=None,
                 fat_content_in_percentage=0):
        self.warranty_period_in_days = warranty_period_in_days
        self.price_in_uah = price_in_uah
        self.producer = producer
        self.producing_country = producing_country
        self.fat_content_in_percentage = fat_content_in_percentage

