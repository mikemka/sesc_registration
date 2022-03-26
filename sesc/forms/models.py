from django.db import models
from . validators import validate_one, validate_two, validate_three, validate_true, validate_ten
from core.generators import generate_id


class Gum(models.Model):
    name = models.TextField(verbose_name='Имя ученика', null=False)
    subm = models.BooleanField(verbose_name='Согласен с условиями', default=False, validators=(validate_true, ))
    slug = models.CharField(max_length=100, unique=True, verbose_name='ID', default=generate_id())
    d1 = models.PositiveSmallIntegerField(verbose_name='Второй иностранный язык 10', default=0, validators=(validate_two, ))
    d2 = models.PositiveSmallIntegerField(verbose_name='Второй иностранный язык 11', default=0, validators=(validate_two, ))
    d3 = models.PositiveSmallIntegerField(verbose_name='География 10', default=0, validators=(validate_one, ))
    d4 = models.PositiveSmallIntegerField(verbose_name='География 11', default=0, validators=(validate_one, ))
    d5 = models.PositiveSmallIntegerField(verbose_name='Обществознание 10', default=0, validators=(validate_two, ))
    d6 = models.PositiveSmallIntegerField(verbose_name='Обществознание 11', default=0, validators=(validate_two, ))
    d7 = models.PositiveSmallIntegerField(verbose_name='Теория познания 10', default=0, validators=(validate_one, ))
    d8 = models.PositiveSmallIntegerField(verbose_name='Теория познания 11', default=0, validators=(validate_one, ))
    d9 = models.PositiveSmallIntegerField(verbose_name='Информатика 10', default=0, validators=(validate_one, ))
    d10 = models.PositiveSmallIntegerField(verbose_name='Информатика 11', default=0, validators=(validate_one, ))
    d11 = models.PositiveSmallIntegerField(verbose_name='Естествознание 10', default=0, validators=(validate_three, ))
    d12 = models.PositiveSmallIntegerField(verbose_name='Естествознание 11', default=0, validators=(validate_three, ))
    d13 = models.PositiveSmallIntegerField(verbose_name='Зарубежная литература 10', default=0, validators=(validate_two, ))
    d14 = models.PositiveSmallIntegerField(verbose_name='Зарубежная литература 11', default=0, validators=(validate_two, ))
    d15 = models.PositiveSmallIntegerField(verbose_name='Диалоги с Чеховым 10', default=0, validators=(validate_one, ))
    d16 = models.PositiveSmallIntegerField(verbose_name='Диалоги с Чеховым 11', default=0, validators=(validate_one, ))
    d17 = models.PositiveSmallIntegerField(verbose_name='Современная литература в жанровом аспекте 10', default=0, validators=(validate_one, ))
    d18 = models.PositiveSmallIntegerField(verbose_name='Современная литература в жанровом аспекте 11', default=0, validators=(validate_one, ))
    d19 = models.PositiveSmallIntegerField(verbose_name='Риторика 10', default=0, validators=(validate_one, ))
    d20 = models.PositiveSmallIntegerField(verbose_name='Риторика 11', default=0, validators=(validate_one, ))
    d21 = models.PositiveSmallIntegerField(verbose_name='Сложные аспекты истории России c древнейших времен до конца XIX века 10', default=0, validators=(validate_two, ))
    d22 = models.PositiveSmallIntegerField(verbose_name='Сложные аспекты истории России c древнейших времен до конца XIX века 11', default=0, validators=(validate_two, ))
    d23 = models.PositiveSmallIntegerField(verbose_name='История философии 10', default=0, validators=(validate_two, ))
    d24 = models.PositiveSmallIntegerField(verbose_name='История философии 11', default=0, validators=(validate_two, ))
    d25 = models.PositiveSmallIntegerField(verbose_name='История мировой культуры 10', default=0, validators=(validate_two, ))
    d26 = models.PositiveSmallIntegerField(verbose_name='История мировой культуры 11', default=0, validators=(validate_two, ))
    d27 = models.PositiveSmallIntegerField(verbose_name='Внеурочная деятельность 10', default=0, validators=(validate_ten, ))
    d28 = models.PositiveSmallIntegerField(verbose_name='Внеурочная деятельность 11', default=0, validators=(validate_ten, ))

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 гум'
    
    def __str__(self) -> str:
        return self.name
