import os
import factory
import factory.django
from django.utils.timezone import now
from faker.providers.lorem.la import Provider as LoremProvider
from django.utils.text import slugify
from django.conf import settings

from .models import Post


class ExtendedLoremProvider(LoremProvider):
    @classmethod
    def title(cls, nb_words=6, variable_nb_words=True):
        return cls.sentence(nb_words, variable_nb_words)[:-1]

    @classmethod
    def split_paragraphs(cls, nb=3):
        return '\n\n'.join(cls.paragraphs(nb))


factory.Faker.add_provider(ExtendedLoremProvider)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    is_published = False
    title = factory.Faker('title')
    slug = factory.LazyAttribute(lambda p: slugify(p.title[:49]))
    featured_image = os.path.join('posts/uploads', 'placeholder.jpg')
    excerpt = factory.Faker('sentence', nb_words=20)
    body = factory.Faker('split_paragraphs', nb=6)

    @factory.lazy_attribute
    def published_at(self):
        return now() if self.is_published else None
