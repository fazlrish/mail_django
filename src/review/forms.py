#New Review form based on Review model
from django.forms import ModelForm
from django.forms.utils import ErrorList

from review.models import Review


class NewReviewForm(ModelForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, user=None,):
        self.user = user
        super(NewReviewForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix,
                                            empty_permitted, instance, use_required_attribute)

    class Meta:
        model = Review
        fields = ('text',)

    def save(self, commit=True):
        self.instance.user = self.user
        return super(NewReviewForm, self).save(commit=commit)