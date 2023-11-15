import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from main.forms import RegistrationForm


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

