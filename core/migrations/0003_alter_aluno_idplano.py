# Generated by Django 4.0.1 on 2022-01-21 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_plano_options_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='idplano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.plano', verbose_name='Plano'),
        ),
    ]
