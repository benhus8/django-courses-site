import json

from django.contrib import messages
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Course, User_Course, Subject, Lesson
from rest_framework.decorators import api_view
from main.forms import RegistrationForm, EditUserDataForm


@login_required()
def index(request):
    return render(request, 'index.html')


def registerView(request):
    return render(request, 'index.html')


@require_POST
@csrf_exempt
def register(request):
    data = json.loads(request.body)
    form = RegistrationForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Registration successful'}, status=201)
    else:
        errors = {field: form.errors[field][0] for field in form.errors}
        response = JsonResponse({'errors': errors}, status=400)
        print(response.content.decode('utf-8'))
        return JsonResponse({'errors': errors}, status=400)

@api_view(['PUT'])
@login_required
def edit_user_data(request):
    data = json.loads(request.body)
    user = request.user
    form = EditUserDataForm(data, instance=user)
    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Edittion successful'}, status=201)
    else:
        errors = {field: form.errors[field][0] for field in form.errors}
        response = JsonResponse({'errors': errors}, status=400)
        print(response.content.decode('utf-8'))
        return JsonResponse({'errors': errors}, status=400)

class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('login')


@login_required
def get_user_data(request):
    user_data = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'birthday': str(request.user.birthday),
        'phone_number': request.user.phone_number,
        'address': request.user.address,
        'building_number': request.user.building_number,
        'postal_code': request.user.postal_code,
        'city': request.user.city,
    }
    return JsonResponse(user_data)


@login_required
def get_available_courses(request):
    user = request.user
    try:
        user_courses = User_Course.objects.filter(user=user)
        course_ids = [user_course.course_id for user_course in user_courses]

        courses = Course.objects.exclude(course_id__in=course_ids).values(
            'course_id',
            'description',
            'access_duration',
            'net_amount',
            'language_cd',
        )

        available_courses = []
        with connection.cursor() as cursor:
            for course in courses:
                course_id = course['course_id']
                cursor.execute('SELECT calculate_total_price(%s)', [course_id])
                total_price = cursor.fetchone()[0]
                course['total_price'] = total_price
                available_courses.append(course)

        return JsonResponse(available_courses, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def add_course_to_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            course_id = int(data.get('courseId'))

            course = Course.objects.get(course_id=course_id)

            User_Course.objects.create(user=request.user, course=course)

            return JsonResponse({'message': 'Course added successfully'})
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def delete_user_course(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            course_id = int(data.get('courseId'))
            user_id = request.user.id

            with connection.cursor() as cursor:
                # Call the stored procedure
                cursor.execute('CALL delete_main_user_course(%s, %s)', [course_id, user_id])

            return JsonResponse({'message': 'Course deleted successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': 'CSRF cookie set'})


@login_required
def get_user_courses(request):
    user = request.user
    try:
        user_courses = User_Course.objects.filter(user=user)
        course_ids = [user_course.course_id for user_course in user_courses]

        courses = Course.objects.filter(course_id__in=course_ids).values(
            'course_id',
            'description',
            'access_duration',
            'net_amount',
            'language_cd',
        )

        return JsonResponse(list(courses), safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def get_course_subjects(request, course_id):
    try:
        course = Course.objects.get(course_id=course_id)
        subjects = Subject.objects.filter(course=course)
        data = [{'id': subject.subject_id, 'title': subject.title, 'description': subject.seqence} for subject in
                subjects]
        return JsonResponse(data, safe=False)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)


@login_required
def get_subject_lessons(request, course_id, subject_id):
    try:
        course = Course.objects.get(course_id=course_id)
        subject = Subject.objects.get(subject_id=subject_id, course=course)
        lessons = Lesson.objects.filter(subject=subject)
        data = [{'id': lesson.lesson_id, 'description': lesson.description} for lesson in lessons]
        return JsonResponse(data, safe=False)
    except (Course.DoesNotExist, Subject.DoesNotExist):
        return JsonResponse({'error': 'Course or subject not found'}, status=404)


@login_required
def get_course_title(request, course_id):
    try:
        course = Course.objects.get(course_id=course_id)
        return JsonResponse({'title': course.description})
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
