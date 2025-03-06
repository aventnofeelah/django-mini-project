from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
CATEGORIES = [
    ("Electronics", "Electronics"),
    ("Computers and laptops", "Computers and laptops"),
    ("Smartphones and gadgets", "Smartphones and gadgets"),
    ("Household appliances", "Household appliances"),
    ("Clothing and footwear", "Clothing and footwear"),
    ("Accessories and jewelry", "Accessories and jewelry"),
    ("Cosmetics and perfumery", "Cosmetics and perfumery"),
    ("Health and care", "Health and care"),
    ("Children's goods", "Children's goods"),
    ("Toys", "Toys"),
    ("Books", "Books"),
    ("Stationery and office supplies", "Stationery and office supplies"),
    ("Automotive goods", "Automotive goods"),
    ("Construction and repair", "Construction and repair"),
    ("Home and garden", "Home and garden"),
    ("Furniture", "Furniture"),
    ("Sports and recreation", "Sports and recreation"),
    ("Food", "Food"),
    ("Pet supplies", "Pet supplies"),
    ("Musical instruments", "Musical instruments"),
    ("Antiques and collecting", "Antiques and collecting"),
    ("Creative goods", "Creative goods"),
    ("Hobby goods", "Hobby goods"),
    ("Holiday goods", "Holiday goods"),
]

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False, verbose_name="Email")
    avatar = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Seller", related_name="products")
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Product name")
    category = models.CharField(max_length=50, choices=CATEGORIES, null=False, blank=False, verbose_name="Category")
    price = models.IntegerField(blank=False, null=False, verbose_name="Price")
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.user} {self.name}"
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"