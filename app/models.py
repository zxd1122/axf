from django.db import models

'''
商品表：  products
    name
    longName
    productId
    storeNums
    specifics
    sort
    marketPrice
    price
    categoryId
    childCid
    img
    keywords
    brandId
    brandName
    safeDay
    safeUnit
    safeUnitDesc
    isDelete
'''


class Product(models.Model):
    name = models.CharField(max_length=64)
    longName = models.CharField(max_length=128)
    productId = models.CharField(max_length=64)
    storeNums = models.IntegerField()
    specifics = models.CharField(max_length=32)
    sort = models.IntegerField()
    marketPrice = models.FloatField()
    price = models.FloatField()
    categoryId = models.CharField(max_length=64)
    childCid = models.CharField(max_length=64)
    img = models.CharField(max_length=256)
    keywords = models.CharField(max_length=256)
    brandId = models.CharField(max_length=64)
    brandName = models.CharField(max_length=64)
    safeDay = models.CharField(max_length=64)
    safeUnit = models.CharField(max_length=64)
    safeUnitDesc = models.CharField(max_length=64)
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "products"


'''
分组表：categories
    categoryId
    categoryName
    sort 
    isDelete
'''


class Category(models.Model):
    categoryId = models.CharField(max_length=64)
    categoryName = models.CharField(max_length=64)
    sort = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "categories"


'''
子组表：childcategories
    childId   
    childName
    sort
    category    (外键，所属的组)
    isDelete
'''


class ChildCategory(models.Model):
    childId = models.CharField(max_length=64)
    childName = models.CharField(max_length=64)
    sort = models.IntegerField()
    category = models.ForeignKey("Category")
    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = "childcategories"
