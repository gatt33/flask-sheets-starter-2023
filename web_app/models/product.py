
DEFAULT_PRODUCTS = [
    # see: https://picsum.photos/images
    {'id': 1, 'name': 'Competition Prep', 'description': 'Bodybuilding Competition Training', 'price': 4.99, 'url': 'https://i.ibb.co/mHMB6p7/Bodybuilding-Prep-Training.jpg'},
    {'id': 2, 'name': 'Cross Fit', 'description': 'An individually-prepared schedule for you.', 'price': 3.49, 'url': 'https://i.ibb.co/GJnLMyY/Cross-Fit-Training.jpg'},
    {'id': 3, 'name': 'Nutrition Training', 'description': 'Get Lean or Thick with our experts', 'price': 129.99, 'url': 'https://i.ibb.co/xXSNkFK/Nutrition-Training.jpg'},
    {'id': 4, 'name': 'Personal Training', 'description': 'We got you for the busy professionals', 'price': 129.99, 'url': 'https://i.ibb.co/xg317s0/personal-trainer-1-compressor.jpg'},
    {'id': 5, 'name': 'Spin Training', 'description': 'Welcome for all age groups', 'price': 0.99, 'url': 'https://i.ibb.co/fXt8PTV/Spin-Training.jpg'},
    {'id': 6, 'name': 'HIIT training', 'description': 'See results fast with us', 'price': 0.99, 'url': 'https://i.ibb.co/K9832Zq/HIIT-Training.jpg'}
]


class Product:
    def __init__(self, attrs):
        self.id = attrs.get("id")
        self.name = attrs.get("name")
        self.description = attrs.get("description")
        self.price = attrs.get("price")
        self.url = attrs.get("url")
        self.created_at = attrs.get("created_at")

    @property
    def to_row(self):
        return [self.id, self.name, self.description, self.price, self.url, str(self.created_at)]
