from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
import requests
from .models import Collection, Characteristic, Userfavorite
from .forms import CollectionForm
from apps.accounts.forms import CustomUserCreationForm

# Views de autenticação
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'collections/home.html')

@login_required
def my_collections_view(request):
    collections = Collection.objects.filter(owner=request.user)
    return render(request, 'collections/my_collections.html', {'collections': collections})

@login_required
def collection_detail_view(request, pk):
    collection = get_object_or_404(
        Collection.objects.filter(owner=request.user) | Collection.objects.filter(is_public=True),
        pk=pk
    )

    return render(request, 'collections/collection_detail.html', {
        'collection': collection
    })

@login_required
def create_collection_view(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.owner = request.user
            collection.save()
            messages.success(request, 'Coleção criada com sucesso!')
            return redirect('my_collections')
    else:
        form = CollectionForm()
    return render(request, 'collections/collection_form.html', {'form': form, 'title': 'Nova Coleção'})

@login_required
def edit_collection_view(request, pk):
    collection = get_object_or_404(Collection, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            messages.success(request, 'Coleção atualizada!')
            return redirect('collection_detail', pk=collection.pk)
    else:
        form = CollectionForm(instance=collection)
    return render(request, 'collections/collection_form.html', {'form': form, 'collection': collection, 'title': 'Editar Coleção'})

@login_required
def delete_collection_view(request, pk):
    collection = get_object_or_404(Collection, pk=pk, owner=request.user)
    if request.method == 'POST':
        collection.delete()
        messages.success(request, 'Coleção excluída!')
        return redirect('my_collections')
    return render(request, 'collections/collection_confirm_delete.html', {'collection': collection})

@login_required
def search_characters_view(request):
    name = request.GET.get('name', '')
    collection_id = request.GET.get('collection_id')
    characters = []
    if name:
        url = f'https://rickandmortyapi.com/api/character/?name={name}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for item in data.get('results', []):
                    characters.append({
                        'external_id': item['id'],
                        'name': item['name'],
                        'status': item['status'],
                        'species': item['species'],
                        'gender': item['gender'],
                        'image': item['image'],
                        'origin_name': item['origin']['name'],
                        'location_name': item['location']['name'],
                        'episode_count': len(item['episode'])
                    })
        except Exception as e:
            messages.error(request, f'Erro na busca: {e}')
    return render(request, 'collections/search_characters.html', {
        'characters': characters,
        'collection_id': collection_id,
        'name': name
    })

@login_required
def import_character_view(request):
    if request.method == 'POST':
        external_id = request.POST.get('external_id')
        collection_id = request.POST.get('collection_id')
        if not external_id:
            messages.error(request, 'ID do personagem não fornecido.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        url = f'https://rickandmortyapi.com/api/character/{external_id}'
        try:
            response = requests.get(url)
            if response.status_code != 200:
                messages.error(request, 'Personagem não encontrado.')
                return redirect(request.META.get('HTTP_REFERER', '/'))
            api_data = response.json()
        except Exception as e:
            messages.error(request, f'Erro na requisição: {e}')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        # Cria ou atualiza
        character, created = Characteristic.objects.update_or_create(
            external_id=external_id,
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
        # Adiciona à coleção se especificado
        if collection_id:
            try:
                collection = Collection.objects.get(id=collection_id, owner=request.user)
                character.collections.add(collection)
                messages.success(request, f'Personagem {character.name} adicionado à coleção {collection.name}.')
            except Collection.DoesNotExist:
                messages.warning(request, 'Coleção não encontrada ou não pertence a você.')
        else:
            messages.success(request, f'Personagem {character.name} importado com sucesso!')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect('home')
@login_required
def remove_character_from_collection(request, collection_id, character_id):
        collection = get_object_or_404(Collection, id=collection_id, owner=request.user)
        character = get_object_or_404(Characteristic, id=character_id)
        # Remove o personagem da coleção (ManyToMany)
        collection.characteristics.remove(character)
        messages.success(request, f'Personagem {character.name} removido da coleção {collection.name}.')
        return redirect('collection_detail', pk=collection.id)