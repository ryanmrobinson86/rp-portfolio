from django.shortcuts import render
from blog.models import Category, Post, Comment

# Create your views here.
def blog_index(request):
	posts = Post.objects.all().order_by('-created_on')
	context = {
		'posts': posts,
	}
	return render(request, 'blog_index.html', context)


def blog_category(request, category):
	posts = Post.objects.filter(
		categories_name_contains=category,
	).order_by(
		'-created_on'
	)
	context = {
		'category': category,
		'posts': posts,
	}
	return render(request, 'blog_category.html', context)


def blog_detail(request, key):
	post = Posts.objects.get(pk=key)
	comments = Comments.objects.filter(post=post)
	context = {
		'post': post,
		'comments': comments,
	}
	return render(request, 'blog_detail.html', context)
