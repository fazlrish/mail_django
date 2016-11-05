from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from django.contrib.auth import authenticate, login, logout


# Main page View
def IndexView(request):
    template_name = "review_service/index.html"
    return render(request, template_name)


# Registration page View
def registration_view(request):
    if (request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username', None),
                                            email=form.cleaned_data.get('email',None),
                                            password=form.cleaned_data.get('password', None))
            user.save()
            template_name = "review_service/authorization.html"
            return render(request, template_name)

    else:
        form = UserRegistrationForm()
        template_name = "review_service/registration.html"
        return render(request, template_name, {'form': form})



# Authorization page View
def AuthorizationView(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(request, user)
            return redirect('/review_service/users/'+str(user.id))
        else:
            return render(request,'review_service/categories.html')
    else:
        form = UserAuthorizationForm()
        template_name = "review_service/authorization.html"
        return render(request, template_name, {'form': form})

def LogOutView(request):
    11111

# Categories page View
class CategoriesView(generic.ListView):
    template_name = "review_service/categories.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Categories.objects.all()


# Users page View
class UserListView(generic.ListView):
    template_name = "review_service/userList.html"
    context_object_name = "userList"

    def get_queryset(self):
        return User.objects.all()


# Category Items page View
class CategoryItemsView(generic.ListView):
    template_name = "review_service/category.html"
    context_object_name = 'categoryItemList'
    category = None;

    def get_queryset(self):
        return CategoryItem.objects.filter(category_id=self.category.id)

    def dispatch(self, request, category_id=None, *args, **kwargs):
        self.category = Categories.objects.get(pk=category_id)
        return super(CategoryItemsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryItemsView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

# Category Item detail page View
# class ItemDetailView(generic.DetailView):
#     template_name = "review_service/itemDetail.html"
#     model = CategoryItem
#     form = None
#     category = None
#     reviews = None
#
#     def dispatch(self, request, category_id=None, pk = None, *args, **kwargs):
#         self.category = Categories.objects.get(pk = category_id)
#         self.reviews = Review.objects.filter(categoryItem = pk)
#         if (request.method == 'POST'):
#             self.form = NewReviewForm(request.POST)
#             if self.form.is_valid():
#                self.form.save()
#         else:
#             self.form = NewReviewForm()
#         return super(ItemDetailView, self).dispatch(request,*args,**kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(ItemDetailView, self).get_context_data(**kwargs)
#         context['category'] = self.category
#         context['reviews'] = self.reviews
#         context['form'] = self.form

def ItemDetailView(request, category_id, pk):
    template_name = "review_service/itemDetail.html"
    item = CategoryItem.objects.get(pk=pk)
    category = Categories.objects.get(pk=category_id)
    reviews = Review.objects.filter(categoryItem=pk)
    if (request.method == 'POST'):
        form = NewReviewForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewReviewForm()
    return render(request, template_name, {'category': category, 'item': item, 'reviews': reviews, 'form': form})


# Categories page View
def UserDetailView(request, user_id):
    template_name = "review_service/userDetail.html"
    user = User.objects.get(pk=user_id)
    reviews = Review.objects.filter(user=user_id)
    return render(request, template_name, {'user': user, 'reviews': reviews})
