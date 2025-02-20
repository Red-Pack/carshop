from django.db import models

# Марка автомобиля
class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Марка")

    def __str__(self):
        return self.name

# Модель автомобиля (привязана к марке)
class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models", verbose_name="Марка")
    name = models.CharField(max_length=50, verbose_name="Модель")

    def __str__(self):
        return f"{self.name}"

# Основная модель автомобиля
class Car(models.Model):
    price = models.PositiveIntegerField(verbose_name="Цена")
    vin = models.CharField(max_length=17, unique=True, verbose_name="VIN")
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="Модель")
    is_new = models.BooleanField(default=False, verbose_name="Новая машина")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    owners = models.PositiveIntegerField(verbose_name="Количество владельцев")
    mileage = models.PositiveIntegerField(verbose_name="Пробег")

    BODY_TYPE_CHOICES = [
        ("седан", "Седан"),
        ("хэтчбек", "Хэтчбек"),
        ("универсал", "Универсал"),
        ("внедорожник", "Внедорожник"),
        ("купе", "Купе"),
    ]
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES, verbose_name="Тип кузова")

    TRANSMISSION_CHOICES = [
        ("MT", "механика"),
        ("AT", "автомат"),
        ("CVT", "вариатор"),
        ("DCT", "робот"),
    ]
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, verbose_name="КПП")

    DRIVE_CHOICES = [
        ("передний", "Передний"),
        ("задний", "Задний"),
        ("полный", "Полный"),
    ]
    drive = models.CharField(max_length=20, choices=DRIVE_CHOICES, verbose_name="Привод")

    WHEEL_CHOICES = [
        ("левый", "Левый"),
        ("правый", "Правый"),
    ]
    wheel = models.CharField(max_length=10, choices=WHEEL_CHOICES, verbose_name="Руль")

    color = models.CharField(max_length=20, verbose_name="Цвет")

    ENGINE_FUEL = [
        ("бензин", "Бензин"),
        ("дизель", "Дизель"),
        ("электричество", "Электричество"),
        ("гибрид", "Гибрид"),
    ]
    engine = models.CharField(max_length=20, choices=ENGINE_FUEL, verbose_name="Двигатель")

    engine_capacity = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Объем двигателя (л)")
    power_hp = models.PositiveIntegerField(verbose_name="Мощность (л.с.)")

    doors = models.PositiveIntegerField(verbose_name="Количество дверей")
    generation = models.CharField(max_length=50, verbose_name="Поколение")
    modification = models.CharField(max_length=50, verbose_name="Модификация")
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def get_mileage_display(self):
        return f"{int(self.mileage):,}".replace(",", " ")

    def get_price_display(self):
        return f"{int(self.price):,}".replace(",", " ")

    def __str__(self):
        return f"{self.model.brand.name} {self.model.name} ({self.year})"

# Фото автомобилей (несколько фото)
class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='cars/', verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return f"Фото {self.car.vin}"