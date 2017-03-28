import factory
import factory.django
from django.utils.timezone import now
from faker.providers.lorem.la import Provider as LoremProvider
from django.utils.text import slugify

from .models import Post


class ExtendedLoremProvider(LoremProvider):
    @classmethod
    def title(cls, nb_words=6, variable_nb_words=True):
        return cls.sentence(nb_words, variable_nb_words)[:-1]


factory.Faker.add_provider(ExtendedLoremProvider)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    is_published = False
    title = factory.Faker('title')
    slug = factory.LazyAttribute(lambda p: slugify(p.title))
    excerpt = factory.Faker('sentence', nb_words=20)
    body = factory.Faker('text', max_nb_chars=5000)

    @factory.lazy_attribute
    def published_at(self):
        return now() if self.is_published else None
