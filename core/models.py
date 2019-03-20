from django.db import models
from django.http import HttpResponse

# Create your models here.

# ---------- MEAL MODEL ------------------------
class Meal(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    price = models.PositiveIntegerField()
    # picture = models.ImageField(upload_to=)
    class Meta:
        verbose_name =("Meal")
        verbose_name_plural =("Meals")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return HttpResponse("Meal_detail", kwargs={"pk": self.pk})

# ---------- TABLE MODEL ------------------------

class Table(models.Model):
    name = models.CharField(max_length=60)
    class Meta:
        verbose_name = ("Table")
        verbose_name_plural = ("Tables")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Table_detail", kwargs={"pk": self.pk})

# ---------- EMPLOYEE MODEL ------------------------

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)
    serving_Tables = models.ForeignKey(
        to= 'Table',
        related_name='Serving',
        on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})

# ---------- ORDER MODEL ------------------------

class Order(models.Model):
    timestamp = models.DateTimeField(auto_now=True)

    Table = models.ForeignKey(
        to= 'Table',
        related_name='serve_on',
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    Meal = models.ForeignKey(
        to= 'Meal',
        related_name='ordered',
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    note = models.CharField(max_length=120, blank=True, null=True)

    waiter = models.ForeignKey(
        to= 'Employee',
        related_name='takenby',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    
    

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return self.note

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return ("orders/{}/delete").format(self.pk)

    def get_update_url(self):
        return ("orders/{}/update").format(self.pk)