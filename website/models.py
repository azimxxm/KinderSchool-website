from django.db import models
from django.db.models.deletion import CASCADE


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    work_type = models.CharField(max_length=50)
    telegram_url = models.URLField(blank=True)
    imstagram_url = models.URLField(blank=True)
    likedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="Teachers/%Y/%m/")

    class Meta:
        verbose_name = "O'qituvchilar"
        verbose_name_plural = "O'qituvchilar"

    def __str__(self):
        return self.name


class Age_Grupp(models.Model):
    age_grupp_name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Bolalar yoshi"
        verbose_name_plural = "Bolalar yoshi"

    def __str__(self):
        return self.age_grupp_name


class Class_blog(models.Model):
    class_name = models.CharField(max_length=100)
    class_type = models.CharField(max_length=100)
    number_of_classes = models.IntegerField(default=0)
    class_price = models.BigIntegerField(default=0)
    age_grupp = models.ManyToManyField(Age_Grupp)
    image = models.ImageField(upload_to="Class/%Y/%m/")

    class Meta:
        verbose_name = "Class_blog"
        verbose_name_plural = "Class_blog"

    def __str__(self):
        return self.class_name

class Gallarey(models.Model):
    image_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="Gallarey/%Y/%m/")
    url = models.URLField()

    class Meta:
        verbose_name = "Gallarey"
        verbose_name_plural = "Gallarey"

    def __str__(self):
        return self.image_name