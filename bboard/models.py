from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models

is_all_posts_passive = True


def is_active_default():
    return is_all_posts_passive


def validate_even(val):
    if val % 2 != 0:
        raise ValidationError("Число %(value)s нечет", code="odd", params={"value": val})

class MinMaxValueValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val):
        if val < self.min_value or val > self.max_value:
            raise  ValidationError("Введённое число должно находится в диапозоне от %(min) до %(max)s"),
        code = "out_of_range",
        params = {"min": self.min_value, "max": self.max_value}


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return f"/{self.pk}/"

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


class Bb(models.Model):
    rubric = models.ForeignKey("Rubric", null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика')
    title = models.CharField(
        max_length=50,
        verbose_name="Товар",
        # validators=[validators.RegexValidator(regex='^.{4,}$')]
        # validators=[validators.MinLengthValidator(4)]
        validators=[validate_even]
    )
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена", default=0)
    is_active = models.BooleanField(default=is_active_default)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    updated = models.DateTimeField(auto_now=True, db_index=True, verbose_name="Изменено")

    def __str__(self):
        return f'{self.title}'

    def clean(self):
        errors = {}
        if not self.content:
            errors["content"] = ValidationError("Укажите описание продоваемого товара")
        if self.price and self.price < 0:
            errors["price"] = ValidationError("Укажите не отрицательное значние цены")

        if errors:
            raise ValidationError(errors)


    def title_a_price(self):
        if self.price:
            return f'{self.title} ({self.price:.2f})'
        return self.title

    # title_a_price.short_description = "Название и цена"

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published', 'title']
