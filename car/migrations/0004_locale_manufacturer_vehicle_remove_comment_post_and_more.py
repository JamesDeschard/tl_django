# Generated by Django 4.1.2 on 2022-10-10 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_car_engine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=100)),
                ('car_name', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('model_year', models.IntegerField()),
                ('serial_number', models.CharField(max_length=100)),
                ('date_auctioned', models.DateField()),
                ('original_price', models.IntegerField()),
                ('adjusted_price', models.IntegerField()),
                ('wikipedia_profile', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='engine',
            name='car',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RenameModel(
            old_name='Car',
            new_name='AuctionHouse',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Engine',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='auction_house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.auctionhouse'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='locale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.locale'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.manufacturer'),
        ),
    ]
