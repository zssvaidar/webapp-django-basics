from django.shortcuts import render
from .models import Deck, User
# Create your views here.
def registerForm(request):
    qs = Deck.objects.all()
    context = {'decks': qs}
    return render(request, 'flashcards/registerForm.html', context)
def createUser(request):
    if(request.method == 'POST'):
        print("*******THAT IS IT*********")
        first_name_input = request.POST.get('first_name', None)
        last_name_input = request.POST.get('last_name', None)
        password_input = request.POST.get('password', None)
        confirm_password_input = request.POST.get('confirm_password', None)
        email_input = request.POST.get('email', None)
        phone_number_input = request.POST.get('phone_number', None)
        new_User = User(first_name = first_name_input, last_name = last_name_input,
        password = password_input, confirm_password = confirm_password_input,
        email = email_input, phone_number = phone_number_input)
        new_User.save()
    context = {}
    return render(request, 'flashcards/registerForm.html', context)
