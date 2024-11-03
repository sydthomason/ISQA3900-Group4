from django.shortcuts import render, get_object_or_404
from .models import Collection, Product
from cart.forms import CartAddProductForm
from cart.cart import Cart

def product_list(request, collection_slug=None):
    collection = None
    collections = Collection.objects.all()
    products = Product.objects.filter(available=True)
    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = products.filter(collection=collection)
    cart = Cart(request)
    for product in products:
        product.cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/list.html', {
        'collection': collection,
        'collections': collections,
        'products': products,
        'cart': cart
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart = Cart(request)
    cartquantity = 0
    for item in cart:
        cartproduct = get_object_or_404(Product, id=item['product'].id)
        if product == cartproduct:
            cartquantity = item['quantity']
            break
    if product.quantity - cartquantity > 0:
        choices = [(i, str(i)) for i in range(1, product.quantity - cartquantity + 1)]
    else:
        choices = [(1, 0)]
    cart_product_form = CartAddProductForm(my_choices=choices)
    return render(request, 'shop/product/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'cart': cart
    })
