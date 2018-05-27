from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return "Category name is " + self.categoryname


class Customers(models.Model):
    customerid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True, db_column='zip')
    country = models.CharField(max_length=50)
    region = models.SmallIntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    creditcardtype = models.IntegerField()
    creditcard = models.CharField(max_length=50)
    creditcardexpiration = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    age = models.SmallIntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'

    def __str__(self):
        return "Customer name of " + self.firstname + " " + self.lastname + " from " + self.city


class Inventory(models.Model):
    prod_id = models.AutoField(primary_key=True)
    quan_in_stock = models.IntegerField()
    sales = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'

    def __str__(self):
        return "ID " + str(self.prod_id)+ " has " + \
        str(self.quan_in_stock) + " stock and " + str(self.sales) + " sales"


class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    category = models.IntegerField()
    title = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    special = models.SmallIntegerField(null=True, blank=True)
    common_prod_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'

    def __str__(self):
        return self.title + " starring " + self.actor


class Reorder(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    date_low = models.DateField()
    quan_low = models.IntegerField()
    date_reordered = models.DateField(null=True, blank=True)
    quan_reordered = models.IntegerField(null=True, blank=True)
    date_expected = models.DateField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'reorder'

    def __str__(self):
        return "Product ID " + str(self.prod_id)


class CustomerHistory(models.Model):
    hist_id = models.AutoField(primary_key=True, db_column='id')
    customerid = models.ForeignKey(Customers, to_field='customerid',
                                    on_delete=models.CASCADE, db_column='customerid')
    orderid = models.IntegerField()
    prod_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cust_hist'

    def __str__(self):
        return str(self.customerid) + " " + str(self.orderid) + " " + str(self.prod_id)


class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    orderdate = models.DateField()
    customerid = models.ForeignKey(Customers, to_field='customerid',
                                    on_delete=models.CASCADE, db_column='customerid')
    netamount = models.DecimalField(max_digits=12, decimal_places=2)
    tax = models.DecimalField(max_digits=12, decimal_places=2)
    totalamount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
        return str(self.orderid) + " of " + str(self.totalamount)


class OrderLines(models.Model):
    table_id = models.AutoField(primary_key=True, db_column='id')
    orderlineid = models.IntegerField()
    orderid = models.ForeignKey(Orders, to_field='orderid',
                                db_column='orderid', on_delete=models.CASCADE)
    prod_id = models.IntegerField()
    quantity = models.SmallIntegerField()
    orderdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'orderlines'

    def __str__(self):
        return str(self.prod_id) + " of " +str(self.quantity)
