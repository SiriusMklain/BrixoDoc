# Generated by Django 4.0.3 on 2022-07-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteBrixo', '0014_articleoem_manno_articleoem_sortno_articles_genartno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='BrandNo',
        ),
        migrations.AddField(
            model_name='suppliers',
            name='BrandNo',
            field=models.IntegerField(blank=True, null=True, verbose_name='BrandNo'),
        ),
    ]