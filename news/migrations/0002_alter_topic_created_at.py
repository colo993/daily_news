# Generated by Django 5.2.3 on 2025-07-23 12:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('news', '0001_initial'),
	]

	operations = [
		migrations.AlterField(
			model_name='topic',
			name='created_at',
			field=models.DateTimeField(
				default=django.utils.timezone.now, verbose_name='creation date'
			),
		),
	]
