# Generated by Django 2.2.7 on 2019-11-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrows', '0011_auto_20191127_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='dtDevolucao',
            field=models.DateField(null=True),
        ),
    ]