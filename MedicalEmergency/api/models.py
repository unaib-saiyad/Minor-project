import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models


# Register your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    mobile = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.user.username}"


class ProductCategory(models.Model):
    category = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.category}"


def get_uuid_product():
    id = uuid.uuid4()
    if not Product.objects.filter(product_id=id).exists():
        return id


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, blank=False, null=False, default=get_uuid_product, editable=False)
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, blank=False, null=False, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=50, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    desc = models.CharField(max_length=300, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="shop/images", null=False, blank=False)

    def __str__(self):
        return f"{self.product_id}_{self.product_name}"


def get_uuid_order():
    while True:
        id = uuid.uuid4()
        if not Order.objects.filter(id=id).exists():
            return id


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=get_uuid_order, blank=False, null=False, editable=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    delivery = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"


def get_uuid_emergency():
    while True:
        id = uuid.uuid4()
        if not EmergencyCall.objects.filter(meeting_id=id).exists():
            return id


class EmergencyCall(models.Model):
    meeting_admin = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    meeting_id = models.UUIDField(primary_key=True, default=get_uuid_emergency, blank=False,
                                  null=False, editable=False)
    link = models.URLField(max_length=200, blank=False, null=False)
    is_activated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.meeting_admin.is_superuser:
            raise TypeError("Only superuser can conduct meetings")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.meeting_admin.username}_{self.meeting_id}"


BLOOD_GROUP = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)


class BloodDonation(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, blank=False, null=False)
    mobile = models.PositiveIntegerField(blank=False, null=False)
    blood_group = models.CharField(max_length=50, choices=BLOOD_GROUP, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    pin = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.id}_{self.user}"
