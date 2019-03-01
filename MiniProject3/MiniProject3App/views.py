from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from .forms import NewTimecardForm
from .models import  Timecard

# function that lists all entries in the database
def index(request):
    allTimecards = Timecard.objects.all()
    return render(request, "MiniProject3App/index.html", {'timecard_list': allTimecards})

# This page will provide a form to add timecards
def timecards(request):
    new_form = NewTimecardForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')#redirect goes to another page
    # injecting...
    return render(request, 'MiniProject3App/index.html', {'selectedteacherinfo': new_form})

# this function is used to edit timecards
def edittimecard(request, id):
    timecard = get_object_or_404(Timecard, pk=id)
    edit_form = NewTimecardForm(request.POST or None, instance=timecard)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')
    return render(request, 'MiniProject3App/edit.html', {'timecardform': edit_form})
# this function is used to delete contacts
def deletetimecard(request,id):
    user = get_object_or_404(Timecard, pk=id)
    if request.method == 'POST':
        timecards.delete()
        return redirect('index')

    return render(request, 'MiniProject3App/delete.html', {'selectedtimecards': timecards })
