from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_add_table_course'),
        ('main', '0002_add_user_tables'),
        ('main', '0003_add_asset_table'),
        ('main', '0004_add_exam_tables'),
        ('main', '0005_add_exam_exam_question_table'),
        ('main', '0006_add_lesson_tables'),
        ('main', '0007_add_certificate_table'),
        ('main', '0008_add_mentor_table')
    ]

    operations = [
        migrations.RunSQL(
            'ALTER TABLE main_course '
            'ADD COLUMN mentor_id INTEGER NOT NULL;'

            'ALTER TABLE main_course '
            'ADD CONSTRAINT fk_mentor '
            'FOREIGN KEY (mentor_id) REFERENCES main_mentor(mentor_id);'
        )
    ]