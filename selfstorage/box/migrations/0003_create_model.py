# Generated by Django 3.2 on 2021-11-26 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('box', '0002_box_place_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('things_names', models.CharField(max_length=200, verbose_name='названия вещей')),
                ('number_of_things', models.PositiveIntegerField(default=1, verbose_name='кол-во единиц вещей')),
                ('storage_address', models.TextField(default='ул. Манчестерская, д. 7, кв. 1', verbose_name='адрес склада')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
