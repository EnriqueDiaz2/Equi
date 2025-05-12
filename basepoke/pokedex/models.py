from django.db import models

# Create your models here.
class Pokemon(models.Model):
    No_Pokemon = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100, unique=True)
    Ruta_Imagen = models.CharField(max_length=255, blank=True, null=True)
    Descripcion = models.TextField(blank=True, null=True)
    Altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f"{self.No_Pokemon} - {self.Nombre}"
    
    def get_tipos(self):
        return self.tipos.all()
        
    class Meta:
        verbose_name = "Pokémon"
        verbose_name_plural = "Pokémon"

class Movimiento(models.Model):
    Nombre_Movimiento = models.CharField(max_length=100, unique=True)
    Precision = models.IntegerField()
    Potencia = models.IntegerField()
    Categoria = models.CharField(max_length=50, choices=[
        ('Físico', 'Físico'),
        ('Especial', 'Especial'),
        ('Estado', 'Estado'),
    ])
    Puntos_Uso = models.IntegerField()
    
    def __str__(self):
        return f"{self.Nombre_Movimiento} ({self.Categoria})"
        
    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"

class Habilidad(models.Model):
    Nombre_Habilidad = models.CharField(max_length=100, unique=True)
    Descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.Nombre_Habilidad
        
    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

class Tipo(models.Model):
    Nombre_Tipo = models.CharField(max_length=50, unique=True)
    Color = models.CharField(max_length=20, blank=True, null=True)  # Para estilos CSS
    
    def __str__(self):
        return self.Nombre_Tipo
        
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

class Categoria(models.Model):
    Nombre_Categoria = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.Nombre_Categoria
        
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Generacion(models.Model):
    Juegos = models.CharField(max_length=100, unique=True)
    Numero = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"Generación {self.Numero}: {self.Juegos}" if self.Numero else self.Juegos
        
    class Meta:
        verbose_name = "Generación"
        verbose_name_plural = "Generaciones"
        ordering = ['Numero']

class Grupo_Huevo(models.Model):
    nombre_huevo = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre_huevo
        
    class Meta:
        verbose_name = "Grupo Huevo"
        verbose_name_plural = "Grupos Huevo"

# Creating relationship models for many-to-many relationships
class PokemonTipo(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='tipos')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='pokemon')
    
    def __str__(self):
        return f"{self.pokemon.Nombre} - {self.tipo.Nombre_Tipo}"
    
    class Meta:
        verbose_name = "Tipo de Pokémon"
        verbose_name_plural = "Tipos de Pokémon"
        unique_together = ['pokemon', 'tipo']

class PokemonHabilidad(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='habilidades')
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE, related_name='pokemon')
    es_oculta = models.BooleanField(default=False)
    
    def __str__(self):
        tipo = "oculta" if self.es_oculta else "normal"
        return f"{self.pokemon.Nombre} - {self.habilidad.Nombre_Habilidad} ({tipo})"
    
    class Meta:
        verbose_name = "Habilidad de Pokémon"
        verbose_name_plural = "Habilidades de Pokémon"
        unique_together = ['pokemon', 'habilidad']

class PokemonMovimiento(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='movimientos')
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE, related_name='pokemon')
    nivel_aprendizaje = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        nivel = f"Nivel {self.nivel_aprendizaje}" if self.nivel_aprendizaje else "MT/MO/Tutor"
        return f"{self.pokemon.Nombre} - {self.movimiento.Nombre_Movimiento} ({nivel})"
    
    class Meta:
        verbose_name = "Movimiento de Pokémon"
        verbose_name_plural = "Movimientos de Pokémon"
        unique_together = ['pokemon', 'movimiento']

class PokemonCategoria(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='categorias')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='pokemon')
    
    def __str__(self):
        return f"{self.pokemon.Nombre} - {self.categoria.Nombre_Categoria}"
    
    class Meta:
        verbose_name = "Categoría de Pokémon"
        verbose_name_plural = "Categorías de Pokémon"
        unique_together = ['pokemon', 'categoria']

class PokemonGeneracion(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='generaciones')
    generacion = models.ForeignKey(Generacion, on_delete=models.CASCADE, related_name='pokemon')
    
    def __str__(self):
        return f"{self.pokemon.Nombre} - {self.generacion.Juegos}"
    
    class Meta:
        verbose_name = "Generación de Pokémon"
        verbose_name_plural = "Generaciones de Pokémon"
        unique_together = ['pokemon', 'generacion']

class PokemonGrupoHuevo(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='grupos_huevo')
    grupo_huevo = models.ForeignKey(Grupo_Huevo, on_delete=models.CASCADE, related_name='pokemon')
    
    def __str__(self):
        return f"{self.pokemon.Nombre} - {self.grupo_huevo.nombre_huevo}"
    
    class Meta:
        verbose_name = "Grupo Huevo de Pokémon"
        verbose_name_plural = "Grupos Huevo de Pokémon"
        unique_together = ['pokemon', 'grupo_huevo']