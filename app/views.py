from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile,Business,Neighbourhood,Post
from .forms import UpdateUserForm, AddBusinessForm,CreateNeighbourhoodForm,CreatePostForm,AddBusinessForm
from django.contrib.auth import authenticate,login,logout
#  Create your views here.
def register(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    context= {
        'form': form,
    }
    return render(request, 'accounts/register.html',context)

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def index(request):
    neighbourhoods = Neighbourhood.objects.all()

    context={ 
        'neighbourhoods':neighbourhoods,
        }
    return render(request, 'all/index.html',context)


def updateprofile(request,id):
    profile = Profile.objects.get(user = id)
    business = Business.objects.all()
    if request.method=='POST':
        updateUserForm = UpdateUserForm(request.POST,request.FILES,instance=request.user.profile)

        if updateUserForm.is_valid():
            updateUserForm.save()

        return HttpResponseRedirect(request.path_info)

    else:
        updateUserForm = UpdateUserForm(instance = request.user.profile)

    context = {
        'updateUserForm': updateUserForm,
        'profile':profile,
        'business':business,
       
    }

    return render(request, 'all/myprofile.html', context)
        
    # neighbourhood
# Neighbourhood
def createNeighbourhood(request):
    current_user = request.user
    neighbourhoods = Neighbourhood.objects.all()
    if request.method == 'POST':
        newhoodform = CreateNeighbourhoodForm(request.POST,request.FILES)
        if newhoodform.is_valid():
            # commit=false => get model object(neighbourhood), then add your extra data and save it.
            create = newhoodform.save(commit=False)
            # one who creates neighbourhood is admin
            create.admin = current_user
            create.save()
            return redirect('index')
    else:
        newhoodform = CreateNeighbourhoodForm()
    context= {
        'newhoodform': newhoodform,
        'neighbourhoods ':neighbourhoods,
        
    }
    return render(request, 'all/newhood.html', context)


def viewneighbourhood(request,neighbourhood_id):
    current_user = request.user
    neighbourhood=Neighbourhood.objects.get(id=neighbourhood_id)
    business=Business.objects.filter(neighbourhood=neighbourhood)
    users= Profile.objects.filter(neighbourhood=neighbourhood)
    posts = Post.objects.filter(neighbourhood=neighbourhood)

    context ={
        'current_user': current_user,
        'neighbourhood':neighbourhood,
        'business': business,
        'users':users,
        'posts': posts
    }
    return render(request,'all/hood.html',context)
    
def join_neighbourhood(request,neighbourhood_id):
    neighbourhood = get_object_or_404(Neighbourhood, id=neighbourhood_id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('index')

def leave_neighbourhood(request,neighbourhood_id):
    neighbourhood = get_object_or_404(Neighbourhood, id=neighbourhood_id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()

    return redirect('index')

# def newpost(request, neighbourhood_id):
#     neighbourhood = Neighbourhood.objects.get(id=neighbourhood_id)
#     if request.method == 'POST':
#         add_post_form = CreatePostForm(request.POST,request.FILES)
#         if add_post_form.is_valid():
#             post = add_post_form.save(commit=False)
#             post.neighbourhood = neighbourhood
#             post.user = request.user
#             post.save()
#             return redirect('hood', neighbourhood.id)
#     else:
#         add_post_form = CreatePostForm()
#     return render(request, 'all/post.html', {'add_post_form': add_post_form,'neighbourhood':neighbourhood})

def newpost(request,neighbourhood_id):
    neighbourhood = Neighbourhood.objects.get(id=neighbourhood_id)
    posts = Post.objects.all()
    if request.method == 'POST':
        newpostform = CreatePostForm(request.POST,request.FILES)
        if newpostform.is_valid():
            # commit=false => get model object(post), then add your extra data and save it.
            newpost = newpostform.save(commit=False)
            # newpost is in that neighbourhood
            newpost.neighbourhood = neighbourhood
            newpost.user = request.user
            newpost.save()
            return redirect('hood',neighbourhood_id)
    else:
        newpostform = CreatePostForm()
    context= {
        'newpostform': newpostform,
        'posts ':posts,
        'neighbourhood':neighbourhood,

        
    }
    return render(request, 'all/post.html', context)


def newbusiness(request,neighbourhood_id):
    neighbourhood = Neighbourhood.objects.get(id=neighbourhood_id)
    business = Business.objects.all()
    if request.method == 'POST':
        businessform = AddBusinessForm(request.POST,request.FILES)
        if businessform.is_valid():
            # commit=false => get model object(post), then add your extra data and save it.
            new_business = businessform.save(commit=False)
            # newpost is in that neighbourhood
            new_business.neighbourhood = neighbourhood
            new_business.user = request.user
            new_business.save()
            return redirect('hood',neighbourhood_id)
    else:
        businessform = AddBusinessForm()
    context= {
        'businessform': businessform,
        'business':business,
        'neighbourhood':neighbourhood,

        
    }
    return render(request, 'all/business.html', context)

    # create,update,delete,update neighbourhood
    # get neighbourhood user
    # get single neighbourhood 
    # create,update,deletepost
    # create ,delete,update,search 