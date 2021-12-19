from iems_app.models import Authorization

def registration_authorized(func):
    def wrap_definition(request, *args, **kwargs):
        # assuming user is already authorized
        try:
            authorization = Authorization.objects.get(user_id=request.user.id)
            return func(request, *args, **kwargs)
        except ObjectDoesNotExist as e:
            return render(request, 'unauthorized.html')
    return wrap_definition
