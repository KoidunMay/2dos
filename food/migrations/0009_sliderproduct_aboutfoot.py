# Generated by Django 4.2.1 on 2023-05-27 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Aboutfoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.product')),
            ],
        ),
    ]
