from blog.helper import save_file
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from blog.models import Profile, Blog, User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    message_value = "Hello, world. my first blog application"
    context = {"message": message_value}
    return render(request, "home.html", context)


def log_in(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Email: {email}, Password: {password}")

        # check if email exists in database
        if not User.objects.filter(email=email).exists():
            messages.error(request, message="Email does not exists in record")
            return redirect("login")

        # check if email and password is correct
        user_query = User.objects.get(email=email)
        username = None
        if user_query:
            username = user_query.username   # get username from User table
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, message="Email or Password is incorrect")
            return redirect("login")
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email_id = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        print(f"""First Name: {first_name}, Last Name: {last_name}, 
                Email: {email_id}, Password: {password}, 
                Confirm Password: {confirm_password}
                """)
        if password != confirm_password:
            messages.error(request, message="Password and Repeat Password does not match")
            return redirect("register")

        if User.objects.filter(email=email_id).exists():
            messages.error(request, message="Email already exists")
            return redirect("register")

        # insert user data to database table User
        user_data = {"username": email_id, "email": email_id}
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        profile_data = {"user": user, "firstname": first_name, "lastname": last_name}
        # insert user data to database table Profile
        profile = Profile.objects.create(**profile_data)
        return redirect("login")
    return render(request, "register.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def blogs(request):
    blogs = Blog.objects.all().order_by("-created_at")
    context = {"blogs": blogs}
    return render(request, "blog.html", context)


@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        blog_image = request.FILES.get("blog_image")
        image_url = save_file(request, blog_image)
        blog_data = {"title": title, "description": content, "image": image_url, "user": request.user}
        print(blog_data)
        Blog.objects.create(**blog_data)  # insert data to database table blog.
        return redirect("list_blogs")
    return render(request, "create_blog.html")


@login_required
def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {"blog": blog}
    return render(request, "blog-single.html", context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/login")
