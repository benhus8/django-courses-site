from django.db import migrations
class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_add_table_course'),
        ('main', '0002_add_user_tables'),
        ('main', '0003_add_asset_table'),
        ('main', '0004_add_exam_tables'),
        ('main', '0005_add_exam_exam_question_table'),
        ('main', '0006_add_lesson_tables'),
        ('main', '0007_add_certificate_table')
    ]

    operations = [
        migrations.RunSQL(
            'CREATE TABLE IF NOT EXISTS main_mentor ('
            'mentor_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'first_name  VARCHAR(100) NOT NULL,'
            'last_name  VARCHAR(100) NOT NULL,'
            'birthday DATE NOT NULL,'
            'email  VARCHAR(100) NOT NULL,'
            'phone_number  VARCHAR(12)'
            ');'
        )
    ]