# Generated by Django 2.0.1 on 2018-01-21 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('continent', models.CharField(choices=[('Asia', 'Asia'), ('Africa', 'Africa'), ('North_America', 'North America'), ('South_America', 'South America'), ('Antarctica', 'Antarctica'), ('Europe', 'Europe'), ('Australia', 'Australia')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Company')),
            ],
        ),
        migrations.AddField(
            model_name='country_products',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='company',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Country'),
        ),
    ]
