# Generated by Django 4.2.10 on 2024-02-24 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddAThingToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('category', models.CharField(choices=[('SHD', 'Should'), ('MST', 'Must'), ('NICE', 'It would be nice if')], max_length=4)),
                ('operation', models.CharField(blank=True, choices=[('+', 'Plus'), ('-', 'Minus')], default='+', max_length=1, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('operation', models.CharField(choices=[('+', 'Plus'), ('-', 'Minus')], max_length=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
