# Generated by Django 4.2.6 on 2023-10-29 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_add_table_course'),
    ]

    operations = [
        migrations.RunSQL(
            'CREATE TABLE IF NOT EXISTS main_user ('
            'user_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'first_name  VARCHAR(100) NOT NULL,'
            'last_name  VARCHAR(100) NOT NULL,'
            'birthday  DATE NOT NULL,'
            'phone_number  VARCHAR(12),'
            'address VARCHAR(100) NOT NULL,'
            'building_number VARCHAR(10),'
            'postal_code VARCHAR(6) NOT NULL,'
            'city VARCHAR(10) NOT NULL'
            ');'
            
            'CREATE TABLE IF NOT EXISTS main_user_course('
            'user_course_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,'
            'course_id  INTEGER NOT NULL,'
            'user_id  INTEGER NOT NULL,'
            'CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES main_course(course_id),'
            'CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES main_user(user_id)'
            ');'
        )
    ]