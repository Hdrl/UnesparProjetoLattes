# Generated by Django 3.1.5 on 2021-05-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lattes', '0003_delete_pessoas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('campus', models.CharField(max_length=255)),
                ('tipoVinculo', models.CharField(max_length=255)),
                ('formacao', models.CharField(max_length=255)),
                ('instituicaoEmQueSeFormou', models.CharField(max_length=255)),
                ('anoQueIngressouNoCampus', models.IntegerField()),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
    ]
