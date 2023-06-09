from django.db import models

# Создать таблицу категорий
class Category(models.Model):
    # Создать колонки для таблицы
    category_name = models.CharField(max_length=75)
    reg_data = models.DateTimeField(auto_now_add=True)
    # вывод информации в нормальном виде
    def __str__(self):
        return self.category_name



# Создать таблицу для продуктов
class Product(models.Model):
    # Создаем колонки для таблицы продуктов
    product_name = models.CharField(max_length=125)
    product_count = models.IntegerField()
    product_price = models.FloatField()
    product_photo = models.ImageField(upload_to='media')
    product_des = models.TextField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    reg_date = models.DateTimeField(auto_now_add=True)

    # Вывод в нормальм виде
    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.PositiveSmallIntegerField(default=1)
    total_for_product = models.FloatField(null=True)

    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_product)

