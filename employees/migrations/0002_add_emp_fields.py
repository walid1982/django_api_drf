from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="emp_id",
            field=models.CharField(max_length=20, default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="employee",
            name="emp_name",
            field=models.CharField(max_length=50, default=""),
            preserve_default=False,
        ),
    ]
