from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from .models import (
    Pokemon, Movimiento, Habilidad, Tipo, Categoria,
    Generacion, Grupo_Huevo, PokemonTipo, PokemonHabilidad,
    PokemonMovimiento, PokemonCategoria, PokemonGeneracion,
    PokemonGrupoHuevo, Naturaleza, Puntos_Base, Evolucion
)
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import generic
from django.urls import reverse_lazy
from .forms import (
    PokemonForm, MovimientoForm, HabilidadForm, TipoForm,
    CategoriaForm, GeneracionForm, GrupoHuevoForm, PokemonTipoForm,
    PokemonHabilidadForm, PokemonMovimientoForm, PokemonCategoriaForm,
    PokemonGeneracionForm, PokemonGrupoHuevoForm, NaturalezaForm,
    PuntosBaseForm, EvolucionForm
)
from django.template.loader import render_to_string

# API view for CRUD operations


@csrf_exempt
def pokemon_crud(request):
    if request.method == 'GET':
        pokemons = Pokemon.objects.all().values()
        return JsonResponse(list(pokemons), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        pokemon = Pokemon.objects.create(**data)
        return JsonResponse({'No_Pokemon': pokemon.No_Pokemon,
                            'message': 'Pokemon created successfully'}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        pokemon_id = data.get('No_Pokemon')
        try:
            pokemon = Pokemon.objects.get(No_Pokemon=pokemon_id)
            for key, value in data.items():
                if key != 'No_Pokemon':
                    setattr(pokemon, key, value)
            pokemon.save()
            return JsonResponse({'message': 'Pokemon updated successfully'})
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        pokemon_id = data.get('No_Pokemon')
        try:
            pokemon = Pokemon.objects.get(No_Pokemon=pokemon_id)
            pokemon.delete()
            return JsonResponse({'message': 'Pokemon deleted successfully'})
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# API endpoints for other models


@csrf_exempt
def movimiento_crud(request):
    if request.method == 'GET':
        movimientos = Movimiento.objects.all().values()
        return JsonResponse(list(movimientos), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        movimiento = Movimiento.objects.create(**data)
        return JsonResponse(
            {'id': movimiento.id, 'message': 'Movimiento created successfully'}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        movimiento_id = data.get('id')
        try:
            movimiento = Movimiento.objects.get(id=movimiento_id)
            for key, value in data.items():
                if key != 'id':
                    setattr(movimiento, key, value)
            movimiento.save()
            return JsonResponse({'message': 'Movimiento updated successfully'})
        except Movimiento.DoesNotExist:
            return JsonResponse({'error': 'Movimiento not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        movimiento_id = data.get('id')
        try:
            movimiento = Movimiento.objects.get(id=movimiento_id)
            movimiento.delete()
            return JsonResponse({'message': 'Movimiento deleted successfully'})
        except Movimiento.DoesNotExist:
            return JsonResponse({'error': 'Movimiento not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def habilidad_crud(request):
    if request.method == 'GET':
        habilidades = Habilidad.objects.all().values()
        return JsonResponse(list(habilidades), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        habilidad = Habilidad.objects.create(**data)
        return JsonResponse(
            {'id': habilidad.id, 'message': 'Habilidad created successfully'}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        habilidad_id = data.get('id')
        try:
            habilidad = Habilidad.objects.get(id=habilidad_id)
            for key, value in data.items():
                if key != 'id':
                    setattr(habilidad, key, value)
            habilidad.save()
            return JsonResponse({'message': 'Habilidad updated successfully'})
        except Habilidad.DoesNotExist:
            return JsonResponse({'error': 'Habilidad not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        habilidad_id = data.get('id')
        try:
            habilidad = Habilidad.objects.get(id=habilidad_id)
            habilidad.delete()
            return JsonResponse({'message': 'Habilidad deleted successfully'})
        except Habilidad.DoesNotExist:
            return JsonResponse({'error': 'Habilidad not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def tipo_crud(request):
    if request.method == 'GET':
        tipos = Tipo.objects.all().values()
        return JsonResponse(list(tipos), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        tipo = Tipo.objects.create(**data)
        return JsonResponse(
            {'id': tipo.id, 'message': 'Tipo created successfully'}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        tipo_id = data.get('id')
        try:
            tipo = Tipo.objects.get(id=tipo_id)
            for key, value in data.items():
                if key != 'id':
                    setattr(tipo, key, value)
            tipo.save()
            return JsonResponse({'message': 'Tipo updated successfully'})
        except Tipo.DoesNotExist:
            return JsonResponse({'error': 'Tipo not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        tipo_id = data.get('id')
        try:
            tipo = Tipo.objects.get(id=tipo_id)
            tipo.delete()
            return JsonResponse({'message': 'Tipo deleted successfully'})
        except Tipo.DoesNotExist:
            return JsonResponse({'error': 'Tipo not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def categoria_crud(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all().values()
        return JsonResponse(list(categorias), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        categoria = Categoria.objects.create(**data)
        return JsonResponse(
            {'id': categoria.id, 'message': 'Categoria created successfully'}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        categoria_id = data.get('id')
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            for key, value in data.items():
                if key != 'id':
                    setattr(categoria, key, value)
            categoria.save()
            return JsonResponse({'message': 'Categoria updated successfully'})
        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'Categoria not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        categoria_id = data.get('id')
        try:
            categoria = Categoria.objects.get(id=categoria_id)
            categoria.delete()
            return JsonResponse({'message': 'Categoria deleted successfully'})
        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'Categoria not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def generacion_crud(request):
    if request.method == 'GET':
        generaciones = Generacion.objects.all().values()
        return JsonResponse(list(generaciones), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        generacion = Generacion.objects.create(**data)
        return JsonResponse(
            {'id': generacion.id, 'message': 'Generacion created successfully'}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        generacion_id = data.get('id')
        try:
            generacion = Generacion.objects.get(id=generacion_id)
            for key, value in data.items():
                if key != 'id':
                    setattr(generacion, key, value)
            generacion.save()
            return JsonResponse({'message': 'Generacion updated successfully'})
        except Generacion.DoesNotExist:
            return JsonResponse({'error': 'Generacion not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        generacion_id = data.get('id')
        try:
            generacion = Generacion.objects.get(id=generacion_id)
            generacion.delete()
            return JsonResponse({'message': 'Generacion deleted successfully'})
        except Generacion.DoesNotExist:
            return JsonResponse({'error': 'Generacion not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def grupo_huevo_crud(request):
    if request.method == 'GET':
        grupos_huevo = Grupo_Huevo.objects.all().values()
        return JsonResponse(list(grupos_huevo), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        grupo_huevo = Grupo_Huevo.objects.create(**data)
        return JsonResponse(
            {'id': grupo_huevo.id, 'message': 'Grupo Huevo created successfully'}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        grupo_huevo_id = data.get('id')
        try:
            grupo_huevo = Grupo_Huevo.objects.get(id=grupo_huevo_id)
            for key, value in data.items():
                if key != 'id':
                    setattr(grupo_huevo, key, value)
            grupo_huevo.save()
            return JsonResponse(
                {'message': 'Grupo Huevo updated successfully'})
        except Grupo_Huevo.DoesNotExist:
            return JsonResponse({'error': 'Grupo Huevo not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        grupo_huevo_id = data.get('id')
        try:
            grupo_huevo = Grupo_Huevo.objects.get(id=grupo_huevo_id)
            grupo_huevo.delete()
            return JsonResponse(
                {'message': 'Grupo Huevo deleted successfully'})
        except Grupo_Huevo.DoesNotExist:
            return JsonResponse({'error': 'Grupo Huevo not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def pokemon_tipo_crud(request):
    if request.method == 'GET':
        pokemon_tipos = PokemonTipo.objects.all().values()
        return JsonResponse(list(pokemon_tipos), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        pokemon_id = data.get('pokemon_id')
        tipo_id = data.get('tipo_id')
        try:
            pokemon = Pokemon.objects.get(No_Pokemon=pokemon_id)
            tipo = Tipo.objects.get(id=tipo_id)
            pokemon_tipo = PokemonTipo.objects.create(
                pokemon=pokemon, tipo=tipo)
            return JsonResponse(
                {'id': pokemon_tipo.id, 'message': 'Pokemon Tipo created successfully'}, status=201)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)
        except Tipo.DoesNotExist:
            return JsonResponse({'error': 'Tipo not found'}, status=404)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        pokemon_tipo_id = data.get('id')
        try:
            pokemon_tipo = PokemonTipo.objects.get(id=pokemon_tipo_id)
            if 'pokemon_id' in data:
                pokemon_tipo.pokemon = Pokemon.objects.get(
                    No_Pokemon=data['pokemon_id'])
            if 'tipo_id' in data:
                pokemon_tipo.tipo = Tipo.objects.get(id=data['tipo_id'])
            pokemon_tipo.save()
            return JsonResponse(
                {'message': 'Pokemon Tipo updated successfully'})
        except PokemonTipo.DoesNotExist:
            return JsonResponse(
                {'error': 'Pokemon Tipo not found'}, status=404)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)
        except Tipo.DoesNotExist:
            return JsonResponse({'error': 'Tipo not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        pokemon_tipo_id = data.get('id')
        try:
            pokemon_tipo = PokemonTipo.objects.get(id=pokemon_tipo_id)
            pokemon_tipo.delete()
            return JsonResponse(
                {'message': 'Pokemon Tipo deleted successfully'})
        except PokemonTipo.DoesNotExist:
            return JsonResponse(
                {'error': 'Pokemon Tipo not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def pokemon_habilidad_crud(request):
    if request.method == 'GET':
        pokemon_habilidades = PokemonHabilidad.objects.all().values()
        return JsonResponse(list(pokemon_habilidades), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        pokemon_id = data.get('pokemon_id')
        habilidad_id = data.get('habilidad_id')
        try:
            pokemon = Pokemon.objects.get(No_Pokemon=pokemon_id)
            habilidad = Habilidad.objects.get(id=habilidad_id)
            pokemon_habilidad = PokemonHabilidad.objects.create(
                pokemon=pokemon, habilidad=habilidad)
            return JsonResponse(
                {'id': pokemon_habilidad.id, 'message': 'Pokemon Habilidad created successfully'}, status=201)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)
        except Habilidad.DoesNotExist:
            return JsonResponse({'error': 'Habilidad not found'}, status=404)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        pokemon_habilidad_id = data.get('id')
        try:
            pokemon_habilidad = PokemonHabilidad.objects.get(
                id=pokemon_habilidad_id)
            if 'pokemon_id' in data:
                pokemon_habilidad.pokemon = Pokemon.objects.get(
                    No_Pokemon=data['pokemon_id'])
            if 'habilidad_id' in data:
                pokemon_habilidad.habilidad = Habilidad.objects.get(
                    id=data['habilidad_id'])
            pokemon_habilidad.save()
            return JsonResponse(
                {'message': 'Pokemon Habilidad updated successfully'})
        except PokemonHabilidad.DoesNotExist:
            return JsonResponse(
                {'error': 'Pokemon Habilidad not found'}, status=404)
        except Pokemon.DoesNotExist:
            return JsonResponse({'error': 'Pokemon not found'}, status=404)
        except Habilidad.DoesNotExist:
            return JsonResponse({'error': 'Habilidad not found'}, status=404)

    elif request.method == 'DELETE':
        data = json.loads(request.body)
        pokemon_habilidad_id = data.get('id')
        try:
            pokemon_habilidad = PokemonHabilidad.objects.get(
                id=pokemon_habilidad_id)
            pokemon_habilidad.delete()
            return JsonResponse(
                {'message': 'Pokemon Habilidad deleted successfully'})
        except PokemonHabilidad.DoesNotExist:
            return JsonResponse(
                {'error': 'Pokemon Habilidad not found'}, status=404)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# Class-based views for Pokemon


class PokemonListView(generic.ListView):
    model = Pokemon
    template_name = 'pokedex/pokemon_list.html'
    context_object_name = 'pokemons'


class PokemonDetailView(generic.DetailView):
    model = Pokemon
    template_name = 'pokedex/pokemon_detail.html'
    context_object_name = 'pokemon'
    pk_url_kwarg = 'no_pokemon'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon = self.get_object()

        # Get types with ordering to ensure consistent display
        context['tipos'] = PokemonTipo.objects.filter(
    pokemon=pokemon).select_related('tipo').order_by('id')

        # Calculate type effectiveness
        context['type_effectiveness'] = pokemon.calculate_type_effectiveness()
        
        # Get all available types for the effectiveness chart
        context['all_types'] = Tipo.objects.all().order_by('Nombre_Tipo')
        
        # Get other related data
        context['habilidades'] = PokemonHabilidad.objects.filter(
            pokemon=pokemon)
        context['movimientos'] = PokemonMovimiento.objects.filter(
            pokemon=pokemon)
        context['categorias'] = PokemonCategoria.objects.filter(
            pokemon=pokemon)
        context['generaciones'] = PokemonGeneracion.objects.filter(
            pokemon=pokemon)
        context['grupos_huevo'] = PokemonGrupoHuevo.objects.filter(
            pokemon=pokemon)
            
        # Get the stats with nature effects if available
        try:
            puntos_base = pokemon.puntos_base
            context['puntos_base'] = puntos_base
            context['stats_with_nature'] = puntos_base.get_stats_with_nature()
            context['stat_percentages'] = puntos_base.get_stat_percentages()
        except Puntos_Base.DoesNotExist:
            context['puntos_base'] = None
            context['stats_with_nature'] = None
            context['stat_percentages'] = None
        
        # Get evolutionary chain data
        evoluciona_de = pokemon.evolucion_de.all().select_related('pokemon')
        evoluciona_a = pokemon.evoluciones.all().select_related('pokemon_evolucion')
        
        context['evoluciona_de'] = evoluciona_de
        context['evoluciona_a'] = evoluciona_a
        
        # Check if this Pokémon is part of a larger evolutionary chain
        context['tiene_evolucion'] = evoluciona_de.exists() or evoluciona_a.exists()
            
        return context


class PokemonCreateView(generic.CreateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = 'pokedex/pokemon_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'¡Pokémon {self.object.Nombre} ha sido registrado exitosamente en la Pokédex!')
        return response

    def get_success_url(self):
        # Redirect to home page instead of detail page
        return reverse_lazy('index')


class PokemonUpdateView(generic.UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = 'pokedex/pokemon_form.html'
    pk_url_kwarg = 'no_pokemon'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Pokémon {self.object.Nombre} ha sido actualizado exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={
                            'no_pokemon': self.object.No_Pokemon})


class PokemonDeleteView(generic.DeleteView):
    model = Pokemon
    template_name = 'pokedex/pokemon_confirm_delete.html'
    success_url = reverse_lazy('pokemon_list')
    pk_url_kwarg = 'no_pokemon'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Check if this is an HTMX request (for the modal)
        if request.headers.get('HX-Request'):
            return render(
                request, 'pokedex/pokemon_delete_modal.html', {'pokemon': self.object})

        # Regular request (full page)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pokemon_name = self.object.Nombre

        # Perform the delete
        response = super().post(request, *args, **kwargs)

        # Add success message
        messages.success(
    request,
     f'Pokémon {pokemon_name} ha sido eliminado correctamente.')

        return response

# Class-based views for Movimiento


class MovimientoListView(generic.ListView):
    model = Movimiento
    template_name = 'pokedex/movimiento_list.html'
    context_object_name = 'movimientos'

    def render_to_response(self, context, **response_kwargs):
        # Check if this is an API request
        if self.request.path.startswith('/api/'):
            movimientos = list(self.get_queryset().values())
            return JsonResponse(movimientos, safe=False)
        return super().render_to_response(context, **response_kwargs)


class MovimientoDetailView(generic.DetailView):
    model = Movimiento
    template_name = 'pokedex/movimiento_detail.html'
    context_object_name = 'movimiento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movimiento = self.get_object()
        context['pokemons'] = PokemonMovimiento.objects.filter(
            movimiento=movimiento)
        # Añadir el campo de descripción para poder mostrarlo en texto negro
        context['descripcion'] = movimiento.Descripcion
        return context


class MovimientoCreateView(generic.CreateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'pokedex/movimiento_form.html'

    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            # Mejora la respuesta para que se visualice adecuadamente
            response = JsonResponse({
                "message": "Use POST method to create new Movimiento",
                "fields": {
                    "id": "BigAutoField (automático)",
                    "Nombre_Movimiento": "CharField (obligatorio)",
                    "Precision": "IntegerField (obligatorio)",
                    "Potencia": "IntegerField (obligatorio)",
                    "Categoria": "CharField (Físico, Especial, Estado)",
                    "Puntos_Uso": "IntegerField (obligatorio)"
                },
                "example": {
                    "Nombre_Movimiento": "Rayo Solar",
                    "Precision": 100,
                    "Potencia": 120,
                    "Categoria": "Especial",
                    "Puntos_Uso": 10
                }
            }, json_dumps_params={'indent': 4})

            # Añadir encabezados para una mejor presentación
            response['Content-Type'] = 'application/json'
            return response

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                data = json.loads(request.body)
                movimiento = Movimiento.objects.create(**data)
                return JsonResponse({
                    'id': movimiento.id,
                    'message': 'Movimiento created successfully'
                }, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Movimiento {self.object.nombre} ha sido creado exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('movimiento_detail', kwargs={'pk': self.object.id})


class MovimientoUpdateView(generic.UpdateView):
    model = Movimiento
    form_class = MovimientoForm
    template_name = 'pokedex/movimiento_form.html'

    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                movimiento = self.get_object()
                return JsonResponse({
                    "id": movimiento.id,
                    "nombre": movimiento.nombre,
                    "Descripcion": movimiento.Descripcion,
                    # Add other fields as needed
                })
            except Movimiento.DoesNotExist:
                return JsonResponse(
                    {'error': 'Movimiento not found'}, status=404)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle API requests with POST for updates (for compatibility)
        if request.path.startswith('/api/'):
            return self.put(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                movimiento = self.get_object()
                data = json.loads(request.body)
                for key, value in data.items():
                    if key != 'id':
                        setattr(movimiento, key, value)
                movimiento.save()
                return JsonResponse(
                    {'message': 'Movimiento updated successfully'})
            except Movimiento.DoesNotExist:
                return JsonResponse(
                    {'error': 'Movimiento not found'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().put(request, *args, **kwargs) if hasattr(super(),
                     'put') else HttpResponse(status=405)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Movimiento {self.object.nombre} ha sido actualizado exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('movimiento_detail', kwargs={'pk': self.object.id})


class MovimientoDeleteView(generic.DeleteView):
    model = Movimiento
    template_name = 'pokedex/movimiento_confirm_delete.html'
    success_url = reverse_lazy('movimiento_list')

# Class-based views for Habilidad


class HabilidadListView(generic.ListView):
    model = Habilidad
    template_name = 'pokedex/habilidad_list.html'
    context_object_name = 'habilidades'

    def render_to_response(self, context, **response_kwargs):
        # Check if this is an API request
        if self.request.path.startswith('/api/'):
            habilidades = list(self.get_queryset().values())
            return JsonResponse(habilidades, safe=False)
        return super().render_to_response(context, **response_kwargs)


class HabilidadDetailView(generic.DetailView):
    model = Habilidad
    template_name = 'pokedex/habilidad_detail.html'
    context_object_name = 'habilidad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        habilidad = self.get_object()
        context['pokemons'] = PokemonHabilidad.objects.filter(
            habilidad=habilidad)
        # Añadir el campo de descripción para poder mostrarlo en texto negro
        context['descripcion'] = habilidad.Descripcion
        return context


class HabilidadCreateView(generic.CreateView):
    model = Habilidad
    form_class = HabilidadForm
    template_name = 'pokedex/habilidad_form.html'

    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            # Mejora la respuesta para que se visualice adecuadamente
            response = JsonResponse({
                "message": "Use POST method to create new Habilidad",
                "fields": {
                    "id": "BigAutoField (automático)",
                    "Nombre_Habilidad": "CharField (obligatorio)",
                    "Descripcion": "TextField (opcional)"
                },
                "example": {
                    "Nombre_Habilidad": "Presión",
                    "Descripcion": "Aumenta el consumo de PP del oponente."
                }
            }, json_dumps_params={'indent': 4})

            # Añadir encabezados para una mejor presentación
            response['Content-Type'] = 'application/json'
            return response

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                data = json.loads(request.body)
                habilidad = Habilidad.objects.create(**data)
                return JsonResponse({
                    'id': habilidad.id,
                    'message': 'Habilidad created successfully'
                }, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Habilidad {self.object.Nombre_Habilidad} ha sido creada exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('habilidad_detail', kwargs={'pk': self.object.id})


class HabilidadUpdateView(generic.UpdateView):
    model = Habilidad
    form_class = HabilidadForm
    template_name = 'pokedex/habilidad_form.html'

    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                habilidad = self.get_object()
                return JsonResponse({
                    "id": habilidad.id,
                    "nombre": habilidad.nombre,
                    "Descripcion": habilidad.Descripcion,
                    # Add other fields as needed
                })
            except Habilidad.DoesNotExist:
                return JsonResponse(
                    {'error': 'Habilidad not found'}, status=404)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle API requests with POST for updates (for compatibility)
        if request.path.startswith('/api/'):
            return self.put(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                habilidad = self.get_object()
                data = json.loads(request.body)
                for key, value in data.items():
                    if key != 'id':
                        setattr(habilidad, key, value)
                habilidad.save()
                return JsonResponse(
                    {'message': 'Habilidad updated successfully'})
            except Habilidad.DoesNotExist:
                return JsonResponse(
                    {'error': 'Habilidad not found'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().put(request, *args, **kwargs) if hasattr(super(),
                     'put') else HttpResponse(status=405)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Habilidad {self.object.nombre} ha sido actualizada exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('habilidad_detail', kwargs={'pk': self.object.id})


class HabilidadDeleteView(generic.DeleteView):
    model = Habilidad
    template_name = 'pokedex/habilidad_confirm_delete.html'
    success_url = reverse_lazy('habilidad_list')

# Class-based views for Tipo


class TipoListView(generic.ListView):
    model = Tipo
    template_name = 'pokedex/tipo_list.html'
    context_object_name = 'tipos'

    def render_to_response(self, context, **response_kwargs):
        # Check if this is an API request
        if self.request.path.startswith('/api/'):
            tipos = list(self.get_queryset().values())
            return JsonResponse(tipos, safe=False)
        return super().render_to_response(context, **response_kwargs)


class TipoDetailView(generic.DetailView):
    model = Tipo
    template_name = 'pokedex/tipo_detail.html'
    context_object_name = 'tipo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo = self.get_object()
        context['pokemons'] = PokemonTipo.objects.filter(tipo=tipo)
        # Remove reference to non-existent Descripcion field
        return context


class TipoCreateView(generic.CreateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'pokedex/tipo_form.html'

    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            # Mejora la respuesta para que se visualice adecuadamente
            response = JsonResponse({
                "message": "Use POST method to create new Tipo",
                "fields": {
                    "id": "BigAutoField (automático)",
                    "Nombre_Tipo": "CharField (obligatorio)",
                    "Color": "CharField (opcional)"
                },
                "example": {
                    "Nombre_Tipo": "Fuego",
                    "Color": "#FF4500"
                }
            }, json_dumps_params={'indent': 4})

            # Añadir encabezados para una mejor presentación
            response['Content-Type'] = 'application/json'
            return response

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                data = json.loads(request.body)
                tipo = Tipo.objects.create(**data)
                return JsonResponse({
                    'id': tipo.id,
                    'message': 'Tipo created successfully'
                }, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Tipo {self.object.Nombre_Tipo} ha sido creado exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('tipo_detail', kwargs={'pk': self.object.id})


class TipoUpdateView(generic.UpdateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'pokedex/tipo_form.html'

    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                tipo = self.get_object()
                return JsonResponse({
                    "id": tipo.id,
                    "Nombre_Tipo": tipo.Nombre_Tipo,
                    "Color": tipo.Color,
                    # Add other fields as needed
                })
            except Tipo.DoesNotExist:
                return JsonResponse({'error': 'Tipo not found'}, status=404)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle API requests with POST for updates (for compatibility)
        if request.path.startswith('/api/'):
            return self.put(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                tipo = self.get_object()
                data = json.loads(request.body)
                for key, value in data.items():
                    if key != 'id':
                        setattr(tipo, key, value)
                tipo.save()
                return JsonResponse({'message': 'Tipo updated successfully'})
            except Tipo.DoesNotExist:
                return JsonResponse({'error': 'Tipo not found'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().put(request, *args, **kwargs) if hasattr(super(),
                     'put') else HttpResponse(status=405)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Tipo {self.object.Nombre_Tipo} ha sido actualizado exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('tipo_detail', kwargs={'pk': self.object.id})


class TipoDeleteView(generic.DeleteView):
    model = Tipo
    template_name = 'pokedex/tipo_confirm_delete.html'
    success_url = reverse_lazy('tipo_list')

# Class-based views for Categoria


class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = 'pokedex/categoria_list.html'
    context_object_name = 'categorias'

    def render_to_response(self, context, **response_kwargs):
        # Check if this is an API request
        if self.request.path.startswith('/api/'):
            categorias = list(self.get_queryset().values())
            return JsonResponse(categorias, safe=False)
        return super().render_to_response(context, **response_kwargs)


class CategoriaDetailView(generic.DetailView):
    model = Categoria
    template_name = 'pokedex/categoria_detail.html'
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = self.get_object()
        context['pokemons'] = PokemonCategoria.objects.filter(
            categoria=categoria)
        # Removed reference to non-existent Descripcion field
        return context


class CategoriaCreateView(generic.CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'pokedex/categoria_form.html'

    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            # Mejora la respuesta para que se visualice adecuadamente
            response = JsonResponse({
                "message": "Use POST method to create new Categoria",
                "fields": {
                    "id": "BigAutoField (automático)",
                    "Nombre_Categoria": "CharField (obligatorio)"
                },
                "example": {
                    "Nombre_Categoria": "Legendario"
                }
            }, json_dumps_params={'indent': 4})

            # Añadir encabezados para una mejor presentación
            response['Content-Type'] = 'application/json'
            return response

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                data = json.loads(request.body)
                categoria = Categoria.objects.create(**data)
                return JsonResponse({
                    'id': categoria.id,
                    'message': 'Categoria created successfully'
                }, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Categoría {self.object.nombre} ha sido creada exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('categoria_detail', kwargs={'pk': self.object.id})


class CategoriaUpdateView(generic.UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'pokedex/categoria_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
    self.request,
     f'Categoría {self.object.nombre} ha sido actualizada exitosamente!')
        return response

    def get_success_url(self):
        return reverse_lazy('categoria_detail', kwargs={'pk': self.object.id})


class CategoriaDeleteView(generic.DeleteView):
    model = Categoria
    template_name = 'pokedex/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = self.get_object()
        context['pokemons'] = categoria.pokemon.all()
        return context

# Class-based views for Generacion


class GeneracionListView(generic.ListView):
    model = Generacion
    template_name = 'pokedex/generacion_list.html'
    context_object_name = 'generaciones'

    def render_to_response(self, context, **response_kwargs):
        # Check if this is an API request
        if self.request.path.startswith('/api/'):
            generaciones = list(self.get_queryset().values())
            return JsonResponse(generaciones, safe=False)
        return super().render_to_response(context, **response_kwargs)


class GeneracionDetailView(generic.DetailView):
    model = Generacion
    template_name = 'pokedex/generacion_detail.html'
    context_object_name = 'generacion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        generacion = self.get_object()
        context['pokemons'] = PokemonGeneracion.objects.filter(
            generacion=generacion)
        # La clase Generacion no tiene un atributo Descripcion
        # context['descripcion'] = generacion.Descripcion
        return context


class GeneracionCreateView(generic.CreateView):
    model = Generacion
    form_class = GeneracionForm
    template_name = 'pokedex/generacion_form.html'

    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            # Mejora la respuesta para que se visualice adecuadamente
            response = JsonResponse({
                "message": "Use POST method to create new Generacion",
                "fields": {
                    "id": "BigAutoField (automático)",
                    "Juegos": "CharField (obligatorio)",
                    "Numero": "IntegerField (opcional)"
                },
                "example": {
                    "Juegos": "Rojo, Azul y Verde",
                    "Numero": 1
                }
            }, json_dumps_params={'indent': 4})

            # Añadir encabezados para una mejor presentación
            response['Content-Type'] = 'application/json'
            return response

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                data = json.loads(request.body)
                generacion = Generacion.objects.create(**data)
                return JsonResponse({
                    'id': generacion.id,
                    'message': 'Generacion created successfully'
                }, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Generación {self.object.Juegos} ha sido creada exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('generacion_detail', kwargs={'pk': self.object.id})

class GeneracionUpdateView(generic.UpdateView):
    model = Generacion
    form_class = GeneracionForm
    template_name = 'pokedex/generacion_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Generación {self.object.Juegos} ha sido actualizada exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('generacion_detail', kwargs={'pk': self.object.id})

class GeneracionDeleteView(generic.DeleteView):
    model = Generacion
    template_name = 'pokedex/generacion_confirm_delete.html'
    success_url = reverse_lazy('generacion_list')

# Class-based views for Naturaleza


class NaturalezaListView(generic.ListView):
    model = Naturaleza
    template_name = 'pokedex/naturaleza_list.html'
    context_object_name = 'naturalezas'


class NaturalezaDetailView(generic.DetailView):
    model = Naturaleza
    template_name = 'pokedex/naturaleza_detail.html'
    context_object_name = 'naturaleza'


class NaturalezaCreateView(generic.CreateView):
    model = Naturaleza
    form_class = NaturalezaForm
    template_name = 'pokedex/naturaleza_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Naturaleza {self.object.nombre} ha sido creada exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('naturaleza_detail', kwargs={'pk': self.object.id})


class NaturalezaUpdateView(generic.UpdateView):
    model = Naturaleza
    form_class = NaturalezaForm
    template_name = 'pokedex/naturaleza_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Naturaleza {self.object.nombre} ha sido actualizada exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('naturaleza_detail', kwargs={'pk': self.object.id})


class NaturalezaDeleteView(generic.DeleteView):
    model = Naturaleza
    template_name = 'pokedex/naturaleza_confirm_delete.html'
    success_url = reverse_lazy('naturaleza_list')

# Class-based views for Grupo_Huevo
class GrupoHuevoListView(generic.ListView):
    model = Grupo_Huevo
    template_name = 'pokedex/grupo_huevo_list.html'
    context_object_name = 'grupos_huevo'
    
    def render_to_response(self, context, **response_kwargs):
        # Check if this is an API request
        if self.request.path.startswith('/api/'):
            grupos_huevo = list(self.get_queryset().values())
            return JsonResponse(grupos_huevo, safe=False)
        return super().render_to_response(context, **response_kwargs)

class GrupoHuevoDetailView(generic.DetailView):
    model = Grupo_Huevo
    template_name = 'pokedex/grupo_huevo_detail.html'
    context_object_name = 'grupo_huevo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo_huevo = self.get_object()
        context['pokemons'] = PokemonGrupoHuevo.objects.filter(grupo_huevo=grupo_huevo)
        # La clase Grupo_Huevo no tiene un atributo Descripcion
        # context['descripcion'] = grupo_huevo.Descripcion
        return context

class GrupoHuevoCreateView(generic.CreateView):
    model = Grupo_Huevo
    form_class = GrupoHuevoForm
    template_name = 'pokedex/grupo_huevo_form.html'
    
    def get(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            # Mejora la respuesta para que se visualice adecuadamente
            response = JsonResponse({
                "message": "Use POST method to create new Grupo Huevo",
                "fields": {
                    "id": "BigAutoField (automático)",
                    "nombre_huevo": "CharField (obligatorio)"
                },
                "example": {
                    "nombre_huevo": "Monstruo"
                }
            }, json_dumps_params={'indent': 4})
            
            # Añadir encabezados para una mejor presentación
            response['Content-Type'] = 'application/json'
            return response
            
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        # Handle API requests
        if request.path.startswith('/api/'):
            try:
                data = json.loads(request.body)
                grupo_huevo = Grupo_Huevo.objects.create(**data)
                return JsonResponse({
                    'id': grupo_huevo.id, 
                    'message': 'Grupo Huevo created successfully'
                }, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Grupo Huevo {self.object.nombre_huevo} ha sido creado exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('grupo_huevo_detail', kwargs={'pk': self.object.id})

class GrupoHuevoUpdateView(generic.UpdateView):
    model = Grupo_Huevo
    form_class = GrupoHuevoForm
    template_name = 'pokedex/grupo_huevo_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Grupo Huevo {self.object.nombre_huevo} ha sido actualizado exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('grupo_huevo_detail', kwargs={'pk': self.object.id})

class GrupoHuevoDeleteView(generic.DeleteView):
    model = Grupo_Huevo
    template_name = 'pokedex/grupo_huevo_confirm_delete.html'
    success_url = reverse_lazy('grupo_huevo_list')

# Class-based views for Puntos_Base
class PuntosBaseListView(generic.ListView):
    model = Puntos_Base
    template_name = 'pokedex/puntos_base_list.html'
    context_object_name = 'puntos_base'

class PuntosBaseDetailView(generic.DetailView):
    model = Puntos_Base
    template_name = 'pokedex/puntos_base_detail.html'
    context_object_name = 'puntos_base'

class PuntosBaseCreateView(generic.CreateView):
    model = Puntos_Base
    form_class = PuntosBaseForm
    template_name = 'pokedex/puntos_base_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Puntos Base para {self.object.pokemon.Nombre} han sido creados exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})
        
    def get_initial(self):
        initial = super().get_initial()
        if 'pokemon' in self.request.GET:
            try:
                pokemon = Pokemon.objects.get(No_Pokemon=self.request.GET['pokemon'])
                initial['pokemon'] = pokemon
            except (ValueError, Pokemon.DoesNotExist):
                pass
        return initial

class PuntosBaseUpdateView(generic.UpdateView):
    model = Puntos_Base
    form_class = PuntosBaseForm
    template_name = 'pokedex/puntos_base_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Puntos Base para {self.object.pokemon.Nombre} han sido actualizados exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})

class PuntosBaseDeleteView(generic.DeleteView):
    model = Puntos_Base
    template_name = 'pokedex/puntos_base_confirm_delete.html'
    success_url = reverse_lazy('puntos_base_list')

# Class-based views for relationship models
# PokemonTipo views
class PokemonTipoListView(generic.ListView):
    model = PokemonTipo
    template_name = 'pokedex/pokemon_tipo_list.html'
    context_object_name = 'pokemon_tipos'

class PokemonTipoCreateView(generic.CreateView):
    model = PokemonTipo
    form_class = PokemonTipoForm
    template_name = 'pokedex/pokemon_tipo_form.html'
    
    def form_valid(self, form):
        # Check if this Pokemon already has this type
        pokemon = form.cleaned_data["pokemon"]
        tipo = form.cleaned_data["tipo"]
        
        # Check if there's already a record for this Pokemon-Tipo combination
        existing_record = PokemonTipo.objects.filter(pokemon=pokemon, tipo=tipo).first()
        
        if (existing_record):
            messages.warning(self.request, f'El tipo {tipo} ya está asignado a {pokemon}')
            return redirect('pokemon_detail', no_pokemon=pokemon.No_Pokemon)
            
        response = super().form_valid(form)
        messages.success(self.request, f'Tipo {tipo} asignado a {pokemon} correctamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})
        
    def get_initial(self):
        initial = super().get_initial()
        if 'pokemon' in self.request.GET:
            try:
                pokemon = Pokemon.objects.get(No_Pokemon=self.request.GET['pokemon'])
                initial['pokemon'] = pokemon
            except (ValueError, Pokemon.DoesNotExist):
                pass
        return initial

class PokemonTipoUpdateView(generic.UpdateView):
    model = PokemonTipo
    form_class = PokemonTipoForm
    template_name = 'pokedex/pokemon_tipo_form.html'
    
    def get_success_url(self):
        return reverse_lazy('pokemon_tipo_list')

class PokemonTipoDeleteView(generic.DeleteView):
    model = PokemonTipo
    template_name = 'pokedex/pokemon_tipo_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        pokemon = self.object.pokemon
        tipo = self.object.tipo
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, f'Tipo {tipo.Nombre_Tipo} eliminado correctamente de {pokemon.Nombre}.')
        return redirect(success_url)

# PokemonHabilidad views
class PokemonHabilidadListView(generic.ListView):
    model = PokemonHabilidad
    template_name = 'pokedex/pokemon_habilidad_list.html'
    context_object_name = 'pokemon_habilidades'

class PokemonHabilidadCreateView(generic.CreateView):
    model = PokemonHabilidad
    form_class = PokemonHabilidadForm
    template_name = 'pokedex/pokemon_habilidad_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Habilidad {form.cleaned_data["habilidad"]} asignada a {form.cleaned_data["pokemon"]} correctamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})
        
    def get_initial(self):
        initial = super().get_initial()
        if 'pokemon' in self.request.GET:
            try:
                pokemon = Pokemon.objects.get(No_Pokemon=self.request.GET['pokemon'])
                initial['pokemon'] = pokemon
            except (ValueError, Pokemon.DoesNotExist):
                pass
        return initial

class PokemonHabilidadUpdateView(generic.UpdateView):
    model = PokemonHabilidad
    form_class = PokemonHabilidadForm
    template_name = 'pokedex/pokemon_habilidad_form.html'
    success_url = reverse_lazy('pokemon_habilidad_list')

class PokemonHabilidadDeleteView(generic.DeleteView):
    model = PokemonHabilidad
    template_name = 'pokedex/pokemon_habilidad_confirm_delete.html'
    success_url = reverse_lazy('pokemon_habilidad_list')

# PokemonMovimiento views
class PokemonMovimientoListView(generic.ListView):
    model = PokemonMovimiento
    template_name = 'pokedex/pokemon_movimiento_list.html'
    context_object_name = 'pokemon_movimientos'

class PokemonMovimientoCreateView(generic.CreateView):
    model = PokemonMovimiento
    form_class = PokemonMovimientoForm
    template_name = 'pokedex/pokemon_movimiento_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Movimiento {form.cleaned_data["movimiento"]} asignado a {form.cleaned_data["pokemon"]} correctamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})
        
    def get_initial(self):
        initial = super().get_initial()
        if 'pokemon' in self.request.GET:
            try:
                pokemon = Pokemon.objects.get(No_Pokemon=self.request.GET['pokemon'])
                initial['pokemon'] = pokemon
            except (ValueError, Pokemon.DoesNotExist):
                pass
        return initial

class PokemonMovimientoUpdateView(generic.UpdateView):
    model = PokemonMovimiento
    form_class = PokemonMovimientoForm
    template_name = 'pokedex/pokemon_movimiento_form.html'
    success_url = reverse_lazy('pokemon_movimiento_list')

class PokemonMovimientoDeleteView(generic.DeleteView):
    model = PokemonMovimiento
    template_name = 'pokedex/pokemon_movimiento_confirm_delete.html'
    success_url = reverse_lazy('pokemon_movimiento_list')

# PokemonCategoria views
class PokemonCategoriaListView(generic.ListView):
    model = PokemonCategoria
    template_name = 'pokedex/pokemon_categoria_list.html'
    context_object_name = 'pokemon_categorias'

class PokemonCategoriaCreateView(generic.CreateView):
    model = PokemonCategoria
    form_class = PokemonCategoriaForm
    template_name = 'pokedex/pokemon_categoria_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Categoría {form.cleaned_data["categoria"]} asignada a {form.cleaned_data["pokemon"]} correctamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})
        
    def get_initial(self):
        initial = super().get_initial()
        if 'pokemon' in self.request.GET:
            try:
                pokemon = Pokemon.objects.get(No_Pokemon=self.request.GET['pokemon'])
                initial['pokemon'] = pokemon
            except (ValueError, Pokemon.DoesNotExist):
                pass
        return initial

class PokemonCategoriaUpdateView(generic.UpdateView):
    model = PokemonCategoria
    form_class = PokemonCategoriaForm
    template_name = 'pokedex/pokemon_categoria_form.html'
    success_url = reverse_lazy('pokemon_categoria_list')

class PokemonCategoriaDeleteView(generic.DeleteView):
    model = PokemonCategoria
    template_name = 'pokedex/pokemon_categoria_confirm_delete.html'
    success_url = reverse_lazy('pokemon_categoria_list')
    success_url = reverse_lazy('pokemon_categoria_list')

# PokemonGeneracion views
class PokemonGeneracionListView(generic.ListView):
    model = PokemonGeneracion
    template_name = 'pokedex/pokemon_generacion_list.html'
    context_object_name = 'pokemon_generaciones'

class PokemonGeneracionCreateView(generic.CreateView):
    model = PokemonGeneracion
    form_class = PokemonGeneracionForm
    template_name = 'pokedex/pokemon_generacion_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Generación {form.cleaned_data["generacion"]} asignada a {form.cleaned_data["pokemon"]} correctamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})
        
    def get_initial(self):
        initial = super().get_initial()
        if 'pokemon' in self.request.GET:
            try:
                pokemon = Pokemon.objects.get(No_Pokemon=self.request.GET['pokemon'])
                initial['pokemon'] = pokemon
            except (ValueError, Pokemon.DoesNotExist):
                pass
        return initial

class PokemonGeneracionUpdateView(generic.UpdateView):
    model = PokemonGeneracion
    form_class = PokemonGeneracionForm
    template_name = 'pokedex/pokemon_generacion_form.html'
    success_url = reverse_lazy('pokemon_generacion_list')

class PokemonGeneracionDeleteView(generic.DeleteView):
    model = PokemonGeneracion
    template_name = 'pokedex/pokemon_generacion_confirm_delete.html'
    success_url = reverse_lazy('pokemon_generacion_list')

# PokemonGrupoHuevo views
class PokemonGrupoHuevoListView(generic.ListView):
    model = PokemonGrupoHuevo
    template_name = 'pokedex/pokemon_grupo_huevo_list.html'
    context_object_name = 'pokemon_grupos_huevo'

class PokemonGrupoHuevoCreateView(generic.CreateView):
    model = PokemonGrupoHuevo
    form_class = PokemonGrupoHuevoForm
    template_name = 'pokedex/pokemon_grupo_huevo_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Grupo Huevo {form.cleaned_data["grupo_huevo"]} asignado a {form.cleaned_data["pokemon"]} correctamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('pokemon_detail', kwargs={'no_pokemon': self.object.pokemon.No_Pokemon})
        
    def get_initial(self):
        initial = super().get_initial()
        if 'pokemon' in self.request.GET:
            try:
                pokemon = Pokemon.objects.get(No_Pokemon=self.request.GET['pokemon'])
                initial['pokemon'] = pokemon
            except (ValueError, Pokemon.DoesNotExist):
                pass
        return initial

class PokemonGrupoHuevoUpdateView(generic.UpdateView):
    model = PokemonGrupoHuevo
    form_class = PokemonGrupoHuevoForm
    template_name = 'pokedex/pokemon_grupo_huevo_form.html'
    success_url = reverse_lazy('pokemon_grupo_huevo_list')

class PokemonGrupoHuevoDeleteView(generic.DeleteView):
    model = PokemonGrupoHuevo
    template_name = 'pokedex/pokemon_grupo_huevo_confirm_delete.html'
    success_url = reverse_lazy('pokemon_grupo_huevo_list')

# Class-based views for Evolucion
class EvolucionListView(generic.ListView):
    model = Evolucion
    template_name = 'pokedex/evolucion_list.html'
    context_object_name = 'evoluciones'


class EvolucionDetailView(generic.DetailView):
    model = Evolucion
    template_name = 'pokedex/evolucion_detail.html'
    context_object_name = 'evolucion'


class EvolucionCreateView(generic.CreateView):
    model = Evolucion
    form_class = EvolucionForm
    template_name = 'pokedex/evolucion_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        pokemon = form.cleaned_data["pokemon"]
        pokemon_evolucion = form.cleaned_data["pokemon_evolucion"]
        messages.success(self.request, f'Evolución de {pokemon.Nombre} a {pokemon_evolucion.Nombre} ha sido creada exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('evolucion_detail', kwargs={'pk': self.object.id})


class EvolucionUpdateView(generic.UpdateView):
    model = Evolucion
    form_class = EvolucionForm
    template_name = 'pokedex/evolucion_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        pokemon = form.cleaned_data["pokemon"]
        pokemon_evolucion = form.cleaned_data["pokemon_evolucion"]
        messages.success(self.request, f'Evolución de {pokemon.Nombre} a {pokemon_evolucion.Nombre} ha sido actualizada exitosamente!')
        return response
    
    def get_success_url(self):
        return reverse_lazy('evolucion_detail', kwargs={'pk': self.object.id})


class EvolucionDeleteView(generic.DeleteView):
    model = Evolucion
    template_name = 'pokedex/evolucion_confirm_delete.html'
    success_url = reverse_lazy('evolucion_list')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        pokemon = self.object.pokemon
        pokemon_evolucion = self.object.pokemon_evolucion
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, f'Evolución de {pokemon.Nombre} a {pokemon_evolucion.Nombre} ha sido eliminada correctamente.')
        return redirect(success_url)

# Additional HTMX views
@csrf_exempt
def preview_image(request):
    """View for previewing Pokemon images via HTMX"""
    if request.method == 'POST':
        image_url = request.POST.get('image_url', '')
        if (image_url):
            # You could add validation here
            return HttpResponse(f'<img src="{image_url}" class="img-preview" />')
    return HttpResponse('')

@csrf_exempt
def pokemon_favorite(request, no_pokemon):
    """HTMX endpoint for toggling favorite status"""
    pokemon = get_object_or_404(Pokemon, No_Pokemon=no_pokemon)
    pokemon.is_favorite = not pokemon.is_favorite  # Toggle favorite status
    pokemon.save()
    
    return HttpResponse(
        render_to_string('pokedex/favorite_button.html', {'pokemon': pokemon})
    )

# Index page
def index(request):
    """Main dashboard with statistics and links to all models"""
    try:
        context = {
            'pokemon_count': Pokemon.objects.count(),
            'movimiento_count': Movimiento.objects.count(),
            'habilidad_count': Habilidad.objects.count(),
            'tipo_count': Tipo.objects.count(),
            'categoria_count': Categoria.objects.count(),
            'generacion_count': Generacion.objects.count(),
            'grupo_huevo_count': Grupo_Huevo.objects.count(),
            'evolucion_count': Evolucion.objects.count(),
        }
    except Exception as e:
        # Handle the case when tables don't exist yet
        context = {
            'error_message': f'Error accessing database tables: {str(e)}',
            'setup_required': True
        }
    return render(request, 'pokedex/index.html', context)
