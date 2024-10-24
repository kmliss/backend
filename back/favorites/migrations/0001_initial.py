# Generated by Django 5.1.2 on 2024-10-22 13:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users')),
            ],
            options={
                'unique_together': {('user_id', 'event_id')},
            },
        ),
        migrations.CreateModel(
            name='ViewedEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users')),
            ],
            options={
                'unique_together': {('user_id', 'event_id')},
            },
        ),
    ]
