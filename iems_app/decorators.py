from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from iems_app.models import *


def batch_counselor_authorized(func):
    def wrap_definition(request, *args, **kwargs):
        # assuming user is already authorized
        try:
            teacher = Teacher.objects.get(user_id=request.user.id)
            counselor = BatchCounselor.objects.get(teacher=teacher)
            return func(request, *args, **kwargs)
        except ObjectDoesNotExist as e:
            return render(request, 'iems_app/unauthorized.html')

    return wrap_definition
