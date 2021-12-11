from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Category, Product, Client, Order
from django.shortcuts import get_object_or_404
from .forms import OrderForm
from .forms import UserForm
from .forms import InterestForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request,'myapp/dashboard.html')
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html')
@login_required

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('index')))

def dashboard(request):
    return render(request,'myapp/dashboard.html')

def myorders(request):
    user = User.objects.filter(username=request.session("username"))

    return render(request, "myorders.html")


# Create your views here.

def index(request):
    cat_list = Category.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html',{'cat_list':cat_list})


def about(request):
    response = render(request, "myapp/about.html")
    # create cookie

    expiry_time = 60 * 5  # in seconds
    response.set_cookie("about_visits", expiry_time);
    if request.COOKIES.get('about_visits'):
        value = int(request.COOKIES.get('about_visits'))
        response.set_cookie('about_visits', value + 1)
        print("value",value)


    return response



def products(request):
 prodlist = Product.objects.all().order_by('id')[:10]
 return render(request, 'myapp/products.html', {'prodlist': prodlist})


def detail(request, cat_no):
    cat_number = cat_no
    cat_list = Category.objects.all()
    product_list = Product.objects.all()
    a = 0
    n = []
    for c in cat_list:
        if cat_number == c.id:
            m = c.warehouse
            print(m)
            a = 1


            for p in product_list:
                print(p.name)
                if m == p.category.name:
                    print("true")


    if a == 0:
        return get_object_or_404(Category, id=cat_no)

    return render(request, 'myapp/detail.html', {'m': m})


def place_order(request):
    msg = ''
    prodlist = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print("saved1")
        if form.is_valid():
            order = form.save(commit= False)
            print("saved")
            if order.num_units <= order.product.stock:
                order.save()
                order.product.stock = order.product.stock - order.num_units
                print("stock",order.product.stock)
                msg = 'Your order has been placed successfully.'
            else:
                msg = 'We do not have sufficient stock to fill your order.'
            return render(request, 'myapp/order_response.html', {'msg': msg})

    else:
        form = OrderForm()
        print("not saved")
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg,
                                                     'prodlist': prodlist})

def response(request):
    return render(request, "myapp/order_response.html")

def productdetail(request, prod_id):
    form = InterestForm()
    prod_info = Product.objects.filter(id =prod_id)
    return render(request, 'myapp/productdetail.html', {'prod_info':prod_info, 'form': InterestForm })


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return render(request, 'myapp/login.html')

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, "myapp/register.html", {'user_form': user_form, registered: 'registered'})
