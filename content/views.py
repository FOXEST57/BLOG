from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm
from django.contrib import messages

def articles_list(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'list.html', {'articles': articles})

def articles_details(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST) 
        if form.is_valid():
            comment = Comment(
                article=article,
                author=request.user if request.user.is_authenticated else None,
                content=form.cleaned_data['content']
            )
            comment.save()
            messages.success(request, 'Commentaire ajouté avec succès.')
        return redirect('articles_details', article_id=article.id)

    comments = article.comments.all().order_by('-created_at')
    return render(request, 'details.html', {'article': article, 'comments': comments, 'form': form})