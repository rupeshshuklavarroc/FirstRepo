from django.shortcuts import render,redirect
from .models import *
# Create your views here.

from django.http import HttpResponse
from .forms import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    total_customer =customers.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()

    context = {'orders' : orders,'customers':customers ,'total_orders' : total_orders,
               'total_customer':total_customer,'pending':pending,'delivered': delivered}
    return render(request,'wipscreen/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request,'wipscreen/products.html',{"products":products})

def customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context ={'customer' : customer,
              'orders' : orders,
              'total_orders':total_orders
    }
    return render(request,'wipscreen/customers.html',context)


def contact(request):
    return HttpResponse('Contact Page')

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print (request.POST)
        form = OrderForm(request.POST)
        form.save()
        return redirect("/")
    context = {'form':form}
    return render(request,'wipscreen/order_form.html',context)

def updateOrder(request,pk):
    order =Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        #print (request.POST)
        form = OrderForm(request.POST,instance=order)
        form.save()
        return redirect("/")
    context = {'form':form}
    return render(request,'wipscreen/order_form.html',context)

def deleteOrder(request,pk):
    order =Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect("/")    
    context = {'item':order}
    
    return render(request,'wipscreen/delete.html',context)

def createEntry(request):
    form = EntryForm()
    if request.method == 'POST':
        #print (request.POST)
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            # Print or log form errors
            print(form.errors)
    context = {'form':form}
    return render(request,'wipscreen/newentry_form.html',context)