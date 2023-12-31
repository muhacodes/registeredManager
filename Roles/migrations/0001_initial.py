# Generated by Django 5.0 on 2023-12-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('about', models.TextField()),
                ('role_type', models.CharField(choices=[('contact', 'Contact'), ('permanent', 'Permanent')], max_length=10)),
                ('info', models.TextField()),
                ('created_at', models.DateField()),
            ],
        ),
    ]
