# Generated by Django 4.0.6 on 2022-07-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.EmailField(max_length=254)),
            ],
        ),
    ]
