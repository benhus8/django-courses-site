from django.db import models
from django.utils.html import mark_safe
class Mentor(models.Model):
    mentor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'main_mentor'

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000)
    access_duration = models.IntegerField()
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    vat = models.DecimalField(max_digits=3, decimal_places=2)
    language_cd = models.CharField(max_length=2)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'main_course'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=100)
    building_number = models.CharField(max_length=10, null=True, blank=True)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'main_user'


class User_Course(models.Model):
    user_course_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'main_user_course'


class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='assets')

    class Meta:
        managed = False
        db_table = 'main_asset'

class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    max_score = models.IntegerField()
    passed = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'main_exam'


class User_Exam(models.Model):
    user_exam_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam')
    user = models.ForeignKey(Exam, on_delete=models.CASCADE , related_name='user')

    class Meta:
        managed = False
        db_table = 'main_user_exam'


class Exam_Question(models.Model):
    exam_question_id = models.AutoField(primary_key=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'main_exam_question'

class Exam_Question_Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    exam_question = models.ForeignKey(Exam_Question, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    correct = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'main_exam_question_answer'

class Exam_Exam_Question(models.Model):
    exam_exam_question_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    exam_question = models.ForeignKey(Exam_Question, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'main_exam_exam_question'

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    seqence = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'main_subject'

class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    seqence = models.CharField(max_length=1000, null=True, blank=True)
    short_description = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'main_lesson'

class Lesson_Content(models.Model):
    lesson_content_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    seqence = models.CharField(max_length=1000)
    content_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'main_lesson_content'

class Certificate(models.Model):
    certificate_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    certificate_pdf_path = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'main_certificate'