from django.shortcuts import reverse
from .models import MySimpleModel
from .forms import Form
from django.views.generic import FormView


class View(FormView):
    template_name = 'django_app/index.html'
    form_class = Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texts'] = MySimpleModel.objects.all()
        return context

    def form_valid(self, form):
        self.success_url = self.success_url or reverse('view')
        MySimpleModel.objects.create(text=form.data['text'])
        return super().form_valid(form)
