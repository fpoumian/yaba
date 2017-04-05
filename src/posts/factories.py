import os
import factory
import factory.django
from django.utils.timezone import now
from faker.providers.lorem.la import Provider as LoremProvider
from faker.providers.date_time import Provider as DateTimeProvider
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

from .models import Post


class ExtendedLoremProvider(LoremProvider):
    @classmethod
    def title(cls, nb_words=6, variable_nb_words=True):
        return cls.sentence(nb_words, variable_nb_words)[:-1]

    @classmethod
    def split_paragraphs(cls, nb=3):
        return '\n\n'.join(cls.paragraphs(nb))

    @staticmethod
    def markdown():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'mocks', 'markdown_post.md'), 'r') as f:
            file_content = f.read()
        return file_content


factory.Faker.add_provider(ExtendedLoremProvider)
factory.Faker.add_provider(DateTimeProvider)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    is_published = False
    title = factory.Faker('title')
    slug = factory.LazyAttribute(lambda p: slugify(p.title[:49]))
    featured_image = os.path.join('posts/uploads', 'placeholder.jpg')
    excerpt = factory.Faker('sentence', nb_words=20)
    # body = factory.Faker('split_paragraphs', nb=6)
    body = factory.Faker('markdown')

    @factory.lazy_attribute
    def published_at(self):
        published_date = factory.Faker('date_time_this_month')
        return published_date.generate(
            extra_kwargs={'tzinfo': timezone.get_default_timezone()}) if self.is_published else None
