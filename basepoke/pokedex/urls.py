from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('api/pokemon/', views.pokemon_crud, name='pokemon_crud'),
    path('api/movimientos/', views.movimiento_crud, name='movimiento_crud'),
    path('api/habilidades/', views.habilidad_crud, name='habilidad_crud'),
    path('api/tipos/', views.tipo_crud, name='tipo_crud'),
    path('api/categorias/', views.categoria_crud, name='categoria_crud'),
    path('api/generaciones/', views.generacion_crud, name='generacion_crud'),
    path('api/grupos-huevo/', views.grupo_huevo_crud, name='grupo_huevo_crud'),
    path('api/pokemon-tipos/', views.pokemon_tipo_crud, name='pokemon_tipo_crud'),
    path('api/pokemon-habilidades/', views.pokemon_habilidad_crud, name='pokemon_habilidad_crud'),
    
    # Home page
    path('', views.index, name='index'),
    
    # Pokemon URLs
    path('pokemon/', views.PokemonListView.as_view(), name='pokemon_list'),
    path('pokemon/<int:no_pokemon>/', views.PokemonDetailView.as_view(), name='pokemon_detail'),
    path('pokemon/new/', views.PokemonCreateView.as_view(), name='pokemon_create'),
    path('pokemon/<int:no_pokemon>/edit/', views.PokemonUpdateView.as_view(), name='pokemon_update'),
    path('pokemon/<int:no_pokemon>/delete/', views.PokemonDeleteView.as_view(), name='pokemon_delete'),
    
    # Movimiento URLs
    path('movimientos/', views.MovimientoListView.as_view(), name='movimiento_list'),
    path('movimientos/<int:pk>/', views.MovimientoDetailView.as_view(), name='movimiento_detail'),
    path('movimientos/new/', views.MovimientoCreateView.as_view(), name='movimiento_create'),
    path('movimientos/<int:pk>/edit/', views.MovimientoUpdateView.as_view(), name='movimiento_update'),
    path('movimientos/<int:pk>/delete/', views.MovimientoDeleteView.as_view(), name='movimiento_delete'),
    
    # Habilidad URLs
    path('habilidades/', views.HabilidadListView.as_view(), name='habilidad_list'),
    path('habilidades/<int:pk>/', views.HabilidadDetailView.as_view(), name='habilidad_detail'),
    path('habilidades/new/', views.HabilidadCreateView.as_view(), name='habilidad_create'),
    path('habilidades/<int:pk>/edit/', views.HabilidadUpdateView.as_view(), name='habilidad_update'),
    path('habilidades/<int:pk>/delete/', views.HabilidadDeleteView.as_view(), name='habilidad_delete'),
    
    # Tipo URLs
    path('tipos/', views.TipoListView.as_view(), name='tipo_list'),
    path('tipos/<int:pk>/', views.TipoDetailView.as_view(), name='tipo_detail'),
    path('tipos/new/', views.TipoCreateView.as_view(), name='tipo_create'),
    path('tipos/<int:pk>/edit/', views.TipoUpdateView.as_view(), name='tipo_update'),
    path('tipos/<int:pk>/delete/', views.TipoDeleteView.as_view(), name='tipo_delete'),
    
    # Categoria URLs
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/new/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/edit/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
    
    # Generacion URLs
    path('generaciones/', views.GeneracionListView.as_view(), name='generacion_list'),
    path('generaciones/<int:pk>/', views.GeneracionDetailView.as_view(), name='generacion_detail'),
    path('generaciones/new/', views.GeneracionCreateView.as_view(), name='generacion_create'),
    path('generaciones/<int:pk>/edit/', views.GeneracionUpdateView.as_view(), name='generacion_update'),
    path('generaciones/<int:pk>/delete/', views.GeneracionDeleteView.as_view(), name='generacion_delete'),
    
    # Grupo Huevo URLs
    path('grupos-huevo/', views.GrupoHuevoListView.as_view(), name='grupo_huevo_list'),
    path('grupos-huevo/<int:pk>/', views.GrupoHuevoDetailView.as_view(), name='grupo_huevo_detail'),
    path('grupos-huevo/new/', views.GrupoHuevoCreateView.as_view(), name='grupo_huevo_create'),
    path('grupos-huevo/<int:pk>/edit/', views.GrupoHuevoUpdateView.as_view(), name='grupo_huevo_update'),
    path('grupos-huevo/<int:pk>/delete/', views.GrupoHuevoDeleteView.as_view(), name='grupo_huevo_delete'),
    
    # Relationship model URLs
    # PokemonTipo URLs
    path('pokemon-tipos/', views.PokemonTipoListView.as_view(), name='pokemon_tipo_list'),
    path('pokemon-tipos/new/', views.PokemonTipoCreateView.as_view(), name='pokemon_tipo_create'),
    path('pokemon-tipos/<int:pk>/edit/', views.PokemonTipoUpdateView.as_view(), name='pokemon_tipo_update'),
    path('pokemon-tipos/<int:pk>/delete/', views.PokemonTipoDeleteView.as_view(), name='pokemon_tipo_delete'),
    
    # PokemonHabilidad URLs
    path('pokemon-habilidades/', views.PokemonHabilidadListView.as_view(), name='pokemon_habilidad_list'),
    path('pokemon-habilidades/new/', views.PokemonHabilidadCreateView.as_view(), name='pokemon_habilidad_create'),
    path('pokemon-habilidades/<int:pk>/edit/', views.PokemonHabilidadUpdateView.as_view(), name='pokemon_habilidad_update'),
    path('pokemon-habilidades/<int:pk>/delete/', views.PokemonHabilidadDeleteView.as_view(), name='pokemon_habilidad_delete'),
    
    # PokemonMovimiento URLs
    path('pokemon-movimientos/', views.PokemonMovimientoListView.as_view(), name='pokemon_movimiento_list'),
    path('pokemon-movimientos/new/', views.PokemonMovimientoCreateView.as_view(), name='pokemon_movimiento_create'),
    path('pokemon-movimientos/<int:pk>/edit/', views.PokemonMovimientoUpdateView.as_view(), name='pokemon_movimiento_update'),
    path('pokemon-movimientos/<int:pk>/delete/', views.PokemonMovimientoDeleteView.as_view(), name='pokemon_movimiento_delete'),
    
    # PokemonCategoria URLs
    path('pokemon-categorias/', views.PokemonCategoriaListView.as_view(), name='pokemon_categoria_list'),
    path('pokemon-categorias/new/', views.PokemonCategoriaCreateView.as_view(), name='pokemon_categoria_create'),
    path('pokemon-categorias/<int:pk>/edit/', views.PokemonCategoriaUpdateView.as_view(), name='pokemon_categoria_update'),
    path('pokemon-categorias/<int:pk>/delete/', views.PokemonCategoriaDeleteView.as_view(), name='pokemon_categoria_delete'),
    
    # PokemonGeneracion URLs
    path('pokemon-generaciones/', views.PokemonGeneracionListView.as_view(), name='pokemon_generacion_list'),
    path('pokemon-generaciones/new/', views.PokemonGeneracionCreateView.as_view(), name='pokemon_generacion_create'),
    path('pokemon-generaciones/<int:pk>/edit/', views.PokemonGeneracionUpdateView.as_view(), name='pokemon_generacion_update'),
    path('pokemon-generaciones/<int:pk>/delete/', views.PokemonGeneracionDeleteView.as_view(), name='pokemon_generacion_delete'),
    
    # PokemonGrupoHuevo URLs
    path('pokemon-grupos-huevo/', views.PokemonGrupoHuevoListView.as_view(), name='pokemon_grupo_huevo_list'),
    path('pokemon-grupos-huevo/new/', views.PokemonGrupoHuevoCreateView.as_view(), name='pokemon_grupo_huevo_create'),
    path('pokemon-grupos-huevo/<int:pk>/edit/', views.PokemonGrupoHuevoUpdateView.as_view(), name='pokemon_grupo_huevo_update'),
    path('pokemon-grupos-huevo/<int:pk>/delete/', views.PokemonGrupoHuevoDeleteView.as_view(), name='pokemon_grupo_huevo_delete'),
    
    # HTMX endpoints
    path('preview-image/', views.preview_image, name='preview_image'),
    path('pokemon/<int:no_pokemon>/favorite/', views.pokemon_favorite, name='pokemon_favorite'),
]