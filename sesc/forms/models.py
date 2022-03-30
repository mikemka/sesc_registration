from django.db import models
from . validators import validate_true
from core.generators import generate_id


class Gum(models.Model):
    name = models.TextField('Имя ученика', null=False)
    subm = models.BooleanField('Согласен с условиями', default=False, validators=(validate_true, ))
    slug = models.CharField('Идентификатор', max_length=100, unique=True, default=generate_id())

    d1 = models.BooleanField('Второй иностранный язык (Б)', default=False)
    d2 = models.BooleanField('География (Б)', default=False)
    d3 = models.BooleanField('Обществознание (Б)', default=False)
    d4 = models.BooleanField('Теория познания (Б)', default=False)
    d5 = models.BooleanField('Информатика (Б)', default=False)
    d6 = models.BooleanField('Естествознание (Б)', default=False)
    d7 = models.BooleanField('Диалоги с Чеховым', default=False)
    d8 = models.BooleanField('Современная литература в жанровом аспекте', default=False)
    d9 = models.BooleanField('Риторика', default=False)
    d10 = models.BooleanField('История философии', default=False)
    d11 = models.BooleanField('История мировой культуры', default=False)

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 гум'
    
    def __str__(self) -> str:
        return self.name
