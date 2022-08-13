from django.db import models
from django.utils.text import slugify

from accounts.models import BaseEntity, User


class Category(BaseEntity):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categoryCreator')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
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
    is_publish = models.BooleanField(default=True)
    image = models.ImageField(upload_to='trailer/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.name


class Film(BaseEntity):
    Type = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=120)
    is_publish = models.BooleanField(default=False)
    video = models.URLField(max_length=250, blank=True)
    is_watchable = models.BooleanField(default=False)
    types = models.CharField(max_length=1, choices=Type)
    slug = models.SlugField(unique=True, blank=True, null=True)
    producers = models.JSONField(blank=True, null=True, default=None)
    actors = models.ManyToManyField(Actor, related_name='movieActors', blank=True)
    release_date = models.DateTimeField()
    description = models.TextField()
    price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    discount_price = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='films/%y/%m', blank=True, null=True)
    director = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filmsDirector')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='filmsCategory')

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
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film')
    vat = models.DecimalField(default=15.00, max_digits=100, decimal_places=2)

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
