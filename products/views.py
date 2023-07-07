from typing import AnyStr
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import ItemMain, ItemsCat, ItemsImages, ItemRating, ItemsSpecifications, ItemFaq, UserCart,Billing, Bstates, Payment, Shipping, ItemMain
from blogs.models import BlogPlant
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    context = {}
    items = ItemMain.objects.all().order_by('-id')[:4]
    items_list = []
    for i in items:
        l = []
        l.append(i.title)
        l.append(i.price)
        l.append(i.slug)
        ima = ItemsImages.objects.filter(title = i)[0]
        l.append(ima.image)
        items_list.append(l)
    context['items'] = items_list
    blogs = BlogPlant.objects.all().order_by('-id')[:3]
    blogs_list = []
    for i in blogs:
        l = []
        l.append(i.blog_title)
        l.append(i.author)
        l.append(i.publish_date)
        l.append(i.blog_image)
        l.append(i.slug)
        l.append(i.blog_content[:100])
        blogs_list.append(l)
    context['blogs'] = blogs_list


    return render(request, 'home.html', context)

def items_display(request):    
    cat = request.GET.getlist('cat', [])
    offerss = request.GET.getlist('offer', [])
    items = []
    offerss = list(map(int, offerss))
    if len(offerss) > 0:
        min_off = min(offerss)
    if len(cat) > 0 or len(offerss) > 0:
        if (len(offerss) and len(cat)):
            items = ItemMain.objects.filter(category__in = ItemsCat.objects.filter(catName__in=cat), offers__gt=min_off)
        elif (len(cat)):
            items = ItemMain.objects.filter(category__in = ItemsCat.objects.filter(catName__in=cat))
        else:
            items = ItemMain.objects.filter(offers__gt=min_off)
    else:
        items = ItemMain.objects.all()
    l = []
    for i in items:
        ll = []
        ll.append(ItemsImages.objects.filter(title=ItemMain.objects.filter(title = i.title)[0])[0].image)
        ll.append(ItemRating.objects.filter(title=ItemMain.objects.filter(title = i.title)[0])[0].ratingValue)
        ll.append(i.price)
        ll.append(i.description)
        ll.append(i.title)
        price = i.price
        offer = i.offers
        newPrice = price - (price * offer)//100
        ll.append(newPrice)
        ll.append(i.slug)
        ll.append(i.offers)
        l.append(ll)
    context = {
        "items": l
    }
    return render(request, "products/items_display.html", context)

@login_required(login_url='login')
def itemView(request, the_slug):
    if request.method == 'GET':
        context = {}
        p = []
        d=[]

        currentItem = ItemMain.objects.filter(slug = the_slug)[0]
        title = currentItem.title
        images = ItemsImages.objects.filter(title=ItemMain.objects.filter(title = title)[0])
        rating = ItemRating.objects.filter(title=ItemMain.objects.filter(title = title)[0])[0]
        descrip = ItemsSpecifications.objects.filter(title=ItemMain.objects.filter(title = title)[0])[0]
        faq = ItemFaq.objects.filter(title=ItemMain.objects.filter(title = title)[0])

        #produect
        price = currentItem.price
        offer = currentItem.offers
        newPrice = price - (price * offer)//100
        p.append(title)
        p.append(price)
        p.append(offer)
        p.append(newPrice)
        p.append(currentItem.availablity)
        p.append(currentItem.shippingCharges)
        p.append(rating.ratingCount)
        p.append(rating.ratingValue)
        p.append(currentItem.plantingAndCare)
        p.append(currentItem.slug)

        #description
        d.append(currentItem.description)
        d.append(descrip.commonName)
        d.append(descrip.plantSpread)
        d.append(descrip.maxHeight)
        d.append(descrip.sunlight)
        d.append(descrip.watering)
        d.append(descrip.soil)
        d.append(descrip.temp)
        d.append(descrip.ferti)
        d.append(descrip.bloomTime)

        context['products'] = p
        context['images'] = images
        context['des'] = d
        context['faq'] = faq

        return render(request, 'products/single_product.html', context)
    else:
        cartItem = json.loads(request.body)
        cartModel = UserCart.objects.filter(
            user = User.objects.filter(username = cartItem.get('user', ''))[0],
            title = ItemMain.objects.filter(title=cartItem.get('item', ''))[0],
        )
        if cartModel:
            cartModel[0].total += 1
            cartModel = UserCart.objects.create(
            user = User.objects.filter(username = cartItem.get('user', ''))[0],
            title = ItemMain.objects.filter(title=cartItem.get('item', ''))[0],
            )
            cartModel[0].save()
        else:
            cartModel = UserCart.objects.create(
                user = User.objects.filter(username = cartItem.get('user', ''))[0],
                title = ItemMain.objects.filter(title=cartItem.get('item', ''))[0],
                total = 1
            )
            cartModel.save()


        return redirect('itemView', the_slug=the_slug)


    

@login_required(login_url='login')
def addReview(request, the_slug):

    if request.method == "POST":
        currentItem = ItemMain.objects.filter(slug = the_slug)[0]
        rating = ItemRating.objects.filter(title=currentItem)[0]
        rating.ratingCount += 1
        rating.rating += int(request.POST.get('rate', 5))
        rating.feedback = request.POST.get('feeds', "")
        rating.save()

    
    return redirect("/items/"+the_slug)

@login_required(login_url='login')
def product_upload(request):
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title', "")
        price = int(request.POST.get('price', 0))
        offers = int(request.POST.get('offers', 0))
        shippingCharges = int(request.POST.get('shippingCharges', 0))
        category = request.POST.get('category', "tree")
        countofproducts = int(request.POST.get('countofproducts', 0))
        description = request.POST.get('description', "")
        plantingAndCare = request.POST.get('plantingAndCare', "")
        availablity = False
        if countofproducts:
            availablity = True

        itemmain = ItemMain.objects.create(
            title = title,
            price = price,
            description = description,
            category = ItemsCat.objects.filter(catName=category)[0],
            availablity = availablity,
            shippingCharges = shippingCharges,
            offers = offers,
            plantingAndCare = plantingAndCare
        )
        itemmain.save()

        commonName = request.POST.get('commonName', "")
        plantSpread = request.POST.get('plantSpread', "")
        maxHeight = request.POST.get('maxHeight', "")
        sunlight = request.POST.get('sunlight', "")
        watering = request.POST.get('watering', "")
        soil = request.POST.get('soil', "")
        temp = request.POST.get('temp', "")
        ferti = request.POST.get('ferti', "")
        bloomTime = request.POST.get('bloomTime', "")

        itemsSpecifications = ItemsSpecifications.objects.create(
            title = ItemMain.objects.filter(title = title)[0],
            commonName = commonName,
            plantSpread = plantSpread,
            maxHeight = maxHeight,
            sunlight = sunlight,
            watering = watering,
            soil = soil,
            temp = temp,
            ferti = ferti,
            bloomTime = bloomTime
        )
        itemsSpecifications.save()

        img0 = request.FILES['img0']
        img1 = request.FILES['img1']
        img2 = request.FILES['img2']
        img3 = request.FILES['img3']

        img = ItemsImages.objects.create(
            title = ItemMain.objects.filter(title=title)[0],
            image = img0
        )
        img.save()

        img = ItemsImages.objects.create(
            title = ItemMain.objects.filter(title=title)[0],
            image = img1
        )
        img.save()
        img = ItemsImages.objects.create(
            title = ItemMain.objects.filter(title=title)[0],
            image = img2
        )
        img.save()
        img = ItemsImages.objects.create(
            title = ItemMain.objects.filter(title=title)[0],
            image = img3
        )
        img.save()

        rat = ItemRating.objects.create(
            title = ItemMain.objects.filter(title=title)[0],
            ratingCount = 1,
            rating = 5,
            feedback = ""
        )

        itemFaq = ItemFaq.objects.create(
            title = ItemMain.objects.filter(title=title)[0],
            question = "",
            answer = ""
        )

        rat.save()
        itemFaq.save()


    return render(request, 'products/product_upload.html', context)

def faq(request):
    context = {}
    return render(request, 'faq.html', context)

@login_required(login_url='login')
def cart(request):
    context = {}
    if request.method == "GET":
        user = request.user
        items = UserCart.objects.filter(
            user = User.objects.filter(username = user)[0]
            )
        l = []
        for i in items:
            ll = []
            item =ItemMain.objects.filter(title = i.title)[0]
            ll.append(ItemsImages.objects.filter(title=item)[0].image)
            ll.append(i.title)
            ll.append(item.description)
            price = item.price
            offer = item.offers
            newPrice = price - (price * offer)//100
            ll.append(newPrice)
            ll.append(i.total)
            l.append(ll)
        context['items'] = l  
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def clear_cart(request):
    context = {}
    if request.method == "GET":
        user = request.user
        items = UserCart.objects.filter(
            user = User.objects.filter(username = user)[0]
            )
        l = []
        for i in items:
            ll = []
            item =ItemMain.objects.filter(title = i.title)[0]
            ll.append(ItemsImages.objects.filter(title=item)[0].image)
            ll.append(i.title)
            ll.append(item.description)
            price = item.price
            offer = item.offers
            newPrice = price - (price * offer)//100
            ll.append(newPrice)
            ll.append(i.total)
            l.append(ll)
            i.delete()
        context['items'] = l  
        return redirect('cart')

@login_required(login_url='login')
def checkout(request):
    if request.method == 'GET':
        user = request.user
        items = UserCart.objects.filter(
            user = User.objects.filter(username = user)[0]
            )
        l = []
        sprice = 0
        snewPrice = 0
        for i in items:
            ll = []
            item =ItemMain.objects.filter(title = i.title)[0]
            price = item.price
            offer = item.offers
            newPrice = price - (price * offer)//100

            sprice += price
            snewPrice += newPrice
        context = {}
        context['price'] = sprice
        context['offer'] = sprice - snewPrice
        context['newPp'] = snewPrice
        
    if request.method == 'POST':
        if request.user.is_authenticated:
            Bfirst_name = request.POST['Bfirst_name']
            Blast_name = request.POST['Blast_name']
            Bcheckout_states = Bstates.objects.get(states = request.POST['Bstates'])
            Bstreet = request.POST['Bstreet']
            Bapartment = request.POST['Bapartment']
            Bcity = request.POST['Bcity']
            Bzip = request.POST['Bzip']
            Bphone = request.POST['Bphone']
            Bemail = request.POST['Bemail']    
            cardno = request.POST['cardno']
            namecard = request.POST['namecard']
            validity = request.POST['validity']
            cvv = request.POST['cvv']
            billing = Billing.objects.create(Bfirst_name=Bfirst_name, Blast_name=Blast_name, Bcheckout_states=Bcheckout_states, Bstreet=Bstreet, Bapartment=Bapartment, Bcity=Bcity, Bzip=float(Bzip), Bphone=float(Bphone), Bemail=Bemail)
            shipping = Shipping.objects.create(Sfirst_name=Bfirst_name, Slast_name=Blast_name, Scheckout_states=Bcheckout_states, Sstreet=Bstreet, Sapartment=Bapartment, Scity=Bcity, Szip=Bzip, Sphone=Bphone, Semail=Bemail)
            payment = Payment.objects.create(cardno=cardno, namecard=namecard, validity=validity, cvv=cvv)
            billing.save()
            payment.save()
            shipping.save()        
            return render(request, 'success.html')
        else:
            return redirect('login')
    else:
        return render(request, 'checkout.html', context)    

def our_team(request):
    context = {}
    return render(request, 'our_team.html', context)

@login_required(login_url='login')
def success(request):
    context = {}
    return render(request, 'success.html', context)

@login_required(login_url='login')
def order_success(request):
    context = {}
    if request.method == "GET":
        user = request.user
        items = UserCart.objects.filter(
            user = User.objects.filter(username = user)[0]
            )
        l = []
        for i in items:
            ll = []
            item =ItemMain.objects.filter(title = i.title)[0]
            ll.append(ItemsImages.objects.filter(title=item)[0].image)
            ll.append(i.title)
            ll.append(item.description)
            price = item.price
            offer = item.offers
            newPrice = price - (price * offer)//100
            ll.append(newPrice)
            ll.append(i.total)
            l.append(ll)
        context['items'] = l
        
    return render(request, 'order_success.html', context)
