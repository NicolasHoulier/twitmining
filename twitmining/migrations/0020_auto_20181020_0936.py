# Generated by Django 2.1.2 on 2018-10-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitmining', '0019_relevanttweet_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('sample_size', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
    ]
