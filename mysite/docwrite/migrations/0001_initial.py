# Generated by Django 3.1 on 2020-08-18 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DocValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_date', models.DateField()),
                ('part_name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('seat_no', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('ar_no', models.IntegerField()),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docwrite.document')),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docwrite.doctype')),
            ],
        ),
    ]
