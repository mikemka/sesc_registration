from django.forms import ValidationError
from django.db import models


class BaseTemplate(models.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) >= 255:
            raise ValidationError(f'Длина текста ({len(name)}) превышает допустимые 255 символов!')
        return name

    class Meta():
        abstract = True
