class DummyViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'API endpoint works'})