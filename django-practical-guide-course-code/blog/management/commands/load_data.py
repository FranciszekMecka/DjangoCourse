# blog/management/commands/load_data.py

from django.core.management.base import BaseCommand
from blog.models import Author, Tag, Post
from blog.factories import AuthorFactory, TagFactory, PostFactory


class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        # Load Authors
        authors = AuthorFactory.create_batch(3)

        # Load Tags
        tags = TagFactory.create_batch(3)

        # Load Posts
        posts = PostFactory.create_batch(4, author=authors[0], tags=[tags[0], tags[1]])
        PostFactory.create_batch(4, author=authors[1], tags=[tags[1], tags[2]])

        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))