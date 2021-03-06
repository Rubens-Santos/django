# Generated by Django 3.1 on 2020-08-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200815_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('recurso', models.CharField(max_length=100, verbose_name='Recurso')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-leaf', 'Folha'), ('lni-rocket', 'Foguete'), ('lni-layers', 'Layer'), ('lni-cog', 'Engrenagem'), ('lni-laptop-phone', 'Notbook')], max_length=17, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-stats-up', 'grafico'), ('lni-layers', 'Design'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuario'), ('lni-mobile', 'Molibe'), ('lni-cog', 'Engrenagem')], max_length=15, verbose_name='Icone'),
        ),
    ]
