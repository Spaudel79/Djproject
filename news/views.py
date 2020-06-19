# from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, MainMenu, SubMenu, BlogTennis,BlogNBA,BlogCricket,Club,Players,BlogEPL,BlogChampionsLeague,BlogSerieA, BlogLaLiga
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from crispy_forms.helper import FormHelper
from django.contrib.auth import login as authlog, logout
from django.contrib.auth.decorators import login_required


# class BlogListData()


# def index(request):
#     return HttpResponse("<h1>Welcome to django<h1>")
#
#
# def about(request):
#     return HttpResponse("<h1>About News page</h1>")
#
#
# def users(request, id):
#     return HttpResponse(f'users page {id}')



class Bloglistview(ListView):
    model = Blog
    template_name = 'gn.html'
    context_object_name = 'Blogdetails'

    # queryset = Blog.objects.all


class Blogdetailview(DetailView):
    template_name = 'gn-details.html'
    context_object_name = 'Blogdetails'

    def get_queryset(self):
        return Blog.objects.all()


#
# def deleteview(request):
#     content={
#         'Blogdata':Blog.objects.all()
#     }
#     return render(request, 'delete.html', content)


class Blogdeleteview(DeleteView):
    template_name = 'delete.html'
    context_object_name = 'Blogdetails'

    def get_queryset(self):
        return Blog.objects.all()

    def get_success_url(self):
        return reverse('gn')

# def deleteblog(request):
#     if request.method=='POST':
#         logout(request)
#         return redirect('blog')
#     else:
#         back_page = request.META.get('HTTP_REFERER')
#         return HttpResponse(back_page)


def index(request):
    content = {
        'title': 'TotalSport',
        'Blogdata': Blog.objects.all(),
        'BlogCricketdata': BlogCricket.objects.all(),
        'BlogNBAdata': BlogNBA.objects.all(),
        'BlogTennisdata': BlogTennis.objects.all(),
    }
    return render(request, 'index.html', content)


@login_required(login_url='login')
def users(request):
     return render(request, 'users.html')


def log_out(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    else:
        back_page = request.META.get('HTTP_REFERER')
        return HttpResponse(back_page)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get['name', False]
        message = request.POST.get['subject', False]
        email = request.POST.get['email', False]
        subject = request.POST.get['subject', False]

        if subject and message and email:
            try:
                send_mail(subject, message, email, ['laravel3pm@gmail.com'])
                message.success(request, 'Message has been send')
                return redirect('contact')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')

    else:
            # In reality we'd use a form class
            # to get proper validation errors.
            # return HttpResponse('Make sure all fields are entered and valid.')

            content = {
                'title': 'Contact'  # title is made dynamic from this
            }
    return render(request, 'contact.html', content)


def about(request):
    content = {
        'title': 'About'
    }
    return render(request, 'about.html', content)



def blog(request):
    # xyz = Blog.objects.all()
    # return HttpResponse(xyz.query)
    content = {
        'title': 'Blog',
        'Blogdata': Blog.objects.all()
    }
    return render(request, 'blog.html', content)

def blog_details(request,criteria):
    content = {
        'title': 'Blog Details ',
        'Blogdata': Blog.objects.filter(pk=criteria)

    }
    return render(request, 'blog_details.html', content)


def blog_cricket(request):

    content = {
        'title': 'Cricket',
        'Blogdata': BlogCricket.objects.all()

    }
    return render(request, 'blogcricket.html', content)

def blogcricket_details(request,criteria):
    content = {
        'title': 'Cricket ',
        'Blogdata': BlogCricket.objects.filter(pk=criteria)

    }
    return render(request, 'blogcricket-details.html', content)


def blog_nba(request):
    # xyz = Blog.objects.all()
    # return HttpResponse(xyz.query)
    content = {
        'title': 'NBA',
        'Blogdata': BlogNBA.objects.all()

    }
    return render(request, 'blognba.html', content)




def blog_tennis(request):
    # xyz = Blog.objects.all()
    # return HttpResponse(xyz.query)
    content = {
        'title': 'Tennis',
        'Blogdata': BlogTennis.objects.all()

    }
    return render(request, 'blogtennis.html', content)

def blog_epl(request):
    # xyz = Blog.objects.all()
    # return HttpResponse(xyz.query)
    content = {
        'title': 'Football-EPL',
        'Blogdata': BlogEPL.objects.all()

    }
    return render(request, 'blogepl.html', content)

def blog_seriea(request):
    # xyz = Blog.objects.all()
    # return HttpResponse(xyz.query)
    content = {
        'title': 'Football-SerieA',
        'Blogdata': BlogSerieA.objects.all()

    }
    return render(request, 'blogseriea.html', content)

def blog_laliga(request):
    # xyz = Blog.objects.all()
    # return HttpResponse(xyz.query)
    content = {
        'title': 'Football-Laliga',
        'Blogdata': BlogLaLiga.objects.all()

    }
    return render(request, 'bloglaliga.html', content)

def blog_cleague(request):
    # xyz = Blog.objects.all()
    # return HttpResponse(xyz.query)
    content = {
        'title': 'Champions League',
        'Blogdata': BlogChampionsLeague.objects.all()

    }
    return render(request, 'blogcleague.html', content)

def login(request):
    if request.method=='POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            authlog(request,user)
            return redirect('users')
        else:
            back_page= request.META.get('HTTP_REFERER')
            return HttpResponse(back_page)

    else:
        content={
                'form': AuthenticationForm()
        }
        return render(request,'login.html',content)


def sign_up(request):
    # xyz = Blog.objects.all()
    # return HttpResponse(xyz.query)
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           back_page = request.META.get('HTTP_REFERER')
           messages.success(request, 'Successfully registered')
           return redirect('sign-up')

        else:
            back_page= request.META.get('HTTP_REFERER')
            return HttpResponse(back_page)

    else:
        content={
                'form': UserCreationForm()
        }
        return render(request,'sign-up.html',content)




