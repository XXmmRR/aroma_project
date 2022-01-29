#from django.shortcuts import render, get_object_or_404
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.views.generic import ListView
#from django.core.mail import send_mail
#from django.db.models import Count
#from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
#from taggit.models import Tag
#from .models import Post, Comment
#from .forms import EmailPostForm, CommentForm, SearchForm

# Create your views here.


#def post_list(request, tag_slug=None):
#    object_list = Post.published.all()
#    tag = None

#    if tag_slug:
#        tag = get_object_or_404(Tag, slug=tag_slug)
#        object_list = object_list.filter(tags__in=[tag])
#
#    paginator = Paginator(object_list, 3) # 3 posts in each page
#    page = request.GET.get('page')
#    try:
#        posts = paginator.page(page)
#    except PageNotAnInteger:
#        # If page is not an integer deliver the first page
#        posts = paginator.page(1)
#    except EmptyPage:
        # If page is out of range deliver last page of results
#        posts = paginator.page(paginator.num_pages)

 #   return render(request,
  #                'blog/post/list.html',
   #               {'page': page,
    #               'posts': posts,
     #              'tag': tag})
