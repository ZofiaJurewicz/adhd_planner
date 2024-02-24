from django import forms

from adhd_planner_app.models import AddAThingToDo


class AddAThingToDoForm(forms.ModelForm):
    class Meta:
        model = AddAThingToDo
        fields = '__all__'