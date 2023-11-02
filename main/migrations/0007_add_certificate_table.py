from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_add_table_course'),
        ('main', '0002_add_user_tables'),
        ('main', '0003_add_asset_table'),
        ('main', '0004_add_exam_tables'),
        ('main', '0005_add_exam_exam_question_table'),
        ('main', '0006_add_lesson_tables')
    ]

    operations = [
        migrations.RunSQL(
            'CREATE TABLE IF NOT EXISTS main_certificate('
            'certificate_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'course_id  INTEGER NOT NULL,'
            'user_id  INTEGER NOT NULL,'
            'date_from  DATE NOT NULL,'
            'date_to  DATE,'
            'certificate_pdf_path  VARCHAR(100),'
            'title  VARCHAR(100) NOT NULL,'
            'description  VARCHAR(100) NOT NULL,'
            'CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES main_course(course_id),'
            'CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES main_user(user_id)'
            ');'
        )
    ]