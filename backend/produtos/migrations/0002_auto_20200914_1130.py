# Generated by Django 3.1 on 2020-09-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='camisa',
            options={'ordering': ['id'], 'verbose_name': 'Camisa', 'verbose_name_plural': 'Camisas'},
        ),
        migrations.AlterModelOptions(
            name='chuteira',
            options={'ordering': ['id'], 'verbose_name': 'Chuteira', 'verbose_name_plural': 'Chuteiras'},
        ),
        migrations.AddField(
            model_name='camisa',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='chuteira',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chuteira',
            name='tipo',
            field=models.CharField(max_length=100, verbose_name='Tipo'),
        ),
    ]
