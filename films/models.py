from django.db import models
from django.utils.text import slugify

from accounts.models import BaseEntity, User


class Category(BaseEntity):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categoryCreator')
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.name[:30]

    def creator_name(self):
        return self.creator.name

    @property
    def parent_category(self):
        return self.parent.name


class Actor(BaseEntity):
    name = models.CharField(max_length=35)

    def __str__(self): return self.name


class Trailer(BaseEntity):
    name = models.CharField(max_length=150)
    trailer_url = models.URLField(max_length=250)
    image = models.ImageField(upload_to='trailer/%y/%m', blank=True, null=True)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Film(BaseEntity):
    Type = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    director = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filmsDirector')
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='filmsCategory')
    actors = models.ManyToManyField(Actor, related_name='movieActors', blank=True)
    producers = models.JSONField(blank=True, null=True, default=None)
    types = models.CharField(max_length=1, choices=Type)
    is_publish = models.BooleanField(default=False)
    release_date = models.DateTimeField()
    description = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    discount_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='films/%y/%m', blank=True, null=True)
    video = models.URLField(max_length=250, blank=True)
    is_watchable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def category_name(self):
        return self.category.name


class Purchase(BaseEntity):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='buy_films')
    quantity = models.IntegerField(default=0)
    vat = models.DecimalField(default=15.00, max_digits=100, decimal_places=2)
    status = models.BooleanField(default=True)

    PAYMENT_TYPES = (
        ('T1', 'CREDIT CARD'),
        ('T2', 'VISA CARD'),
        ('T3', 'BANK'),
        ('T4', 'STRIPE'),
    )
    payment = models.CharField(max_length=2, choices=PAYMENT_TYPES)
    is_download = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.name

    @property
    def get_discount_price(self):
        return self.item.discount_price

    @property
    def total_price(self):
        return self.item.price * self.quantity - self.vat

    @property
    def get_item_name(self):
        return self.item.name

    @property
    def get_customer_name(self):
        return self.customer.name


class Notification(BaseEntity):
    title = models.CharField(max_length=100)
    is_publish = models.BooleanField(default=True)
    details = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='notification/%m/%d', blank=True, null=True)

    def __str__(self): return self.title

