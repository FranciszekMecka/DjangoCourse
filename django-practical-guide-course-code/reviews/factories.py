import factory
from .models import Review


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    user_name = factory.Faker('name')
    review_text = factory.Faker('paragraph', nb_sentences=3)
    rating = factory.Iterator([1, 2, 3, 4, 5])
