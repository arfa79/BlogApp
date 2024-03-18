from ninja import NinjaAPI
from .models import Post, Comment

api = NinjaAPI()

@api.get("/posts")
def get_posts(request):
    posts = Post.objects.all()
    return posts

@api.get("/posts/{post_id}")
def get_post(request, post_id: int):
    post = Post.objects.get(id=post_id)
    return post

@api.post("/posts")
def create_post(request, title: str, content: str):
    post = Post.objects.create(title=title, content=content)
    return post

@api.put("/posts/{post_id}")
def update_post(request, post_id: int, title: str, content: str):
    post = Post.objects.get(id=post_id)
    post.title = title
    post.content = content
    post.save()
    return post