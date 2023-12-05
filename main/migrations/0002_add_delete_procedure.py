from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE PROCEDURE delete_main_user_course(cId INTEGER, uId INTEGER)
            LANGUAGE SQL
            AS $$
              DELETE FROM main_user_course WHERE course_id = cId and user_id = uId;
            $$;
            """
        ),
    ]