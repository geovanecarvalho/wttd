from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string
from django.conf import settings
from eventex.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(
        request,
        'subscriptions/subscription_form.html',
        {'form': SubscriptionForm()},
    )


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(
            request, 'subscriptions/subscription_form.html', {'form': form}
        )

    subscription = form.save()
    # subscription = Subscription.objects.create(**form.cleaned_data)

    # Send email
    _send_mail(
        'Confirmação de inscrição',
        settings.DEFAULT_FROM_EMAIL,
        subscription.email,
        'subscriptions/subscription_email.txt',
        {'subscription': subscription},
    )

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(
        request,
        'subscriptions/subscription_detail.html',
        {'subscription': subscription},
    )


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
