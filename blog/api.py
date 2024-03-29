from ninja import NinjaAPI
from .models import Post, Comment

api = NinjaAPI()
# Define an endpoint for getting all posts
@api.get("/posts")
def get_posts(request):
    posts = Post.objects.all()
    return posts
# Define an endpoint for getting a specific post by its ID
@api.get("/posts/{post_id}")
def get_post(request, post_id: int):
    post = Post.objects.get(id=post_id)
    return post
# Define an endpoint for creating a new post
@api.post("/posts")
def create_post(request, title: str, content: str):
    post = Post.objects.create(title=title, content=content)
    return post
# Define an endpoint for updating an existing post
@api.put("/posts/{post_id}")
def update_post(request, post_id: int, title: str, content: str):
    post = Post.objects.get(id=post_id)
    post.title = title
    post.content = content
    post.save()
    return post