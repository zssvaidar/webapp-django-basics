from                  django.shortcuts  import render, redirect
from        django.contrib.auth.models  import User
from                         django.db  import transaction
from                           .models  import iv_items, iv_item_specification, iv_cart, iv_customer
from  invoice_profile_management.forms  import CartForm
from                            .forms  import ItemForm, SpecificationForm

def main_V(request):
        items = iv_items.objects.all()
        specifications = iv_item_specification.objects.all()
        cartform = CartForm()
        return render(request, 'invoice_management/invoice_main.html', {'goods' : items,'specifications' : specifications,'cartform' : cartform,})

def inv_GET(request, item_id):

        item_item = iv_items.objects.all().order_by("id")[0]
        item_id = item_id  - item_item.id

        if(request.method == 'POST'):
            cartform = CartForm(request.POST)
            current_user_id = request.user.id
            if(cartform.is_valid()):
                quantitity = cartform.cleaned_data["quantitity"]
                user_fk = iv_customer.objects.get(user = current_user_id)
                item_fk = iv_items.objects.all()[item_id]
                cart = iv_cart(customer_fk = user_fk, item_fk = item_fk, quantitity = quantitity)
                cart.save()
                return redirect ('invoices_page')

        return redirect ('invoices_page')


def edit_inv_V(request, id):

        if(request.method == 'POST'):
            item = ItemForm(request.POST)
            if(item.is_valid()):
                item.save(commit=False)

                item_obj=                   iv_items.objects.all()[id]
                item_obj.qr                 item.cleaned_data["qr"]
                item_obj.product_name=      item.cleaned_data["product_name"]
                item_obj.quantitity=        item.cleaned_data["quantitity"]
                item_obj.price=             item.cleaned_data["price"]
                item_obj.specification_fk=  item.cleaned_data["specification_fk"]
                item_obj.save()
                return redirect('invoices_page')

        item_item = iv_items.objects.all().order_by("id")[0]
        id =  id - item_item.id
        item = ItemForm()
        item.fields['qr'].initial=                  iv_items.objects.all()[id].qr
        item.fields['product_name'].initial=        iv_items.objects.all()[id].product_name
        item.fields['quantitity'].initial=          iv_items.objects.all()[id].quantitity
        item.fields['price'].initial=               iv_items.objects.all()[id].price
        item.fields['specification_fk'].initial=    iv_items.objects.all()[id].specification_fk
        return render(request,'invoice_management/invoice_edit.html',{'item' : item,'id' : id})
def add_inv_V(request):
        if(request.method == 'POST'):
            item = ItemForm(request.POST)
            if(item.is_valid()):
                qr =                item.cleaned_data["qr"]
                product_name =      item.cleaned_data["product_name"]
                quantitity =        item.cleaned_data["quantitity"]
                price =             item.cleaned_data["price"]
                specification_fk =  item.cleaned_data["specification_fk"]
                item_obj = iv_items(qr = qr, product_name = product_name, quantitity = quantitity, price = price, specification_fk = specification_fk)
                item_obj.save()
                return redirect('invoices_page')


        item = ItemForm()
        item.fields['qr']           .widget.attrs['placeholder']= "QR"
        item.fields['product_name'] .widget.attrs['placeholder']= "Product name"
        item.fields['quantitity']   .widget.attrs['placeholder']= "Quantity"
        item.fields['price']        .widget.attrs['placeholder']= "Price"
        return render(request, 'invoice_management/invoice_edit.html', {'item1':item} )

def delete_inv_V(request, id):
        dQuery = iv_items.objects.get( id = id).delete()
        return redirect('invoices_page')
def delete_inv_customer(request, id):
        dQuery = iv_cart.objects.get( id = id).delete()
        return redirect('invoice_profile_management:profile')
