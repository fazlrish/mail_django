from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from base.models import Category_item
from review.forms import NewReviewForm
from review.models import Review
# Review edit page View

def new_review_view(request):
    category_item = Category_item.objects.get(pk=request.POST['category_item'])
    if request.method == 'POST':
        form = NewReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save()
            review.category_item = category_item
            review.save()
        return redirect(request.META.get('HTTP_REFERER'))

@login_required
def review_edit_view(request, review_id):
    if (request.method=='GET'):
        form = NewReviewForm(instance=Review.objects.get(pk = review_id))
        return render(request, "review/review_edit.html", {'review_id':review_id, 'form': form})
    elif(request.method=='POST'):
        form = NewReviewForm(request.POST, user=request.user)
        review = Review.objects.get(pk=review_id)
        if form.is_valid():
            review.text = request.POST['text']
            review.save()
        return redirect(request.POST['next'])