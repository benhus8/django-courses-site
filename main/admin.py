from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.utils.safestring import mark_safe
from base64 import b64encode
import os
from django.conf import settings
from .models import Mentor, Course, User, User_Course, Asset, Exam, User_Exam, Exam_Question, Exam_Question_Answer, Exam_Exam_Question, Subject, Lesson, Lesson_Content, Certificate

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('mentor_id','first_name', 'last_name', 'birthday', 'email', 'phone_number')
    search_fields = ('mentor_id','first_name', 'last_name', 'birthday', 'email', 'phone_number')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id','description', 'access_duration', 'net_amount', 'vat', 'language_cd', 'mentor')
    search_fields =  ('course_id','description', 'access_duration', 'net_amount', 'vat', 'language_cd', 'mentor')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'birthday', 'phone_number', 'address', 'building_number', 'postal_code', 'city')
    search_fields = ('id','first_name', 'last_name', 'birthday', 'phone_number', 'address', 'building_number', 'postal_code', 'city')

@admin.register(User_Course)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user_course_id','course', 'user')
    search_fields = ('user_course_id','course', 'user')

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_id', 'img_preview')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_id','score', 'max_score', 'passed','course')
    search_fields = ('exam_id','score', 'max_score', 'passed','course')

@admin.register(User_Exam)
class UserExamAdmin(admin.ModelAdmin):
    list_display = ('user_exam_id','exam', 'user')
    search_fields = ('user_exam_id','exam', 'user')

@admin.register(Exam_Question)
class ExamQuestionAdmin(admin.ModelAdmin):
    list_display = ('exam_question_id', 'asset','description')
    search_fields = ('exam_question_id', 'asset','description')

@admin.register(Exam_Question_Answer)
class ExamQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id','exam_question','asset', 'description', 'correct')
    search_fields = ('answer_id','exam_question','asset', 'description', 'correct')

@admin.register(Exam_Exam_Question)
class ExamExamQuestionAdmin(admin.ModelAdmin):
    list_display = ('exam_exam_question_id','exam', 'exam_question')
    search_fields = ('exam_exam_question_id','exam', 'exam_question')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_id','course', 'title','seqence')
    search_fields = ('subject_id','course', 'title','seqence')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_id','subject', 'seqence', 'short_description', 'description')
    search_fields = ('lesson_id','subject', 'seqence', 'short_description', 'description')

@admin.register(Lesson_Content)
class LessonContentAdmin(admin.ModelAdmin):
    list_display = ('lesson_content_id','lesson', 'asset', 'seqence', 'content_type')
    search_fields = ('lesson_content_id','lesson', 'asset', 'seqence', 'content_type')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_id','course', 'user', 'date_from', 'date_to','certificate_pdf_path', 'title', 'description')
    search_fields = ('certificate_id','course', 'user', 'date_from', 'date_to','certificate_pdf_path', 'title', 'description')

