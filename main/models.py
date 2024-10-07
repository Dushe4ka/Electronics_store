from django.db import models

NULLABLE = {"null": True, "blank": True}


class Link(models.Model):
    LEVEL_ZERO = 0
    LEVEL_FIRST = 1
    LEVEL_SECOND = 2
    LEVEL = [
        (LEVEL_ZERO, "завод"),
        (LEVEL_FIRST, "розничная сеть"),
        (LEVEL_SECOND, "Индивидуальный преприниматель")
    ]

    name = models.CharField(max_length=50, verbose_name="Название")
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")
    level = models.IntegerField(choices=LEVEL, verbose_name="Уровень сети")
    supplier = models.ForeignKey(
        "Link", on_delete=models.SET_NULL, verbose_name="Поставщик", **NULLABLE
    )
    arrears = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.name}, {self.email}, {self.country}"

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"


class Product(models.Model):

    name = models.CharField(max_length=250, verbose_name="Название продукта")
    product_model = models.CharField(max_length=250, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода")
    supplier = models.ForeignKey(
        Link, on_delete=models.CASCADE, verbose_name="Поставщик", related_name="products"
    )

    def __str__(self):
        return f"{self.name} - {self.product_model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
