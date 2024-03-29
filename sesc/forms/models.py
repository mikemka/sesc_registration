from django.db import models
from core.models import BaseTemplate


class Gum(BaseTemplate, models.Model):
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


class Sgum(BaseTemplate, models.Model):
    d1 = models.BooleanField('География (Б)', default=False)
    d2 = models.BooleanField('Теория познания (Б)', default=False)
    d3 = models.BooleanField('МХК (Б)', default=False)
    d4 = models.BooleanField('Информатика (Б)', default=False)
    d5 = models.BooleanField('Естествознание (Б)', default=False)
    d6 = models.BooleanField('Зарубежная литература', default=False)
    d7 = models.BooleanField('Современная литература в жанровом аспекте', default=False)
    d8 = models.BooleanField('Диалоги с Чеховым', default=False)
    d9 = models.BooleanField('Политология', default=False)
    d10 = models.BooleanField('Социология', default=False)
    d11 = models.BooleanField('История философии', default=False)

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 соцгум'
    
    def __str__(self) -> str:
        return self.name


class SocEk(BaseTemplate, models.Model):
    d1 = models.BooleanField('Теория познания (Б)', default=False)
    d2 = models.BooleanField('МХК (Б)', default=False)
    d3 = models.BooleanField('География (Б)', default=False)
    d4 = models.BooleanField('Информатика (Б)', default=False)
    d5 = models.BooleanField('Естествознание (Б)', default=False)
    d6 = models.BooleanField('Экономическая география', default=False)
    d7 = models.BooleanField('История философии ', default=False)
    d8 = models.BooleanField('Сложные математические задачи', default=False)

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 соцэк'
    
    def __str__(self) -> str:
        return self.name


class MatInf(BaseTemplate, models.Model):
    d1 = models.BooleanField('Обществознание (Б)', default=False)
    d2 = models.BooleanField('География (Б)', default=False)
    d3 = models.BooleanField('МХК (Б)', default=False)
    d4 = models.BooleanField('Теория познания (Б)', default=False)
    d5 = models.BooleanField('Биология (Б)', default=False)
    d6 = models.BooleanField('Физика (Б)', default=False)
    d7 = models.BooleanField('Химия (Б)', default=False)
    d8 = models.BooleanField('Избранные главы учебников естественных наук', default=False)

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 матинф'
    
    def __str__(self) -> str:
        return self.name


class FizMat(BaseTemplate, models.Model):
    d1 = models.BooleanField('Обществознание (Б)', default=False)
    d2 = models.BooleanField('География (Б)', default=False)
    d3 = models.BooleanField('МХК (Б)', default=False)
    d4 = models.BooleanField('Теория познания (Б)', default=False)
    d5 = models.BooleanField('Биология (Б)', default=False)
    d6 = models.BooleanField('Химия (Б)', default=False)
    d7 = models.BooleanField('Астрономия', default=False)
    d8 = models.BooleanField('Избранные главы учебников естественных наук', default=False)

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 физмат'
    
    def __str__(self) -> str:
        return self.name


class FizTech(BaseTemplate, models.Model):
    d1 = models.BooleanField('Обществознание (Б)', default=False)
    d2 = models.BooleanField('География (Б)', default=False)
    d3 = models.BooleanField('МХК (Б)', default=False)
    d4 = models.BooleanField('Теория познания (Б)', default=False)
    d5 = models.BooleanField('Биология (Б)', default=False)
    d6 = models.BooleanField('Химия (Б)', default=False)
    d7 = models.BooleanField('Инженерная графика (геометрическое и проекционное черчение)', default=False)
    d8 = models.BooleanField('Астрономия', default=False)
    d9 = models.BooleanField('Избранные главы учебников естественных наук', default=False)

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 физтех'
    
    def __str__(self) -> str:
        return self.name


class Him(BaseTemplate, models.Model):
    d1 = models.BooleanField('Обществознание (Б)', default=False)
    d2 = models.BooleanField('География (Б)', default=False)
    d3 = models.BooleanField('МХК (Б)', default=False)
    d4 = models.BooleanField('Теория познания (Б)', default=False)
    d5 = models.BooleanField('Информатика (Б)', default=False)
    d6 = models.BooleanField('Биология (Б)', default=False)
    d7 = models.BooleanField('Решение сложных задач по математике', default=False)
    d8 = models.BooleanField('Физические задачи повышенной сложности', default=False)
    d9 = models.BooleanField('Биологические задачи', default=False)
    d10 = models.BooleanField('Химический практикум', default=False)
    d11 = models.BooleanField('Астрономия', default=False)

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 хим'
    
    def __str__(self) -> str:
        return self.name


class Bio(BaseTemplate, models.Model):
    d1 = models.BooleanField('Обществознание (Б)', default=False)
    d2 = models.BooleanField('География (Б)', default=False)
    d3 = models.BooleanField('МХК (Б)', default=False)
    d4 = models.BooleanField('Теория познания (Б)', default=False)
    d5 = models.BooleanField('Информатика (Б)', default=False)
    d6 = models.BooleanField('Физика (Б)', default=False)
    d7 = models.BooleanField('Решение сложных задач по математике', default=False)
    d8 = models.BooleanField('Информатика в задачах', default=False)
    d9 = models.BooleanField('Сложные вопросы ботаники, зоологии, анатомии', default=False)
    d10 = models.BooleanField('Химические задачи повышенной сложности', default=False)
    d11 = models.BooleanField('Биологический практикум', default=False)

    class Meta():
        verbose_name = 'ученик'
        verbose_name_plural = '10 био'
    
    def __str__(self) -> str:
        return self.name
