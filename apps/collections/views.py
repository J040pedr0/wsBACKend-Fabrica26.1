from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
import requests
from .models import Collection, Characteristic, Userfavorite
from .serializers import CollectionSerializer, CharacteristicSerializer, UserfavoriteSerializer 
from .models import Collection, Characteristic, Userfavorite


# coleções
class CollectionListCreateView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # serve para o usuario ver sua coleção e a coleção publica.
        return Collection.objects.filter(owner=self.request.user) | Collection.objects.filter(is_public=True)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # impedindo que o usuário acesse coleções de outros usuários
        return Collection.objects.filter(owner=self.request.user) 
# personagens

class CharacteristicListCreateView(generics.ListCreateAPIView):
    serializer_class = CharacteristicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Characteristic.objects.filter(added_by=self.request.user )

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class CharacteristicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Characteristic.objects.filter(added_by=self.request.user)
    
class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = UserfavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Userfavorite.objects.filter(user=self.request.user)


class FavoriteDeleteView(generics.DestroyAPIView):
    queryset = Userfavorite.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Userfavorite.objects.filter(user=self.request.user)

# consumindo API (Rick and Morty)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])

def search_rick_and_morty(request):
    name = request.query_params.get('name','')
    url = f'https://rickandmortyapi.com/api/character/?name={name}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results = []
            for item in data.get('results', []):
                results.append({
                    'external_id': item['id'],
                    'name': item['name'],
                    'status': item['status'],
                    'species': item['species'],
                    'gender': item['gender'],
                    'origin_name': item['origin']['name'],
                    'location_name': item['location']['name'],
                    'episode_count': len(item['episode']),
                })
            return Response(results, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'NENHUM PERSONAGEM ENCONTRADO '}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR )
    


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def import_characters_from_api(request):
    external_id = request.data.get('external_id')
    collection_ids = request.data.get('collection_ids',[])
    if not external_id:
        return Response({'Error': 'external_id é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
    url = f'https://rickandmortyapi.com/api/character/{external_id}'
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return Response({'Error': 'Personagem não encontrado na API externa'}, status=status.HTTP_404_NOT_FOUND)
        api_data = response.json()
    except Exception as e:
        return Response({'Error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    character, created = Characteristic.objects.get_or_create(
        external_id=api_data['id'],
        defaults={
            'name': api_data['name'],
            'status': api_data['status'],
            'species': api_data['species'],
            'gender': api_data['gender'],
            'image': api_data['image'],
            'origin_name': api_data['origin']['name'],
            'location_name': api_data['location']['name'],
            'added_by': request.user,
        }
    )
    if collection_ids:
        collections = Collection.objects.filter(id__in=collection_ids, owner=request.user)
        character.collections.add(*collections)
    serializer = CharacteristicSerializer(character, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)

