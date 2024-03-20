from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .models import Comment, Post, PostSettings,Author



# Create your views here.
def index(request):
    print(request.user.id)
    if request.user.id is None:
        return render(request, 'index.html')

    context = {
        "post_list": Post.objects.all()
    }
    # print(f"""{Post.objects
    #          .exclude(text__isnull=True)
    #          .exclude(text__exact='').all()}""")#.order_by('-text').first()}")
    
        # post = Post()
        # post.title = form_data['title']
        # post.text = form_data['text']
        # post.save()
    return render(request, 'index.html', context=context)

def detail(request, post_id):
    # _post = Post.objects.filter(pk=post_id).first()
    # if _post is None:
    #     # 404
    #     ...

    _post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=_post)

    context = {"post": _post, "comments": comments}
    return render(request, "detail.html", context=context)


def create(request):
    if request.method == "POST":
        form_data = request.POST
        post_settings, _ = PostSettings.objects.get_or_create()
        title=form_data['title']
        text=form_data['text']
        if len(text) > post_settings.text_len or len(title) > post_settings.title_len:
            ...
        else: 
            author, _ = Author.objects.get_or_create(name=request.user.id)
            post = Post(text=text, title=title, author=author)
            post.save()
            

    return redirect('index')
    
def create_comment(request, post_id):
    if request.method == "POST":
        form_data = request.POST
        # post_id = form_data.get("post_id")
        text = form_data.get("text")
        author, _ = Author.objects.get_or_create(name=request.user.id)
        post = Post.objects.filter(pk=post_id).first()
        comment = Comment(text=text, post=post, author=author)
        comment.save()
        return redirect('detail', post_id=post_id)
    return render(request, "create_comment.html", context={'post_id':post_id})
