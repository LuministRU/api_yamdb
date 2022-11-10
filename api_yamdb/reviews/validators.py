import re
from datetime import date

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_username(value):
    if value == 'me':
        raise ValidationError(
            ('Имя me недоступно!')
        )
    if re.search(r'^[\w.@+-]+$', value) is None:
        raise ValidationError(
            (f'Недопустимые символы в имени {value}!')
        )


def validate_year(self, value):
    year = date.today().year
    if value >= year:
        raise ValidationError('Укажите правильный год.')
    return value
