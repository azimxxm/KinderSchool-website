# Generated by Django 3.2.7 on 2021-09-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallarey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Gallarey/%Y/%m/')),
            ],
            options={
                'verbose_name': 'Gallarey',
                'verbose_name_plural': 'Gallarey',
            },
        ),
    ]