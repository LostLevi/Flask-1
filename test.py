import models
from models import Post
from app import db



posts = Post.query.all()
print(posts)

p2 = Post.query.filter(Post.title.contains('second')).all()

print(p2)

p3 = Post.query.filter(Post.title=='First post').all()

print(p3)
