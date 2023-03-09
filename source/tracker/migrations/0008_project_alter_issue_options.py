# Generated by Django 4.1.7 on 2023-03-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_alter_issue_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(null=True, verbose_name='Дата окончания')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
            ],
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]