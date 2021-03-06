# Generated by Django 2.2 on 2019-05-17 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='FileVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='versions', to='user.User')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='file.File')),
            ],
        ),
    ]
