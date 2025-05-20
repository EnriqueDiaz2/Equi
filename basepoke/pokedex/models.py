from django.db import models

# Create your models here.
class Pokemon(models.Model):
    No_Pokemon = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100, unique=True)
    Ruta_Imagen = models.CharField(max_length=255, blank=True, null=True)
    Descripcion = models.TextField(blank=True, null=True)
    Altura = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    Peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    naturaleza = models.ForeignKey('Naturaleza', on_delete=models.SET_NULL, related_name='pokemon', null=True, blank=True)
    
    def __str__(self):
        return f"{self.No_Pokemon} - {self.Nombre}"
    
    def get_tipos(self):
        return self.tipos.all()
    
    def calculate_type_effectiveness(self):
        """
        Calculate the effectiveness of all types against this Pokémon based on its type(s).
        Returns a dictionary with effectiveness values: 0, 0.25, 0.5, 1, 2, or 4
        """
        # Diccionario de efectividades de tipo
        # La clave es el tipo atacante, el valor es una lista de tipos contra los
        # que es superefectivo (x2)
        type_chart = {
            'Normal': [],
            'Fuego': ['Planta', 'Hielo', 'Bicho', 'Acero'],
            'Agua': ['Fuego', 'Tierra', 'Roca'],
            'Eléctrico': ['Agua', 'Volador'],
            'Planta': ['Agua', 'Tierra', 'Roca'],
            'Hielo': ['Planta', 'Tierra', 'Volador', 'Dragón'],
            'Lucha': ['Normal', 'Hielo', 'Roca', 'Siniestro', 'Acero'],
            'Veneno': ['Planta', 'Hada'],
            'Tierra': ['Fuego', 'Eléctrico', 'Veneno', 'Roca', 'Acero'],
            'Volador': ['Planta', 'Lucha', 'Bicho'],
            'Psíquico': ['Lucha', 'Veneno'],
            'Bicho': ['Planta', 'Psíquico', 'Siniestro'],
            'Roca': ['Fuego', 'Hielo', 'Volador', 'Bicho'],
            'Fantasma': ['Psíquico', 'Fantasma'],
            'Dragón': ['Dragón'],
            'Siniestro': ['Psíquico', 'Fantasma'],
            'Acero': ['Hielo', 'Roca', 'Hada'],
            'Hada': ['Lucha', 'Dragón', 'Siniestro']
        }
        
        # Inmunidades: tipo atacante como clave, tipos inmunes como valores
        immunities = {
            'Normal': ['Fantasma'],
            'Eléctrico': ['Tierra'],
            'Lucha': ['Fantasma'],
            'Veneno': ['Acero'],
            'Tierra': ['Volador'],
            'Psíquico': ['Siniestro'],
            'Fantasma': ['Normal'],
            'Dragón': ['Hada']
        }
        
        # Resistencias: tipo atacante como clave, tipos que resisten como valores
        resistances = {
            'Normal': ['Roca', 'Acero'],
            'Fuego': ['Fuego', 'Agua', 'Roca', 'Dragón'],
            'Agua': ['Agua', 'Planta', 'Dragón'],
            'Eléctrico': ['Eléctrico', 'Planta', 'Dragón'],
            'Planta': ['Fuego', 'Planta', 'Veneno', 'Volador', 'Bicho', 'Dragón', 'Acero'],
            'Hielo': ['Fuego', 'Agua', 'Hielo', 'Acero'],
            'Lucha': ['Veneno', 'Volador', 'Psíquico', 'Bicho', 'Hada'],
            'Veneno': ['Veneno', 'Tierra', 'Roca', 'Fantasma'],
            'Tierra': ['Planta', 'Bicho'],
            'Volador': ['Eléctrico', 'Roca', 'Acero'],
            'Psíquico': ['Psíquico', 'Acero'],
            'Bicho': ['Fuego', 'Lucha', 'Veneno', 'Volador', 'Fantasma', 'Acero', 'Hada'],
            'Roca': ['Lucha', 'Tierra', 'Acero'],
            'Fantasma': ['Siniestro'],
            'Dragón': ['Acero'],
            'Siniestro': ['Lucha', 'Siniestro', 'Hada'],
            'Acero': ['Fuego', 'Agua', 'Eléctrico', 'Acero'],
            'Hada': ['Fuego', 'Veneno', 'Acero']
        }
        
        # Obtener los tipos del Pokémon
        pokemon_types = [pt.tipo.Nombre_Tipo for pt in self.get_tipos()]
        
        # Inicializar el diccionario de efectividades con valor 1 (daño normal)
        effectiveness = {tipo: 1.0 for tipo in type_chart.keys()}
        
        # Calcular la efectividad para cada tipo
        for attacking_type, super_effective_against in type_chart.items():
            # Revisar si alguno de los tipos del Pokémon es inmune al tipo atacante
            if attacking_type in immunities and any(pt in immunities[attacking_type] for pt in pokemon_types):
                effectiveness[attacking_type] = 0
                continue
                
            # Calcular multiplicador de daño basado en resistencias y debilidades
            multiplier = 1.0
            for pokemon_type in pokemon_types:
                # Super efectivo (x2)
                if pokemon_type in super_effective_against:
                    multiplier *= 2
                # Resistencia (x0.5)
                if attacking_type in resistances and pokemon_type in resistances[attacking_type]:
                    multiplier *= 0.5
                    
            effectiveness[attacking_type] = multiplier
            
        return effectiveness
        
    class Meta:
        verbose_name = "Pokémon"
        verbose_name_plural = "Pokémon"

class Evolucion(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='evoluciones')
    pokemon_evolucion = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='evolucion_de')
    metodo_evolucion = models.CharField(max_length=100)
    nivel_evolucion = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.pokemon.Nombre} evoluciona a {self.pokemon_evolucion.Nombre} ({self.metodo_evolucion})"
    
    class Meta:
        verbose_name = "Evolución"
        verbose_name_plural = "Evoluciones"
        
class Puntos_Base(models.Model):
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE, related_name='puntos_base')
    HP = models.IntegerField()
    Ataque = models.IntegerField()
    Defensa = models.IntegerField()
    Ataque_Especial = models.IntegerField()
    Defensa_Especial = models.IntegerField()
    Velocidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.pokemon.Nombre} - Puntos Base"
        
    def get_stats_with_nature(self):
        """
        Calculate stats considering nature effects
        Returns a dictionary with the modified stats
        """
        stats = {
            'HP': self.HP,
            'Ataque': self.Ataque,
            'Defensa': self.Defensa,
            'Ataque_Especial': self.Ataque_Especial,
            'Defensa_Especial': self.Defensa_Especial,
            'Velocidad': self.Velocidad,
        }
        
        # Apply nature effects if the Pokemon has a nature
        if self.pokemon.naturaleza:
            # Stat to increase (10% boost)
            if self.pokemon.naturaleza.aumenta != 'Ninguna':
                stats[self.pokemon.naturaleza.aumenta] = int(stats[self.pokemon.naturaleza.aumenta] * 1.1)
                
            # Stat to decrease (10% reduction)
            if self.pokemon.naturaleza.disminuye != 'Ninguna':
                stats[self.pokemon.naturaleza.disminuye] = int(stats[self.pokemon.naturaleza.disminuye] * 0.9)
                
        return stats
    
    def get_stat_percentages(self):
        """
        Calculate the percentage for each stat for displaying in stat bars
        Returns a dictionary with percentages
        """
        # Average maximum stat values for normalization
        max_hp = 255
        max_other = 180
        
        stats = self.get_stats_with_nature()
        
        return {
            'HP': min(100, int(stats['HP'] / max_hp * 100)),
            'Ataque': min(100, int(stats['Ataque'] / max_other * 100)),
            'Defensa': min(100, int(stats['Defensa'] / max_other * 100)),
            'Ataque_Especial': min(100, int(stats['Ataque_Especial'] / max_other * 100)),
            'Defensa_Especial': min(100, int(stats['Defensa_Especial'] / max_other * 100)),
            'Velocidad': min(100, int(stats['Velocidad'] / max_other * 100)),
        }
        
    class Meta:
        verbose_name = "Puntos Base"
        verbose_name_plural = "Puntos Base"
class Movimiento(models.Model):
    Nombre_Movimiento = models.CharField(max_length=100, unique=True)
    Precision = models.IntegerField()
    Potencia = models.IntegerField()
    Categoria = models.CharField(max_length=50, choices=[
        ('Físico', 'Físico'),
        ('Especial', 'Especial'),
        ('Estado', 'Estado'),
    ])
    Descripcion = models.TextField(blank=True, null=True)
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

class Naturaleza(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    aumenta = models.CharField(max_length=20, choices=[
        ('Ataque', 'Ataque'),
        ('Defensa', 'Defensa'),
        ('Ataque_Especial', 'Ataque Especial'),
        ('Defensa_Especial', 'Defensa Especial'),
        ('Velocidad', 'Velocidad'),
        ('Ninguna', 'Ninguna'),
    ], default='Ninguna')
    disminuye = models.CharField(max_length=20, choices=[
        ('Ataque', 'Ataque'),
        ('Defensa', 'Defensa'),
        ('Ataque_Especial', 'Ataque Especial'),
        ('Defensa_Especial', 'Defensa Especial'),
        ('Velocidad', 'Velocidad'),
        ('Ninguna', 'Ninguna'),
    ], default='Ninguna')
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        if self.aumenta == 'Ninguna' and self.disminuye == 'Ninguna':
            return f"{self.nombre} (Neutral)"
        return f"{self.nombre} (+{self.aumenta.replace('_', ' ')}, -{self.disminuye.replace('_', ' ')})"
    
    class Meta:
        verbose_name = "Naturaleza"
        verbose_name_plural = "Naturalezas"

class Debilidad(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='debilidades')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='debilidades')

    def __str__(self):
        return f"{self.pokemon.Nombre} - {self.tipo.Nombre_Tipo}"

    class Meta:
        verbose_name = "Debilidad"
        verbose_name_plural = "Debilidades"

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