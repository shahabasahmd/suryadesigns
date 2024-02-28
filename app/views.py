from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User  
from django.contrib import messages ,auth
from .models import *
from django.db.models import Count,Avg
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# from app.forms import Reviewform

# Create your views here.
def index(request):
    dict_banner= {
      'banner':banner.objects.all()
     }
    dict_collections= {
      'collections':collections.objects.all()
     }
    dict_product= {
      # 'products':Product.objects.all().order_by("-id")
        'products':Product.objects.filter(product_status="published",featured="True")
       
        
   }
    context = {
      **dict_banner,**dict_product,**dict_collections
   }
    return render(request, "core/index.html",context)


def category_list_view(request):
     categories = Category.objects.all().annotate()
   
     context = {
          "categories":categories
     }
     return render(request, "core/category_list.html",context)

def product_list_view(request):
     products = Product.objects.filter(product_status="published")
     context = {
          "products":products
     }
     return render(request, "core/product_list.html",context)

def category_product_list_view(request,cid):
     category = Category.objects.get(cid=cid)
     products = Product.objects.filter(product_status="published",category=category)
           
     context = {
          "category":category,
          "products":products
      }
     return render(request, "core/category-product-list.html",context)

def product_detail_view(request,pid):
     product = Product.objects.get(pid=pid)
     p_image = product.p_images.all()
     reviews = Review.objects.filter(pid=product)
     products = Product.objects.filter(category=product.category).exclude(pid=pid)


     context = {
          'p':product,
          'p_image':p_image,
          'products':products,
          'reviews': reviews,

     }
     return render(request, "core/product-detail.html",context)



@login_required
def add_to_wishlist(request, pid):
    if request.user.is_authenticated:
        user = request.user
        product = Product.objects.get(pk=pid)
        wishlist_item, created = Wishlist.objects.get_or_create(user=user, product=product)
        if created:
            # Wishlist item was added successfully
            # You can redirect the user to a success page or send a success message
            return redirect('wishlist')
        else:
            # Wishlist item already exists
            # You can redirect the user to an appropriate page or send a message
            return HttpResponse("not added to wishlist")  
    else:
        # User is not authenticated, handle accordingly
        return redirect('sign-in') 


@login_required
def wishlist_view(request):
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)
        num_of_products = wishlist_items.count() 
        return render(request, 'core/wishlist.html', {'wishlist_items': wishlist_items, 'num_of_products': num_of_products})
    else:
        # Handle case where user is not authenticated
        return render(request, 'userauths/login.html')

@login_required
def remove_from_wishlist(request, item_id):
    if request.method == 'POST':
        try:
            item = Wishlist.objects.get(pk=item_id)
            item.delete()
            return redirect('wishlist')
        except Wishlist.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item does not exist'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



from django.shortcuts import get_object_or_404
@login_required
def add_review(request):
    if request.method == 'POST':
        # Retrieve the review text and product ID from the form data
        review_text = request.POST.get('review_text')
        product_id = request.POST.get('product_id')

        # Retrieve the Product instance corresponding to the provided product ID
        product = get_object_or_404(Product, pk=product_id)

        # Create a new Review instance and assign the Product instance to it
        review = Review.objects.create(
            createdby=request.user, 
            pid=product,  # Assign the Product instance to the pid field
            content=review_text,
        )

        # Optionally, you can add a success message
        messages.success(request, 'Review submitted successfully.')

        # Redirect to the product detail page
        # You need to specify the correct URL name and pass the product ID
        return redirect('index')

    return redirect('product_detail')



