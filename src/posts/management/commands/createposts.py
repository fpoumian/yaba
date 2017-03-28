from django.core.management.base import BaseCommand
from django.db import transaction

from posts.models import Post
from posts.seed import create_posts


class Command(BaseCommand):
    help = 'Seeds the database with a given number of unpublished and published posts.'

    def add_arguments(self, parser):
        parser.add_argument('--unpublished',
                            default=0,
                            type=int,
                            help='The number of unpublished posts to create.')

        parser.add_argument('--published',
                            default=0,
                            type=int,
                            help='The number of published posts to create.')

    def handle(self, *args, **options):
        confirm = input("""This operation will IRREVERSIBLY DESTROY all posts currently in the database.
        Are you sure you want to do this?

        Type 'yes' to continue, or 'no' to cancel: """)

        if confirm == 'yes':
            with transaction.atomic():
                Post.objects.all().delete()

                unpublished = max(0, options['unpublished'])
                published = max(0, options['published'])
                create_posts(unpublished, published)

        else:
            self.stdout.write('Operation cancelled.\n')
