# Generated by Django 5.0.6 on 2024-05-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=500)),
                ('agree', models.IntegerField(default=0)),
                ('disagree', models.IntegerField(default=0)),
                ('agreeRate', models.DecimalField(decimal_places=4, default=0, max_digits=5)),
                ('disagreeRate', models.DecimalField(decimal_places=4, default=0, max_digits=5)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
