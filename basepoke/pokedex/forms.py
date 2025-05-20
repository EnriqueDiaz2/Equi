from django import forms
from .models import (
    Pokemon, Movimiento, Habilidad, Tipo, Categoria, 
    Generacion, Grupo_Huevo, PokemonTipo, PokemonHabilidad, 
    PokemonMovimiento, PokemonCategoria, PokemonGeneracion, 
    PokemonGrupoHuevo, Naturaleza, Puntos_Base, Evolucion
)

# Common CSS classes for form styling
input_class = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-pokemon-red focus:ring focus:ring-pokemon-red focus:ring-opacity-50'
text_area_class = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-pokemon-red focus:ring focus:ring-pokemon-red focus:ring-opacity-50'
select_class = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-pokemon-red focus:ring focus:ring-pokemon-red focus:ring-opacity-50'

# Pokemon Form
class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['No_Pokemon', 'Nombre', 'Ruta_Imagen', 'Descripcion', 'Altura', 'Peso', 'naturaleza']
        widgets = {
            'No_Pokemon': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Número de Pokémon'}),
            'Nombre': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Nombre del Pokémon'}),
            'Ruta_Imagen': forms.URLInput(attrs={'class': input_class, 'placeholder': 'URL de la imagen'}),
            'Descripcion': forms.Textarea(attrs={'class': text_area_class, 'placeholder': 'Descripción', 'rows': 4}),
            'Altura': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Altura en metros', 'step': '0.01'}),
            'Peso': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Peso en kg', 'step': '0.01'}),
            'naturaleza': forms.Select(attrs={'class': select_class}),
        }

# Movimiento Form
class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ['Nombre_Movimiento', 'Precision', 'Potencia', 'Categoria', 'Puntos_Uso'
        ]
        widgets = {
            'Nombre_Movimiento': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Nombre del movimiento'}),
            'Precision': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Precisión (0-100)'}),
            'Potencia': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Potencia'}),
            'Categoria': forms.Select(attrs={'class': select_class}),
            'Puntos_Uso': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Puntos de uso (PP)'}),
        }

# Habilidad Form
class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['Nombre_Habilidad', 'Descripcion']
        widgets = {
            'Nombre_Habilidad': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Nombre de la habilidad'}),
            'Descripcion': forms.Textarea(attrs={'class': text_area_class, 'placeholder': 'Descripción', 'rows': 3}),
        }

# Tipo Form
class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['Nombre_Tipo', 'Color']
        widgets = {
            'Nombre_Tipo': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Nombre del tipo'}),
            'Color': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Color (hex o nombre)'}),
        }

# Categoria Form
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['Nombre_Categoria']
        widgets = {
            'Nombre_Categoria': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Nombre de la categoría'}),
        }

# Naturaleza Form
class NaturalezaForm(forms.ModelForm):
    class Meta:
        model = Naturaleza
        fields = ['nombre', 'aumenta', 'disminuye', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Nombre de la naturaleza'}),
            'aumenta': forms.Select(attrs={'class': select_class}),
            'disminuye': forms.Select(attrs={'class': select_class}),
            'descripcion': forms.Textarea(attrs={'class': text_area_class, 'placeholder': 'Descripción', 'rows': 3}),
        }

# Generacion Form
class GeneracionForm(forms.ModelForm):
    class Meta:
        model = Generacion
        fields = ['Juegos', 'Numero']
        widgets = {
            'Juegos': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Juegos de la generación'}),
            'Numero': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Número de generación'}),
        }

# Grupo_Huevo Form
class GrupoHuevoForm(forms.ModelForm):
    class Meta:
        model = Grupo_Huevo
        fields = ['nombre_huevo']
        widgets = {
            'nombre_huevo': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Nombre del grupo huevo'}),
        }

# Relationship Forms
class PokemonTipoForm(forms.ModelForm):
    class Meta:
        model = PokemonTipo
        fields = ['pokemon', 'tipo']
        widgets = {
            'pokemon': forms.Select(attrs={'class': select_class}),
            'tipo': forms.Select(attrs={'class': select_class}),
        }

class PokemonHabilidadForm(forms.ModelForm):
    class Meta:
        model = PokemonHabilidad
        fields = ['pokemon', 'habilidad', 'es_oculta']
        widgets = {
            'pokemon': forms.Select(attrs={'class': select_class}),
            'habilidad': forms.Select(attrs={'class': select_class}),
            'es_oculta': forms.CheckboxInput(attrs={'class': 'rounded border-gray-300 text-pokemon-red shadow-sm focus:border-pokemon-red focus:ring focus:ring-pokemon-red focus:ring-opacity-50'}),
        }

class PokemonMovimientoForm(forms.ModelForm):
    class Meta:
        model = PokemonMovimiento
        fields = ['pokemon', 'movimiento', 'nivel_aprendizaje']
        widgets = {
            'pokemon': forms.Select(attrs={'class': select_class}),
            'movimiento': forms.Select(attrs={'class': select_class}),
            'nivel_aprendizaje': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Nivel de aprendizaje'}),
        }

class PokemonCategoriaForm(forms.ModelForm):
    class Meta:
        model = PokemonCategoria
        fields = ['pokemon', 'categoria']
        widgets = {
            'pokemon': forms.Select(attrs={'class': select_class}),
            'categoria': forms.Select(attrs={'class': select_class}),
        }

class PokemonGeneracionForm(forms.ModelForm):
    class Meta:
        model = PokemonGeneracion
        fields = ['pokemon', 'generacion']
        widgets = {
            'pokemon': forms.Select(attrs={'class': select_class}),
            'generacion': forms.Select(attrs={'class': select_class}),
        }

class PokemonGrupoHuevoForm(forms.ModelForm):
    class Meta:
        model = PokemonGrupoHuevo
        fields = ['pokemon', 'grupo_huevo']
        widgets = {
            'pokemon': forms.Select(attrs={'class': select_class}),
            'grupo_huevo': forms.Select(attrs={'class': select_class}),
        }

# PuntosBase Form
class PuntosBaseForm(forms.ModelForm):
    class Meta:
        model = Puntos_Base
        fields = ['pokemon', 'HP', 'Ataque', 'Defensa', 'Ataque_Especial', 'Defensa_Especial', 'Velocidad']
        widgets = {
            'pokemon': forms.Select(attrs={'class': select_class}),
            'HP': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'HP base'}),
            'Ataque': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Ataque base'}),
            'Defensa': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Defensa base'}),
            'Ataque_Especial': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Ataque Especial base'}),
            'Defensa_Especial': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Defensa Especial base'}),
            'Velocidad': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Velocidad base'}),
        }

# Evolucion Form
class EvolucionForm(forms.ModelForm):
    class Meta:
        model = Evolucion
        fields = ['pokemon', 'pokemon_evolucion', 'metodo_evolucion', 'nivel_evolucion']
        widgets = {
            'pokemon': forms.Select(attrs={'class': select_class}),
            'pokemon_evolucion': forms.Select(attrs={'class': select_class}),
            'metodo_evolucion': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Método de evolución'}),
            'nivel_evolucion': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Nivel de evolución (opcional)'}),
        }