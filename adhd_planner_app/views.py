from datetime import date

from django.shortcuts import render, redirect
from django.views import View

from adhd_planner_app.forms import AddAThingToDoForm
from adhd_planner_app.models import AddAThingToDo


class HomeView(View):
    def get(self, request):
        today = date.today()
        must_things = AddAThingToDo.objects.filter(category='MST').order_by('start_date')
        should_things = AddAThingToDo.objects.filter(category='SHOW').order_by('start_date')
        nice_things = AddAThingToDo.objects.filter(category='NICE').order_by('start_date')
        ctx = {
            'should_things': should_things,
            'must_things': must_things,
            'nice_things': nice_things,
            'today': today,
        }
        return render(request, 'home.html', ctx)


class AddAThingToDoView(View):
    def get(self, request):
        form = AddAThingToDoForm()
        return render(request, 'thing_to_do.html', {'form': form})

    def post(self, request):
        form = AddAThingToDoForm(request.POST)

        if form.is_valid():
            thing_to_do = form.save(commit=False)
            thing_to_do.save()
            return redirect('home')

        return render(request, 'thing_to_do.html', {'form': form})
