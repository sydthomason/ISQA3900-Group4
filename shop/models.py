from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User  # Using Django's built-in User model


class Collection(models.Model):  # Groups suits into categories
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'collection'
        verbose_name_plural = 'collections'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_collection', args=[self.slug])


class Suit(models.Model):  # Represents individual suits
    collection = models.ForeignKey(Collection, related_name='suits', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Updated from rental_price
    quantity = models.IntegerField(default=1)  # Added for inventory tracking
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='suits/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:suit_detail', args=[self.slug])


class Transaction(models.Model):  # Tracks suit purchases
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)  # Links to the User
    suit = models.ForeignKey(Suit, related_name='transactions', on_delete=models.CASCADE)  # Links to the Suit
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total cost of purchase
    payment_method = models.CharField(max_length=50, choices=[('CC', 'Credit Card'), ('PP', 'PayPal')])
    transaction_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-transaction_date',)

    def __str__(self):
        return f"Transaction {self.id} by {self.user.username}"
