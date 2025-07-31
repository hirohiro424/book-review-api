from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author

# ========================
# 📘 Book Templates
# ========================

class BookTemplateListView(View):
    def get(self, request):
        return render(request, 'books/list.html')

class BookTemplateCreateView(View):
    def get(self, request):
        return render(request, 'books/create.html')

class BookTemplateUpdateView(View):
    def get(self, request, pk):
        return render(request, 'books/update.html', {'book_id': pk})

class BookTemplateDetailView(View):
    def get(self, request, pk):
        return render(request, 'books/detail.html', {'book_id': pk})


# ========================
# 💬 Review Templates
# ========================

class ReviewTemplateListView(View):
    def get(self, request):
        return render(request, 'reviews/list.html')

class ReviewTemplateCreateView(View):
    def get(self, request):
        return render(request, 'reviews/create.html')

class ReviewTemplateUpdateView(View):
    def get(self, request, pk):
        return render(request, 'reviews/update.html', {'review_id': pk})

class ReviewTemplateDetailView(View):
    def get(self, request, pk):
        return render(request, 'reviews/detail.html', {'review_id': pk})


# ========================
# 🖋️ Author Templates
# ========================

class AuthorTemplateListView(View):
    def get(self, request):
        return render(request, 'authors/list.html')

class AuthorTemplateCreateView(View):
    def get(self, request):
        return render(request, 'authors/create.html')

    def post(self, request):
        name = request.POST.get('name')
        if name:
            Author.objects.create(name=name)
        return redirect('author_list')

class AuthorTemplateUpdateView(View):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return render(request, 'authors/update.html', {'author': author})

    def post(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        name = request.POST.get('name')
        if name:
            author.name = name
            author.save()
        return redirect('author_list')

class AuthorTemplateDeleteView(View):
    def post(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return redirect('author_list')
