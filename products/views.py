from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.contrib import messages
from django.db.models import Q
from taggit.models import Tag

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.errir(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name_icontains=query) | Q(description_benefits_icontains=query) | Q(tag_icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term':query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)





# # def all_products_each_category(request):
# #     """ A view to show all products from each product category, including sorting and search queries """
#     products = Category.objects.all()

#      context = {
#         'categories': products,
#     }

#     return render(request, 'products/categories.html', context)

# # def all_products_each_healthgoal(request):
# #     """ A view to show all products from each product health goal, including sorting and search queries """
#     products = HealthGoal.objects.all()

#      context = {
#         'healthgoals': products,
#     }

#     return render(request, 'products/healthgoals.html', context)

# # def all_products_each_package(request):
# #     """ A view to show all products from each product package, including sorting and search queries """
#     products = Package.objects.all()

#      context = {
#         'packages': products,
#     }

#     return render(request, 'products/packages.html', context)