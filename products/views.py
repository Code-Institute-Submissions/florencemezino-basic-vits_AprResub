from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from taggit.models import Tag

from .models import Product, Category, HealthGoal, Package
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    healthgoals = None
    packages = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=['vitamins', 'minerals', 'plants', 'specialities', 'merchandises'])

        if 'healthgoal' in request.GET:
            healthgoals = request.GET['healthgoal'].split(',')
            products = products.filter(healthgoal__name__in=healthgoals)
            healthgoals = HealthGoal.objects.filter(name__in=['immunity', 'brain', 'energy', 'eyes', 'sleep', 'stress', 'heart', 'joints', 'skin', 'hair', 'digestion', 'bones', 'shape'])

        if 'package' in request.GET:
            packages = request.GET['package'].split(',')
            products = products.filter(package__name__in=packages)
            packages = Package.objects.filter(name__in=['women_health', 'men_health', 'kids_health', 'teens_health', 'seniors_health'])

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description_benefits__icontains=query) | Q(healthgoal__icontains=query) | Q(package__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_healthgoals': healthgoals,
        'current_packages': packages,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

# admin : add product
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)





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