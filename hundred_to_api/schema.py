from graphene_django_cruddals import DjangoProjectCruddals

class HundredToApiProjectCruddals( DjangoProjectCruddals ):
    class Meta:
        apps = "__all__"

schema = HundredToApiProjectCruddals.schema

