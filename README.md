# 2026_ejercitacion_git_grupo3
🌳 Guía de Proyecto: Eco-Tracker Las Varillas
Objetivo: Desarrollar una aplicación de consola en Python para registrar árboles urbanos, trabajando en un entorno colaborativo con Git y GitHub.

👥 Organización del Equipo
El grupo se divide en 4 o 5 integrantes. Cada uno tiene una Tarea Única. Nadie puede trabajar en la rama main (principal) directamente; todo se desarrolla en ramas separadas y se fusiona tras una revisión.

🛠️ Reglas del Flujo de Trabajo (Workflow)
Clonar el repositorio: git clone [URL_DEL_REPO]

Crear una rama propia: git checkout -b feature-tarea-X (reemplaza X por tu número de tarea).

Programar: Realiza los cambios en los archivos .py indicados.

Guardar y Subir:

git add .

git commit -m "Finalizada tarea X: [Descripción breve]"

git push origin feature-tarea-X

Revisión por Pares: Tus compañeros deben mirar tu código en GitHub. Si te dan el "visto bueno":

Regresa a la rama principal: git checkout main

Trae los cambios de tus compañeros: git pull origin main

Fusiona tu trabajo: git merge feature-tarea-X

Resolver conflictos: Si Git avisa de un conflicto, ábrelo con el editor, decide qué código queda, guarda, haz git add y git commit.

Sube el resultado final: git push origin main

📋 Asignación de Tareas
Estructura de archivos:
data_manager.py: Lógica de datos y funciones.

main.py: Menú y ejecución.

👤 Alumno 1: El Arquitecto de Datos
Archivo: data_manager.py

Misión: Crear una lista global llamada inventario. Crear la función inicializar_datos() que cargue 3 diccionarios de ejemplo. Cada diccionario (árbol) debe tener las llaves: "especie", "estado" (ej: "Saludable") y "ubicacion".

Meta: Ser el primero en subir para que los demás tengan una base.

👤 Alumno 2: El Registrador
Archivo: data_manager.py

Misión: Crear la función agregar_arbol(especie, estado, ubicacion). Debe recibir los datos, crear un nuevo diccionario y añadirlo a la lista inventario usando .append().

Meta: Asegurarte de que la función retorne un mensaje de confirmación.

👤 Alumno 3: El Diseñador de Interfaz
Archivo: main.py

Misión: Crear el archivo main.py e importar las funciones de data_manager. Diseñar un menú usando un bucle while True que muestre opciones (1. Ver árboles, 2. Agregar, 3. Salir). Por ahora, solo debe funcionar la opción "Salir".

Meta: Establecer la estructura visual del programa.

👤 Alumno 4: El Analista de Datos
Archivo: data_manager.py y main.py

Misión: En data_manager.py, crear la función listar_arboles() que recorra la lista con un for e imprima cada árbol de forma legible. En main.py, conectar esta función a la opción "Ver árboles" del menú.

Meta: Gestionar el primer gran conflicto de código al modificar main.py.

👤 Alumno 5 (Si el grupo es de 5): El Inspector de Salud
Archivo: data_manager.py y main.py

Misión: Crear una función que filtre la lista de inventario y devuelva solo los árboles cuyo estado sea "Enfermo". Agregar una nueva opción al menú en main.py para mostrar este reporte.

Meta: Trabajar sobre código que otros ya han modificado.

🚨 Desafío Extra: El Conflicto de Identidad
Instrucción obligatoria: Todos los integrantes deben escribir su nombre en un comentario en la línea 1 de main.py antes de intentar hacer su primer merge. Esto obligará a cada uno a aprender a resolver conflictos de líneas superpuestas.

¡Muchos éxitos, desarrolladores! Recuerden: comunicarse con el equipo es tan importante como escribir código.
