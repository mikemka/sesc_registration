from django.forms import ValidationError


def validate_true(value: bool):
    if not value:
        raise ValidationError('Это поле обязательно!')
