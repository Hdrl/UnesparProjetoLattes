# Generated by Django 3.1.5 on 2021-07-07 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lattes', '0007_auto_20210707_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=45)),
                ('nomeCitacao', models.CharField(max_length=45)),
                ('idCNPQ', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ProducaoAutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordemAutoria', models.CharField(max_length=45)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Autores', to='lattes.autor')),
                ('producao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producoes', to='lattes.producao')),
            ],
        ),
        migrations.CreateModel(
            name='AreaConhecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grandeArea', models.CharField(max_length=45)),
                ('area', models.CharField(max_length=45)),
                ('subArea', models.CharField(max_length=45)),
                ('especialidade', models.CharField(max_length=45)),
                ('producaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AreasConhecimento', to='lattes.producao')),
            ],
        ),
    ]