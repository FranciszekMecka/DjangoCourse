from django.core.management.base import BaseCommand
from reviews.factories import ReviewFactory


class Command(BaseCommand):
    help = 'Generate random reviews using ReviewFactory'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='The number of reviews to create')

    def handle(self, *args, **options):
        count = options['count']
        reviews = ReviewFactory.create_batch(count)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} reviews'))
