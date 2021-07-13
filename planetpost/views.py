from planetpost.forms import PlanetPostForm, UserPostForm
from django.shortcuts import render, redirect, get_object_or_404
from planetpost.models import Planet_Comments, Planet_Post
from planetmodel.models import Body

def post_form_view(request):
    if request.method =="POST":
        # body=Body.objects.get(id=planet_id)
        form = PlanetPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            your_post = Planet_Post.objects.create(author=request.user, post=data.get('post'), body=data.get('body'), planet_img=data.get('planet_img'))
        return redirect("post", your_post.pk)
    form = PlanetPostForm()
    return render(request, 'generic_form.html', {'form': form})

def planet_post_detail(request, post_id: int):
    post = Planet_Post.objects.get(id=post_id)
    comments = Planet_Comments.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

def add_comment(request, post_id: int):
    post = Planet_Post.objects.get(id=post_id)
    if request.method == "POST":
        form = UserPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post", post_id)
    form = UserPostForm()
    return render(request, 'generic_form.html', {'form': form})

def post_list(request):
    posts = Planet_Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def upvote_view(request, post_id):
    vote = Planet_Post.objects.get(id=post_id)
    vote.total_votes += 1
    vote.up_vote += 1
    vote.save()
    return redirect(request.META['HTTP_REFERER'])


def downvote_view(request, post_id):
    vote = Planet_Post.objects.get(id=post_id)
    vote.total_votes -= 1
    vote.down_vote += 1
    vote.save()
    return redirect(request.META['HTTP_REFERER'])

def total_vote(request):
    votes = Planet_Post.objects.all().order_by('-total_votes')
    return render(request, "post_detail.html", {"votes": votes})
        
        
def comment_upvote_view(request, comment_id):
    vote = Planet_Comments.objects.get(id=comment_id)
    vote.total_votes += 1
    vote.up_vote += 1
    vote.save()
    return redirect(request.META['HTTP_REFERER'])


def comment_downvote_view(request, comment_id):
    vote = Planet_Comments.objects.get(id=comment_id)
    vote.total_votes -= 1
    vote.down_vote += 1
    vote.save()
    return redirect(request.META['HTTP_REFERER'])

def comment_total_vote(request):
    votez = Planet_Comments.objects.all().order_by('-total_votes')
    return render(request, "post_detail.html", {"votez": votez})


def comment_edit(request, comment_id):
    comment = get_object_or_404(Planet_Comments, id=comment_id)
    # if request.user is the same as comment.author:
    if request.method == "POST":
        form = UserPostForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.author = request.user
            comment.save()
            return redirect("post", comment.post.id)
    else:
        form = UserPostForm(instance=comment)
    return render(request, "generic_form.html", {"form": form})


    

