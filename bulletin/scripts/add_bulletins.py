import random

from bulletin.models import Bulletin
from user.models import User

titles = [
    "iPhone 15 Pro Max",
    "PlayStation 5",
    "MacBook Air M3",
    "Велосипед Trek FX 3",
    "Электросамокат Xiaomi",
    "Гитара Fender Stratocaster",
    "Монитор LG UltraFine 5K",
    "Кресло Herman Miller",
    "Наушники Sony WH-1000XM5",
    "Часы Apple Watch Series 9",
]

descriptions = [
    "В идеальном состоянии, полный комплект.",
    "Почти не использовался, всё работает.",
    "Новая модель, куплена недавно.",
    "Есть мелкие царапины, цена снижена.",
    "Продажа по причине ненадобности.",
    "Подарок, не подошёл.",
    "Гарантия до конца года.",
    "Использовался аккуратно, без дефектов.",
    "Цвет чёрный, всё оригинальное.",
    "Без торга, цена окончательная.",
]

users = list(User.objects.all())

for i in range(10):
    Bulletin.objects.create(
        title=titles[i],
        price=random.randint(5000, 200000),
        description=descriptions[i],
        author=users[i % len(users)],  # по кругу назначаем пользователей
    )
print("Bulletins added")
