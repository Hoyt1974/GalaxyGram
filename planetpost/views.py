from planetpost.forms import PlanetPostForm, UserPostForm
from django.shortcuts import render, redirect
from planetpost.models import Planet_Comments, Planet_Post


def post_form_view(request):
    if request.method =="POST":
        form = PlanetPostForm(request.POST, request.FILES)
        your_post = Planet_Post.objects.create(author=request.user, post=request.POST['post'], planet_img=request.FILES['planet_img'],)
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
        
        


    

