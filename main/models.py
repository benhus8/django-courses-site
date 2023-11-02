from django.db import models


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000)
    access_duration = models.IntegerField()
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    vat = models.DecimalField(max_digits=3, decimal_places=2)
    language_cd = models.CharField(max_length=2)


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


class UserCourse(models.Model):
    user_course_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    image = models.BinaryField()


class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    score = models.IntegerField()
    max_score = models.IntegerField()
    passed = models.BooleanField(default=False)


class UserExam(models.Model):
    user_exam_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam')
    user = models.ForeignKey(Exam, on_delete=models.CASCADE , related_name='user')


class ExamQuestion(models.Model):
    exam_question_id = models.AutoField(primary_key=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)


class ExamQuestionAnswer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    exam_question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    correct = models.BooleanField()