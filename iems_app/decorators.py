from iems_app.models import Batchcounselor
def is_batchcounselor(func):
    def wrap_definition(request, *args, **kwargs):
        # assuming user is already authorized
        try:
            authorization = Batchcounselor.objects.get(user_id=request.user.id)
            return func(request, *args, **kwargs)
        except ObjectDoesNotExist as e:
            return render(request, 'iems_app/unauthorized.html')
    return wrap_definition
