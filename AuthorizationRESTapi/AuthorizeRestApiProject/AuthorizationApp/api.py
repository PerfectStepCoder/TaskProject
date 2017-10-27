from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from django.http import HttpResponse

from .models import User


class UserResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'name': 'name',
        'email': 'email',
        'type': 'type',
        'password': 'password'
    })

    # GET /api/posts/ (but not hooked up yet)
    def list(self):
        print("GET query")
        return User.objects.all()

    # GET /api/posts/<pk>/ (but not hooked up yet)
    def detail(self, pk):
        return User.objects.get(id=pk)

    def is_debug(self):
        return True

    def is_authenticated(self):
        return True
        #return self.request.user.is_authenticated()

    # Add new user!
    def create(self):
        print("POST query")
        new_user = {arr[0]: arr[1] for arr in map(lambda x: x.split('='), str(self.body, "utf-8").split('\n'))}
        User.objects.create(
            name=new_user['name'],
            email=new_user['email'],
            type=new_user['type'],
            password=new_user['password']
        )
        return HttpResponse({'success': True})

    # GET
    def login(self):
        return User.objects.get(name=self.GET["name"])


    def logout(self):
        pass
