# Generated by Django 2.0.2 on 2018-05-28 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved', models.BooleanField(default=False)),
                ('table', models.IntegerField()),
                ('seat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SeatingRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
            options={
                'ordering': ['-number'],
            },
        ),
        migrations.AddField(
            model_name='seating',
            name='revision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seating.SeatingRevision'),
        ),
        migrations.AddField(
            model_name='seating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='seatingrevision',
            unique_together={('event', 'number')},
        ),
    ]
