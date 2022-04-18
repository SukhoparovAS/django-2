# Generated by Django 4.0.3 on 2022-04-08 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0007_alter_ssubscriber_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ssubscriber',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.AlterUniqueTogether(
            name='ssubscriber',
            unique_together={('user', 'category')},
        ),
    ]
