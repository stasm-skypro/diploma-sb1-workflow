from bulletin.models import Bulletin, Review
from user.models import User

review_texts = [
    "Отличный товар, полностью соответствует описанию.",
    "Продавец ответил быстро, всё понравилось.",
    "Хорошее качество, рекомендую.",
    "Быстрая доставка и честное описание.",
    "Пользуюсь уже неделю — всё отлично.",
    "Было немного сомнений, но всё супер!",
    "Упаковка надёжная, товар новый.",
    "Продавец вежливый, помог с выбором.",
    "Реально стоит своих денег.",
    "Сделка прошла без проблем, рекомендую!",
]

users = list(User.objects.all())
ads = list(Bulletin.objects.all())

for i in range(10):
    Review.objects.create(
        text=review_texts[i],
        author=users[i % len(users)],  # равномерно распределяем авторов
        ad=ads[i % len(ads)],  # равномерно распределяем объявления
    )

print("Reviews added")
