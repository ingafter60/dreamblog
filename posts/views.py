from django.shortcuts import render

from .models import Post 
from marketing.models import Signup

# # part 1 to display all posts
# def index(request):
#     # query/get all post objects, filter by featured
#     queryset = Post.objects.filter(featured=True)
#     context = {
#         'object_list' : queryset
#     }
#     return render(request, 'index.html', context)

# # part 2 to display all posts and latest posts
# def index(request):
#     # query/get all post objects, filter by featured
#     featured = Post.objects.filter(featured=True)
#     latest   = Post.objects.order_by('-timestamp')[0:3]

#     context = {
#         'object_list' : featured,
#         'latest'      : latest
#     }

#     return render(request, 'index.html', context)

# part 3 to display all posts and latest posts
def index(request):
    # query/get all post objects, filter by featured
    featured = Post.objects.filter(featured=True)
    latest   = Post.objects.order_by('-timestamp')[0:3]

    # Subscribe to Newsletter
    # get email from the request
    if request.method == "POST":
        email = request.POST["email"]
        # get the signup object
        new_signup = Signup()
        # use the email to singup
        new_signup.email = email
        # save the email
        new_signup.save()

    context = {
        'object_list' : featured,
        'latest'      : latest
    }
    
    return render(request, 'index.html', context)

def blog(request):
	return render(request, 'blog.html')

def post(request):
	return render(request, 'post.html')