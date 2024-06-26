# Generated by Django 5.0.4 on 2024-04-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='photo/')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='permanent_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='present_address',
            field=models.CharField(max_length=200),
        ),
    ]
