import factory

from . import models


class AuthorFactory(factory.Factory):
    class Meta:
        model = models.Author

    name = 'Joe'
    salutation = 'Blow'
    email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.name, a.salutation).lower())
