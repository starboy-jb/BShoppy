from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
import json

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n // 4 + (n % 4 > 0)
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds' : allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower():
        return True
    return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodTemp = Product.objects.filter(category=cat)
        prod = [item for item in prodTemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + (n % 4 > 0)
        if n > 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, 'message' : ""}
    if len(allProds) == 0 or len(query) < 4:
        params = {'message': "Please enter valid product name"}
    return render(request, 'shop/search.html', params)

def about(request):
    return render(request, 'shop/about.html')

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', 0)
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id = orderId, email = email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id = orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                response = json.dumps({'status': "success", 'updates':updates, 'item_json': order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                response = json.dumps({'status': "error"},
                                      default=str)
                return HttpResponse(response)

        except Exception as e:
            response = json.dumps({'status': "exception"},
                                  default=str)
            return HttpResponse(response)
    return render(request, 'shop/tracker.html')

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc, sep='\n')
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})

def myCart(request):
    return render(request, 'shop/myCart.html')

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        amount = request.POST.get('amount', 0)
        print(amount)
        order = Order(items_json = items_json, name = name, email = email, address=address, city = city, state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id = order.order_id, update_desc = "You order has been placed")
        update.save()
        thank = True
        return render(request, 'shop/checkout.html', {'thank': thank, 'id' : order.order_id})
    return render(request, 'shop/checkout.html')

def productView(request, myId):
    products = Product.objects.filter(id = myId)
    return render(request, 'shop/prodView.html', {'product': products[0]})
