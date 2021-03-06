import autopep8
from django.forms import Form, CharField
from django.http import HttpResponse
from django.views.generic import FormView


class CodeForm(Form):
    code = CharField()
    mode = CharField()


class Pep8View(FormView):
    template_name = "base.html"
    form_class = CodeForm

    def form_valid(self, form):
        mode = int(form.cleaned_data["mode"])
        clean_code = autopep8.fix_code(form.cleaned_data["code"],options={"aggressive":mode})
        return HttpResponse(clean_code)