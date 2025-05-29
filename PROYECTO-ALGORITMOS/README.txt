ESTRUCTURAS DE DATOS Y ANALISIS DE ALGORITMOS.

ESTUDIANTES: 

ERICK JOAN LIZARAZO PARDO - CODIGO: 2231875
JUAN FELIPE CASTELLANOS CASTRO - CODIGO: 2231868

RESUMEN DEL PROBLEMA:

El turismo terrestre en Colombia ha ganado protagonismo debido a la riqueza natural, 
cultural y gastronómica del país. Sin embargo, muchos viajeros enfrentan dificultades 
al planificar sus recorridos por carretera, especialmente al calcular distancias, tiempos,
costos de combustible, peajes y condiciones climáticas.
La falta de herramientas personalizadas para estas necesidades limita la experiencia del 
viajero y puede llevar a una mala gestión del tiempo y recursos.

OBJETIVOS DEL PROYECTO: 

Diseñar y desarrollar una herramienta informática que permita a los usuarios planificar 
rutas terrestres dentro de Colombia de forma eficiente. El sistema debe ser capaz de 
calcular distancias, tiempos estimados de viaje, costos aproximados de combustible y peajes, 
e incorporar factores como el clima.

ANALISIS DEL PROBLEMA:
Se identificaron las necesidades de los viajeros al organizar rutas terrestres: eficiencia, 
claridad y facilidad de uso.
Se establecieron los requerimientos funcionales principales del sistema.

DISEÑO DEL PROGRAMA:

Se organizaron los datos en estructuras adecuadas como listas y árboles binarios.
Se definió una interfaz de usuario por consola con menús interactivos y mensajes claros.

IMPLEMENTACION: 

El lenguaje utilizado fue Python.

AVANCES DE LA ENTREGA #1: 

En la primera etapa del proyecto se estableció la finalidad principal y el contexto general: 
desarrollar un asistente en Python para planificar viajes terrestres dentro de Colombia, 
apoyándose en estadísticas reales del turismo nacional.

Se definieron claramente las cinco preguntas claves que el programa debe responder para 
facilitar la planificación de viajes:

1.Determinar la distancia y el tiempo aproximado entre dos ciudades.
2.Identificar la ruta más corta entre dos puntos seleccionados.
3.Calcular el costo aproximado de combustible para el trayecto.
4.Estimar el tiempo adicional de viaje bajo condiciones climáticas adversas (lluvia y pavimento húmedo).
5.Calcular el costo aproximado de peajes en la ruta.

AVANCES DE LA ENTREGA #2: 

En esta segunda etapa del proyecto "Asistente de Viajes por Tierra - Turismo en Colombia" se avanzó 
en la optimización del manejo y organización de la información relacionada con las ciudades visitadas 
durante los viajes.

Para ello, se incorporó la estructura de datos Árbol Binario de Búsqueda (ABB), que permite almacenar 
y gestionar las ciudades de manera eficiente, superando las limitaciones del uso exclusivo de listas 
enlazadas desarrollado en la primera entrega.
Con esta mejora, cada vez que un usuario registra un nuevo viaje, las ciudades de origen y destino 
se insertan en el ABB, respetando el orden alfabético. Esto permite:

1.Inserciones rápidas y organizadas de nuevas ciudades.
2.Búsquedas eficientes para determinar si una ciudad ya ha sido visitada, sin necesidad de recorrer toda una lista.
3.Impresión ordenada de todas las ciudades visitadas, facilitando la visualización alfabética de la información.

AVANCES DE LA ENTREGA #3: 

En esta tercera etapa del proyecto "Asistente de Viajes por Tierra - Turismo en Colombia", se dio un salto 
importante en la complejidad y funcionalidad del sistema, atendiendo la necesidad de modelar las rutas entre 
ciudades de forma más realista y flexible.

Dado el crecimiento del turismo terrestre y la diversidad de conexiones posibles entre ciudades, se implementó 
una estructura de datos grafo dirigido ponderado, donde:

1.Cada nodo representa una ciudad.
2.Cada arista dirigida representa una ruta entre dos ciudades, con atributos como distancia, tiempo, 
costo de combustible, peajes y condiciones climáticas.

Las principales funcionalidades añadidas en esta entrega incluyen:

1.Inserción y eliminación de ciudades en el grafo.
2.Inserción, actualización y eliminación de rutas entre ciudades.
3.Búsqueda de rutas directas entre dos ciudades.
4.Visualización completa de las ciudades y sus rutas asociadas.

Esta mejora permite al asistente ofrecer una planificación de viajes mucho más precisa, adaptada a 
las condiciones reales de las carreteras colombianas y las necesidades de los viajeros, optimizando tiempos, 
costos y seguridad.

