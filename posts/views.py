from django.shortcuts import render

from .models import Post 

# part 1 to display all posts
def index(request):
    # query/get all post objects, filter by featured
    queryset = Post.objects.filter(featured=True)
    context = {
        'object_list' : queryset
    }
    return render(request, 'index.html', context)

def blog(request):
	return render(request, 'blog.html')

def post(request):
	return render(request, 'post.html')