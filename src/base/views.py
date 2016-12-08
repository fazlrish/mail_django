from django.shortcuts import render

# Create your views here.
# Main page View
from django.views import generic

from base.models import Categories, Category_item
from review.forms import NewReviewForm
from review.models import Review


def index_view(request):
    template_name = "base/index.html"
    return render(request, template_name)

# Categories page View
class Categories_view(generic.ListView):
    model = Categories
    template_name = "base/categories.html"
    context_object_name = 'categories'

    def get_queryset(self):
        return Categories.objects.all()

# Category Items page View
class Category_items_view(generic.ListView):
    template_name = "base/category.html"
    context_object_name = 'categoryItemList'
    category = None

    def get_queryset(self):
        return Category_item.objects.filter(category_id=self.category.id)

    def dispatch(self, request, category_id=None, *args, **kwargs):
        self.category = Categories.objects.get(pk=category_id)
        return super(Category_items_view, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Category_items_view, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

# Category Items Detail page View
class Item_detail_view(generic.DetailView):
    template_name = "base/item_detail.html"
    context_object_name = 'item'
    model = Category_item

    def get_context_data(self, **kwargs):
        context = super(Item_detail_view, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(category_item=self.kwargs['pk'])
        context['form'] = NewReviewForm()
        return context


# def item_detail_view(request, pk):
#     template_name = "base/item_detail.html"
#     item = Category_item.objects.get(pk=pk)
#     reviews = Review.objects.filter(category_item=item)
#     if (request.method == 'POST'):
#         form = NewReviewForm(request.POST, user = request.user, category_item=Category_item.objects.get(pk=item.id))
#         if form.is_valid():
#             form.save()
#             form = NewReviewForm()
#     else:
#         form = NewReviewForm()
#     return render(request, template_name, {'category': item.category, 'item': item, 'reviews': reviews, 'form': form})