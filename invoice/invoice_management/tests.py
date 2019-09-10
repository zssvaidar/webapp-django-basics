from django.test                          import TestCase
from django.contrib.auth.models           import User
from .models                              import iv_items, iv_item_specification
from .forms                               import ItemForm
from invoice_management.models            import iv_customer, iv_cart
from invoice_profile_management.forms     import CustomerForm

class ITEM_TEST(TestCase):
    def setUp(self, qr="1KK1", product_name="watchines", quantitity=1, price=1):
        specification = iv_item_specification.objects.create(name="chemical")
        self.iv_item = iv_items.objects.create(specification_fk=specification, qr=qr, product_name=product_name, quantitity=quantitity, price=price)
    def test_IF(self):
        form = ItemForm({})
        self.assertFalse(form_1.is_valid())

class CUSTOMER_TEST(TestCase):
    def setUp(self, business_name="nme", business_email="eml", business_address="dist", city="alm", country="kaz", fax="1K"):
       u = User.objects.create(username='N2', first_name='NF', last_name='NL', email='@gmail', password='pass')
       self.customer = iv_customer.objects.create(user=u, business_name=business_name, business_email=business_email, business_address=business_address, city=city, country=country, fax=fax)

    def test_C_CRT(self):
        c = self.customer
        self.assertTrue(isinstance(c,iv_customer))

    def test_C_F_valid(self):
        form = CustomerForm({'business_name':"luke", 'business_email':"skywalker@gg", 'business_address':"VIctory", 'city':"alm", 'country':"kaz", 'fax':"1KK1"})
        self.assertTrue(form.is_valid())
    def test_C_F_invalid(self):
        form_1 = CustomerForm({'business_email':"skywalker@gg", 'business_address':"VIctory", 'city':"alm", 'country':"kaz", 'fax':"1KK1"})
        form_2 = CustomerForm({'business_address':"V8D1", 'city':"alm", 'country':"kaz", 'fax':"1KK1"})
        form_3 = CustomerForm({'city':"alm", 'country':"kaz", 'fax':"1KK1"})
        self.assertFalse(form_1.is_valid())
        self.assertFalse(form_2.is_valid())
        self.assertFalse(form_3.is_valid())
