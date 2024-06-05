# blog/factories.py

import factory
from .models import Author, Tag, Post


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    caption = factory.Faker('word')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=6)
    excerpt = factory.Faker('sentence', nb_words=12)
    image_name = factory.Faker('image_url', width=250, height=250)
    slug = factory.Faker('slug')
    content = factory.Faker('text', max_nb_chars=200)
    author = factory.SubFactory(AuthorFactory)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            # A list of tags were passed in, use them
            for tag in extracted:
                self.tags.add(tag)
