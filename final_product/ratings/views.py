from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

from ratings.models import Rating
from ratings.forms import RatingForm, formset_factory, modelformset_factory

def home(request):
    """ Show the entry point to the ratings app
    :param request: Django request object
    :return: rendered homepage
    """
    """ Moved create rating logic to here"""
    form_class = RatingForm
    form = form_class
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            _ = form.save()
            return redirect(home)
    context = {'ratings': Rating.objects.all(), 'form': form}
    return render(request, 'home.html', context)

class RatingDelete(View):
    """ We delete a request by notes, which is probably the most unique key"""
    def post(self, request):
        rname = request.POST['name']
        rnotes = request.POST['notes']
        Rating.objects.filter(notes=rnotes).delete()
        return redirect(home)

class EditRating(View):
    """ Edit a rating """
    form_class = RatingForm
    template_name = 'ratings/edit_rating.html'
    EditFormSet = None
    formset = None

    def get(self, request):
        """ Use modelformset to pre-populate form"""
        self.EditFormSet = modelformset_factory(Rating, fields=('beer_name', 'score', 'brewer_name', 'notes'),  max_num=len(Rating.objects.all()),extra = 0)    
        self.formset = self.EditFormSet(initial=Rating.objects.all().values()) 
        return render(request, self.template_name, {'formset': self.formset})

    def post(self, request):
        if 'rname' in request.POST:
            """get values from ajax post"""
            ename = request.POST['rname']
            rbrewer = request.POST['brewer']
            rscore = request.POST['score']
            rnotes = request.POST['notes']
            rrow = request.POST['row']
            rsuccess = request.POST['success']
            """iterate for the proper row number and update it with the new values"""
            if(int(rsuccess) == 1):  
                RatingNum = 1
                for each in Rating.objects.all():   
                    if(RatingNum == int(rrow)):
                        each.beer_name = ename
                        each.score = rscore
                        each.brewer_name = rbrewer
                        each.notes = rnotes
                        each.save()
                    RatingNum = RatingNum + 1
                return render(request, self.template_name, {'formset': self.formset}) 
            else: 
                print("blank values detected")
                return render(request, self.template_name, {'formset': self.formset})
        return redirect(home)
