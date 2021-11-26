from django.shortcuts import redirect, render
from todo.forms import ProductForm
from todo.models import Product
from django.db.models import Q
from django.contrib import messages
# Create your views here.

#home page
def home(request):
    product = Product()
    if request.method =='POST':

        name = request.POST['content']
        description =  request.POST['desc']
        product = Product.objects.create(name=name,description=description)
        product.save()
    product_data = Product.objects.all()
    

    return render(request, 'todo/home.html',{'product':product_data})


#search functionality 
def search(request):
    search_data = request.GET.get('search')
    mydict ={}
    if search_data:
        
        results = Product.objects.filter(Q(name__icontains=search_data) | Q(description__icontains=search_data))
        mydict = {'results':results}
    else:
        messages.info(request,'data not found')
    
    return render(request,'todo/search.html',context=mydict)





# update data  method
def update_data(request,i):
    i = int(i)
    try:
        product_id = Product.objects.get(id=i)

    except Product.DoesNotExist:
        return redirect('/')
    form = ProductForm(request.POST or None ,instance=product_id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'todo/form.html',{'data':form})
#delete method
def delete_data(request,i):
    i = int(i)
    try:
        form = Product.objects.get(id =i)
    except Product.DoesNotExist:
        return redirect('/')
    form.delete()
    return redirect('/')
    
# code by Sunil Raut






   