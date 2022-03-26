from django.forms import ValidationError


def validate_one(value: int):
    if value < 0 or 1 < value:
        raise ValidationError('Число не ≤ 1')


def validate_two(value: int):
    if value < 0 or 2 < value:
        raise ValidationError('Число не ≤ 2')


def validate_three(value: int):
    if value < 0 or 3 < value:
        raise ValidationError('Число не ≤ 3')


def validate_ten(value: int):
    if value < 0 or 10 < value:
        raise ValidationError('Число не ≤ 10')


def validate_true(value: bool):
    if not value:
        raise ValidationError('Это поле обязательно!')
