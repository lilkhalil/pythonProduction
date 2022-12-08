from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from .models import HTMLtext
from .serializers import HTMLtextSerializers
import htmltext
import validators

# Create your views here.
class HTMLtextView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='url', 
                description='URL of the HTML page', 
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'Official GitHub Page',
                        value='https://github.com'
                    ),
                    OpenApiExample(
                        'RTU MIREA Login Page',
                        value='https://online-edu.mirea.ru/my'
                    ),
                    OpenApiExample(
                        'Official RTU MIREA Page',
                        value='https://www.mirea.ru/'
                    )
                ],
                required=True
            ),
        ],
        request=None,
        responses={
            200: OpenApiResponse(
                response=HTMLtextSerializers,
                description='Succesfully retrieved'
            )
        },
        description='Returns text fragments between HTML tags in JSON format',
        methods=['GET']
    )
    def get(self, request):
        url = request.GET.get('url')
        
        if not validators.url(url):
            return Response('URL is incorrect', status=400)

        result = HTMLtext(url, htmltext.gettext(url)['value'])

        serializer_for_request = HTMLtextSerializers(instance=result)

        return Response(serializer_for_request.data)