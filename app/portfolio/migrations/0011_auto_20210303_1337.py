# Generated by Django 3.1.7 on 2021-03-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_project_ongoing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('email', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('subject', models.TextField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, max_length=5000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-completion_date']},
        ),
    ]
