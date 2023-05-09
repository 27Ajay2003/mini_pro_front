from rest_framework.response import Response
from rest_framework.views import APIView


class ApiOverviewAV(APIView):
    def get(self, request, format=None):
        overview = [
            "Define later.",
        ]
        return Response(overview)