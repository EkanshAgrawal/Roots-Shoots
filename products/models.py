from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.utils.text import slugify
from django.contrib.auth.models import User



class ItemsCat(models.Model):
    catName = models.CharField(max_length=20, default="")

    def __str__(self) -> str:
        return self.catName

class ItemMain(models.Model):
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=25)
    description = models.TextField()
    category = models.ForeignKey(ItemsCat, on_delete=models.CASCADE)
    availablity = models.BooleanField(default=False)
    shippingCharges = models.IntegerField(default=0)   
    offers = models.IntegerField(default=0)
    plantingAndCare = models.TextField()
    slug = models.SlugField(max_length=50,unique=True, default="", editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class ItemsImages(models.Model):
    title = models.ForeignKey(ItemMain, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images')

    def __str__(self) -> str:
        return str(self.title)


class ItemsSpecifications(models.Model):
    title = models.ForeignKey(ItemMain, on_delete=models.CASCADE)
    commonName = models.TextField(default="", max_length=50)
    plantSpread = models.TextField(default="", max_length=50)
    maxHeight = models.TextField(default="", max_length=50)
    sunlight = models.TextField(default="", max_length=50)
    watering = models.TextField(default="", max_length=50)
    soil = models.TextField(default="", max_length=50)
    temp = models.TextField(default="", max_length=50)
    ferti = models.TextField(default="", max_length=50)
    bloomTime = models.TextField(default="", max_length=50)

    def __str__(self) -> str:
        return str(self.title)


class ItemFaq(models.Model):
    title = models.ForeignKey(ItemMain, on_delete=models.CASCADE)
    question = models.CharField(max_length=50)
    answer = models.TextField()

    def __str__(self) -> str:
        return str(self.title)

class ItemRating(models.Model):
    title = models.ForeignKey(ItemMain, on_delete=models.CASCADE)
    ratingCount = models.IntegerField()
    rating = models.IntegerField()
    ratingValue = models.DecimalField(decimal_places=2, max_digits=10, editable=False)
    feedback = models.TextField(default="")

    def save(self, *args, **kwargs):
        self.ratingValue = self.rating / self.ratingCount
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.title)


class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.ForeignKey(ItemMain, on_delete=models.CASCADE)
    total = models.IntegerField()

    def __str__(self) -> str:
        return str(str(self.user) + " -> " + str(self.title))


class Bstates(models.Model):

    states = models.CharField(max_length = 50, unique = True)
    def __str__(self):
        return self.states


class Billing(models.Model):
    Bfirst_name = models.CharField(max_length= 264)
    Blast_name = models.CharField(max_length= 264)
    Bcheckout_states = models.ForeignKey(Bstates, on_delete = models.CASCADE, related_name ='Bstates')
    Bstreet = models.CharField(max_length= 264)
    Bapartment = models.CharField(max_length= 264)
    Bcity = models.CharField(max_length= 264)
    Bzip = models.IntegerField(default=0)
    Bphone = models.IntegerField(default=0)
    Bemail = models.EmailField(max_length= 264)

class Shipping(models.Model):
    Sfirst_name = models.CharField(max_length= 264)
    Slast_name = models.CharField(max_length= 264)
    Scheckout_states = models.ForeignKey(Bstates, on_delete = models.CASCADE, related_name ='Sstates')
    Sstreet = models.CharField(max_length= 264)
    Sapartment = models.CharField(max_length= 264)
    Scity = models.CharField(max_length= 264)
    Szip = models.IntegerField(default=0)
    Sphone = models.IntegerField(default=0)
    Semail = models.EmailField(max_length= 264)

class Payment(models.Model):
    cardno = models.IntegerField(default=0)
    namecard = models.CharField(max_length= 264)
    cvv = models.IntegerField(default=0)
    validity = models.DateField(default="0000-00")

    def save(self, *args, **kwargs):
        check = self.validity.split("-")
        print(check)
        if len(check) == 2:
            self.validity += "-01"
            print(self.validity)
        super().save(*args, **kwargs)
    


