from typing import List
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from eventex.core.models import Speaker, Talk


home = ListView.as_view(template_name='index.html', model=Speaker)


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    }
    return render(request, 'core/talk_list.html', context)
