from django.shortcuts import render
from .models import Product
from taggit.models import Tag

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


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