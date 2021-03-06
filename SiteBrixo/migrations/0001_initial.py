# Generated by Django 4.0.3 on 2022-08-03 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExternalId', models.CharField(blank=True, max_length=255, null=True, verbose_name='ExternalId')),
                ('AssemblyGroup', models.CharField(blank=True, max_length=255, null=True, verbose_name='AssemblyGroup')),
                ('GenericArticle', models.CharField(blank=True, max_length=255, null=True, verbose_name='GenericArticle')),
                ('ArticleNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='ArticleNumber')),
                ('Type', models.IntegerField(blank=True, null=True, verbose_name='Type')),
                ('GenericArticleNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='GenericArticleNumber')),
                ('Attributes', models.JSONField(blank=True, null=True, verbose_name='Attributes')),
                ('Gtin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Gtin')),
                ('GenArtNo', models.IntegerField(blank=True, null=True, verbose_name='GenArtNo')),
                ('StatusDat', models.IntegerField(blank=True, null=True, verbose_name='StatusDat')),
            ],
        ),
        migrations.CreateModel(
            name='DisplayBra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bra_brand_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='bra_brand_no')),
                ('bra_short_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='bra_short_name')),
                ('view_term_plain', models.CharField(blank=True, max_length=255, null=True, verbose_name='view_term_plain')),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('BrandNo', models.IntegerField(blank=True, null=True, verbose_name='BrandNo')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'default_related_name': 'VehicleBrands',
            },
        ),
        migrations.CreateModel(
            name='VehicleModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('ModelNumber', models.IntegerField(blank=True, null=True, verbose_name='ModelNumber')),
                ('VehicleBrandId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VehicleModels', to='SiteBrixo.vehiclebrands')),
            ],
            options={
                'default_related_name': 'VehicleModels',
            },
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeNumber', models.IntegerField(blank=True, null=True, verbose_name='TypeNumber')),
                ('Year', models.CharField(blank=True, max_length=255, null=True, verbose_name='Year')),
                ('BodyType', models.CharField(blank=True, max_length=255, null=True, verbose_name='BodyType')),
                ('DriveType', models.CharField(blank=True, max_length=255, null=True, verbose_name='DriveType')),
                ('EngineType', models.CharField(blank=True, max_length=255, null=True, verbose_name='EngineType')),
                ('ValvesPerChamber', models.IntegerField(blank=True, null=True, verbose_name='ValvesPerChamber')),
                ('Cylinders', models.IntegerField(blank=True, null=True, verbose_name='Cylinders')),
                ('Volume', models.IntegerField(blank=True, null=True, verbose_name='Volume')),
                ('CcmTech', models.IntegerField(blank=True, null=True, verbose_name='CcmTech')),
                ('FuelType', models.CharField(blank=True, max_length=255, null=True, verbose_name='FuelType')),
                ('FuelMixtureFormation', models.CharField(blank=True, max_length=255, null=True, verbose_name='FuelMixtureFormation')),
                ('HorsePowers', models.CharField(blank=True, max_length=255, null=True, verbose_name='HorsePowers')),
                ('KiloWatts', models.CharField(blank=True, max_length=255, null=True, verbose_name='KiloWatts')),
                ('Engines', models.CharField(blank=True, max_length=255, null=True, verbose_name='Engines')),
                ('TypeName', models.CharField(blank=True, max_length=255, null=True, verbose_name='TypeName')),
                ('VehicleModelId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Vehicles', to='SiteBrixo.vehiclemodels')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TradeNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='TradeNo')),
                ('FirstPage', models.IntegerField(blank=True, null=True, verbose_name='FirstPage')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('Article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Articl', to='SiteBrixo.articles')),
            ],
        ),
        migrations.CreateModel(
            name='Supers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SupersNo', models.CharField(blank=True, max_length=255, null=True, verbose_name='CountryCode')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('Article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Article', to='SiteBrixo.articles')),
            ],
        ),
        migrations.CreateModel(
            name='Marketplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.IntegerField(blank=True, null=True, verbose_name='Type')),
                ('OzonId', models.IntegerField(blank=True, null=True, verbose_name='OzonId')),
                ('ArticleId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Marketplaces', to='SiteBrixo.articles')),
            ],
        ),
        migrations.CreateModel(
            name='LnkTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LnkTargetType', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetType')),
                ('LnkTargetNo', models.IntegerField(blank=True, null=True, verbose_name='LnkTargetNo')),
                ('SeqNo', models.IntegerField(blank=True, null=True, verbose_name='SeqNo')),
                ('Article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Art', to='SiteBrixo.articles')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Path', models.CharField(blank=True, max_length=255, null=True, verbose_name='Path')),
                ('Order', models.CharField(blank=True, max_length=255, null=True, verbose_name='Order')),
                ('ArticleId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='File', to='SiteBrixo.articles')),
                ('VehicleId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='File', to='SiteBrixo.vehicles')),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocNo', models.IntegerField(blank=True, null=True, verbose_name='DocNo')),
                ('LangNo', models.IntegerField(blank=True, null=True, verbose_name='LangNo')),
                ('DocName', models.CharField(blank=True, max_length=255, null=True, verbose_name='DocName')),
                ('DocContentType', models.IntegerField(blank=True, null=True, verbose_name='DocContentType')),
                ('DocTermNorm', models.IntegerField(blank=True, null=True, verbose_name='DocTermNorm')),
                ('DocType', models.IntegerField(blank=True, null=True, verbose_name='DocType')),
                ('Article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Arti', to='SiteBrixo.articles')),
            ],
        ),
        migrations.CreateModel(
            name='Crit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CritNo', models.IntegerField(blank=True, null=True, verbose_name='CritNo')),
                ('CritVal', models.CharField(blank=True, max_length=255, null=True, verbose_name='CritVal')),
                ('FirstPage', models.IntegerField(blank=True, null=True, verbose_name='FirstPage')),
                ('Article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Artic', to='SiteBrixo.articles')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryCode', models.CharField(blank=True, max_length=255, null=True, verbose_name='CountryCode')),
                ('Article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Articles', to='SiteBrixo.articles')),
            ],
        ),
        migrations.CreateModel(
            name='ArticlesToVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Criterias', models.CharField(blank=True, max_length=255, null=True, verbose_name='Criterias')),
                ('ExternalId', models.CharField(blank=True, max_length=255, null=True, verbose_name='ExternalId')),
                ('ArticleId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArticlesToVehicle', to='SiteBrixo.articles')),
                ('VehicleId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArticlesToVehicle', to='SiteBrixo.vehicles')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='SupplierId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Articles', to='SiteBrixo.suppliers'),
        ),
        migrations.CreateModel(
            name='ArticleOem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='Brand')),
                ('OemNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='OemNumber')),
                ('IsOriginal', models.IntegerField(blank=True, null=True, verbose_name='IsOriginal')),
                ('NormalizerOemNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='NormalizerOemNumber')),
                ('IsReplacer', models.IntegerField(blank=True, null=True, verbose_name='IsReplacer')),
                ('ManNo', models.IntegerField(blank=True, null=True, verbose_name='ManNo')),
                ('SortNo', models.IntegerField(blank=True, null=True, verbose_name='SortNo')),
                ('ArticleId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArticleOem', to='SiteBrixo.articles')),
            ],
        ),
    ]
