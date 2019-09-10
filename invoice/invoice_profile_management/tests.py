from .forms                         import Userform, EditUserForm
from django.test                    import TestCase
from django.contrib.auth.models     import User
from django.contrib.auth.forms      import UserCreationForm

class USER_TEST(TestCase):
    def setUp(self, username='NewUserName2', first_name='NewfirstName', last_name='NewLastName', email='zssq@gmail.com', password='passpasspass'):
        self.user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

    def test_user_creation_valid(self):
        a = self.user
        self.assertTrue(isinstance(a,User))

    def test_UF_valid(self):
        form = Userform({'username':"NewUserName",'first_name':"NewfirstName", 'last_name':"NewLastName", 'email':"zssq@gmail.com" , 'password':"passpasspass"})
        self.assertTrue(form.is_valid())
    def test_UF_invalid(self):
        form_1 = Userform({'first_name':"N1", 'last_name':"NL", 'email':"@" , 'password':"pass"})
        form_2 = Userform({'username':"N2",'first_name':"N", 'last_name':"NL", 'email':"@gmail" })
        form_3 = Userform({'username':"N3",'first_name':"", 'last_name':"NL", 'email':"@gmail" , 'password':"pass"})
        form_4 = Userform({'username':"N4",'first_name':"N", 'email':"@gmail" , 'password':"pass"})
        self.assertFalse(form_1.is_valid() or form_2.is_valid() or form_3.is_valid() or form_4.is_valid())

    def test_UF_valid(self):
        form = UserCreationForm({'username':"N5", 'password1':"passpasspass", 'password2':"passpasspass"})
        self.assertTrue(form.is_valid())
    def test_UF_invalid(self):
        form_1 = UserCreationForm({'username':"N6", 'password1':"pass", 'password2':"pass"})
        form_2 = UserCreationForm({'username':"N7", 'password':""})
        form_3 = UserCreationForm({'username':"", 'password':"pass"})
        self.assertFalse(form_1.is_valid() or form_2.is_valid() or form_3.is_valid())

    def test_EDT_F_valid(self):
        a = self.user
        form = EditUserForm({'first_name':a.first_name, 'last_name':a.last_name, 'email':a.email}, instance = self.user)
        self.assertTrue(form.is_valid())
    def test_EDT_F_invalid(self):
        a = self.user
        form_1 = EditUserForm({'email':"aemailwithoutdog"}, instance = self.user)
        self.assertFalse(form_1.is_valid())
