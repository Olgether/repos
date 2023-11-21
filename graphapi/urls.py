from django.urls import path

from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView

from .schemas import schema  


# Переопределяем метод execute_graphql_request, 
# чтобы добавить дополнительную логику перед 
# выполнением запроса GraphQL. 
class CustomGraphQLView(GraphQLView): 
    def execute_graphql_request(self, request, 
        data, query, variables, operation_name, 
        show_graphiql=False):
        return super().execute_graphql_request(
            request, data, query, variables, 
            operation_name, show_graphiql
        )

@login_required(login_url='/login')
def graphql_view(request):
    # Создаем экземпляр CustomGraphQLView с передачей параметров 
    # graphiql=True и schema=schema.
    view = CustomGraphQLView.as_view(graphiql=True, schema=schema)
    # Вызываем представление view, передавая объект 
    # request для обработки запроса GraphQL.
    return view(request)


urlpatterns = [
    path('', graphql_view),
]