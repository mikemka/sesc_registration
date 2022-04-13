from django.db import models
from forms.validators import validate_true
from core.generators import generate_id


class BaseTemplate(models.Model):
    name = models.TextField('Имя ученика', null=False)
    subm = models.BooleanField('Согласен с условиями', default=False, validators=(validate_true, ))
    slug = models.CharField('Идентификатор', max_length=100, unique=True, default=generate_id())
    attached = models.BooleanField('Экспортировать', default=False)

    class Meta():
        abstract = True
