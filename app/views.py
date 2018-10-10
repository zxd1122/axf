from django.shortcuts import render

from app.models import Product, Category, ChildCategory


# Create your views here.

def home(request):
    return render(request, "axfApp/home/home.html")


def market(request, categoryId):
    # 获取分组数据
    categories = Category.objects.all()

    # 获取商品数据
    products = Product.objects.filter(categoryId=categoryId)

    return render(request, "axfApp/market/market.html", {"categories": categories, "products": products})


def cart(request):
    return render(request, "axfApp/cart/cart.html")


def mine(request):
    return render(request, "axfApp/mine/mine.html")
