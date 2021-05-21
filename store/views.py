from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def comments(request):
    context = {}
    return render(request, 'store/comments.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def category(request):
    context = {}
    return render(request, 'store/category.html', context)


def login(request):
    context = {}
    return render(request, 'store/login.html', context)


def logout(request):
    context = {}
    return render(request, 'store/logout.html', context)

