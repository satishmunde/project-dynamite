# Generated by Django 4.2.4 on 2024-05-14 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="trainer",
            name="user_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="staff",
            name="gym",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="api.gym",
            ),
        ),
        migrations.AddField(
            model_name="staff",
            name="user_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="softwaremembership",
            name="gym_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.gym"
            ),
        ),
        migrations.AddField(
            model_name="membership",
            name="gym",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.gym"
            ),
        ),
        migrations.AddField(
            model_name="membership",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.member"
            ),
        ),
        migrations.AddField(
            model_name="membership",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.workoutplan"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="gym",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.gym"
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="user_name",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="gym",
            name="user_name",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="equipment",
            name="gym",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="api.gym",
            ),
        ),
    ]
