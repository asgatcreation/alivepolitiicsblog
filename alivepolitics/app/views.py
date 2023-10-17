from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from app.models import Post,Category,Tag,Comment
from .models import Post
from.forms import CommentForm

from django.views.generic import ListView, DetailView

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

# Create your views here.



def base(request):
    return render(request, "app/base.html")



def home(request):
    popular_post = Post.objects.filter(section = 'Popular',status=1).order_by('-id')[0:4]
    recent_post = Post.objects.filter(section = 'Recent',status=1).order_by('-id')[0:4] 
    main_post = Post.objects.filter(main_post = True,status=1)[0:1] #.order_by('-id')[0:4] 
    editors_pick = Post.objects.filter(section = 'Editors_pick',status=1).order_by('-id')
    trending = Post.objects.filter(section = 'Trending',status=1).order_by('-id')
    inspiration = Post.objects.filter(section = 'Inspiration',status=1).order_by('-id')[0:2]
    inspiration = Post.objects.filter(section = 'Inspiration',status=1).order_by('-id')[0:2]
    latest_post = Post.objects.filter(section = 'Latest_Posts',status=1).order_by('-id')[0:4]
    
    category = Category.objects.all()
   
   
    
    context = {
        'popular_post':popular_post,
        'recent_post':recent_post,
        'main_post':main_post,
        'editors_pick':editors_pick,
        'trending':trending,
        'inspiration':inspiration,
        'latest_post':latest_post,
        'category':category,
        
        
        
    }
    
    return render(request, "app/index.html",context)

        # def detail(request, slug):
        #     post = Post.objects.filter(slug__iexact = slug)
        #     if post.exists():
        #         post = post.first()
        #     else:
        #         return HttpResponse('<h1>Post Not Found</h1>')
            
        #     context = {
        #         'post': post
        #    }
            
        #     return render(request, 'app/post_detail.html', context)

        # def detail(request, slug, pk):
        #     post = Post.get_post(id=pk)
        #     context = {
        #         'post': post,
        #     }
        #     return render(request, 'app/post_detail.html', context)


        # class PostDetailView(DetailView):
        #     model = Post
        #     template_name = 'post_detail.html'


        # class PostDetailView(DetailView):
        #     model = Post
        #     template_name = 'post_detail.html'
        #     context_object_name = 'post'
        #     slug_field = 'slug'
        #     slug_url_kwarg = 'slug'

        #     def get_object(self, queryset=None):
        #         slug = self.kwargs.get(self.slug_url_kwarg)
        #         queryset = queryset or self.get_queryset()
        #         return get_object_or_404(queryset, **{self.slug_field: slug})

def post_details(request, slug):
    post = Post.objects.filter(slug = slug)#get(id=pk)
    if post.exists():
        post = post.first()
    else:
        return redirect('app:404')
    
    comments = post.comments.filter(active=True)
    new_comment = None    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    # #return render(request, template_name, {'post': post,
    #                                        'comments': comments,
    #                                        'new_comment': new_comment,
    #                                        'comment_form': comment_form})
    
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form    
    }
    return render(request, "app/post_detail.html", context )


def page_not_found(request):
    return render(request, "app/404.html")