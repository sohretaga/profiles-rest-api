from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Tets Api View"""

    def get(self, response, format=None):
        api = [
            'test text'
        ]

        return Response({'message': 'Hello', 'api': api})