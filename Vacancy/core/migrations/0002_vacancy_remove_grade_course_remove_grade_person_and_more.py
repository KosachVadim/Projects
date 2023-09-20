# Generated by Django 4.2.5 on 2023-09-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('salary_range', models.CharField(max_length=255)),
                ('manager_account', models.CharField(max_length=255)),
                ('profit_type', models.CharField(max_length=255)),
                ('profit_amount', models.FloatField()),
                ('working_conditions', models.TextField()),
                ('contact_person', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='grade',
            name='course',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='person',
        ),
        migrations.RemoveField(
            model_name='person',
            name='courses',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]