from django.shortcuts import render, redirect
from django.views.generic.base import View

from ratings.models import Rating
from ratings.forms import RatingForm, EditForm,  formset_factory



def home(request):
    """ Show the entry point to the ratings app
    :param request: Django request object
    :return: rendered homepage
    """
    context = {'ratings': Rating.objects.all()}
    return render(request, 'home.html', context)


class RatingCreate(View):
    """ Create a new Rating """
    form_class = RatingForm
    template_name = 'ratings/rating_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            _ = form.save()
            return redirect(home)
        return render(request, self.template_name, {'form: form'})

class EditRating(View):
    """ Edit one or al ratings """

    form_class = RatingForm
    template_name = 'ratings/edit_rating.html'

    def get(self, request):
        data = {
         'form-TOTAL_FORMS': '10',
         'form-INITIAL_FORMS': '5',
         'form-MAX_NUM_FORMS': '',
         'form-0-title': '',
         'form-0-pub_date': '',
         'ratings': Rating.objects.all()
        }
        """context = {'ratings': Rating.objects.values()}"""
        EditFormSet = formset_factory(RatingForm, extra = 0)
        formset = EditFormSet(initial=Rating.objects.all().values())
        return render(request, self.template_name, {'formset': formset})

    def post(self, request):
        data = {
         'form-TOTAL_FORMS': '10',
         'form-INITIAL_FORMS': '5',
         'form-MAX_NUM_FORMS': '',
         'form-0-title': '',
         'form-0-pub_date': '',
         'ratings': Rating.objects.all()
        }
        EditFormSet = formset_factory(RatingForm, extra = 0)
        formset = EditFormSet(initial=Rating.objects.all().values())
        for form in formset:
            print(form.as_table()) 
            form.save()      
        return redirect(home)

        


