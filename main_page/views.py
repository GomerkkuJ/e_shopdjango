from django.shortcuts import render, redirect
# from .models import Category, Product, Cart
from . import models
from .forms import SearchForm
from telebot import TeleBot

bot = TeleBot('6268047377:AAFBPtUIx89JX77RhHu1g0XNDB9I3rCxBYw', parse_mode='HTML')

def index(request):
    # Берем все категории с базы данных
    all_categories = models.Category.objects.all()
    all_products = models.Product.objects.all()

    # Получим значение введенное в поисковик
    # from_frontend = request.GET.get('exact_product')
    #
    # # Было ли введено что-то в поиск
    # if from_frontend is not None:
    #     all_products = models.Product.objects.filter(product_name__contains=from_frontend)

    search_bar =SearchForm()

    # Создаем словарь
    context = {'all_categories': all_categories,
               'products': all_products,
               'form': search_bar}
    if request.method == 'POST':
        product_find = request.POST.get('search_product')
        try:
            search_result = models.Product.objects.get(product_name=product_find)
            return redirect(f'/item{search_result.id}')
        except:
            return redirect("/")
    return render(request, 'index.html', context)

def current_category(request, pk):
    category = models.Product.objects.get(id=pk)
    context = {'products': category}
    return render(request, 'current_category.html', context)

def get_exact_category(request, pk):
    # Получаем категорию
    exact_category = models.Category.objects.get(id=pk)
    # выводим продукты по этой категории
    category_products = models.Product.objects.filter(product_categoty=exact_category)
    return render(request, 'exact_category.html', {'category_products': category_products})

# Получить определенный продукт
def exact_product(request, pk):
    # find_product_from_db = models.Product.objects.get(id=pk)
    # context = {'product': find_product_from_db}
    product = models.Product.objects.get(id=pk)
    if request.method == 'POST':
        models.Cart.objects.create(user_id=request.user.id,
                                   user_product=product,
                                   user_product_quantity=request.POST.get('user_product_quantity'),
            total_for_product=product.product_price*int(request.POST.get('user_product_quantity')))
        return redirect('/cart')
    return render(request, 'exact_product.html')


def get_user_cart(request):
    user_cart = models.Cart.objects.filter(user_id=request.user.id)
    return render(request, 'user_cart.html', {'cart': user_cart})

# Оформление заказа
def complete_order(request):
    # Получаем корзину пользователя
    user_cart = models.Cart.objects.filter(user_id=request.user.id)

    #Формируем сообщения для ТГ админа
    result_message = 'Новый заказ(сайт)\n\n'
    total_for_all_cart = 0
    for cart in user_cart:
        result_message += f'<b>{cart.user_product}</b> x {cart.user_product_quantity} = {cart.total_for_product} сум\n'
        total_for_all_cart += cart.total_for_product
    result_message += f'\n---------\n<b>Итого: {total_for_all_cart} сум</b>'

    # Отправляем админу сообщение в ТГ
    bot.send_message(860227652, result_message)


    return redirect('/')



