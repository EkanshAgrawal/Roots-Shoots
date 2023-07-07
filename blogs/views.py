from django.shortcuts import render, redirect
from .models import BlogPlant, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def blog_home(request):
    context = {
        "blogs": BlogPlant.objects.all(),
        "tags": {
        'plant': 'PLANT TALK',
        'gardening': 'GARDENING DIY\'S',
        'styling' : 'PLANTS STYLING',
        'kitchen' : 'KITCHEN GARDENING',
        'development' : 'SUSTAINABLE DEVELOPEMENT'
        }
    }
    return render(request, "blogs/blog_home.html", context)

@login_required(login_url='login')
def blog_upload(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            author = User.objects.get(username = request.user.username)
            blog_title = request.POST['blog_title']
            blog_content = request.POST['blog_content']
            blog_image = request.FILES['blog_image']
            category = Category.objects.get(category = request.POST['category'])
            blog = BlogPlant.objects.create(author=author, blog_title=blog_title, blog_content=blog_content, blog_image=blog_image, category=category)
            blog.save()
            return render(request, 'blogs/blog_upload.html')
        else:
            return redirect('login')
    else:
        return render(request, 'blogs/blog_upload.html')

@login_required(login_url='login')
def blog_details(request, the_slug):
    blog = BlogPlant.objects.filter(slug=the_slug)
    return render(request, 'blogs/blog_details.html', {'blog': blog[0]})
