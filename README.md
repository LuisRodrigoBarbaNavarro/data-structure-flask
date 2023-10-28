# Práctica 3 I Flask Con Diccionarios, Conjuntos, Tuplas 🐈

---

### Información Básica ✨

**Nombre:** Barba Navarro Luis Rodrigo

**Fecha (Creación):** 24/10/23

**Descripción:** Este repositorio aloja un proyecto en Python que utiliza el framework Flask para implementar operaciones de manipulación de diccionarios, tuplas y conjuntos. Estas operaciones permiten agregar, eliminar y combinar elementos de estos tipos de datos de manera eficiente. El proyecto es una herramienta autónoma que se ejecuta localmente y ofrece estas funciones directamente a través de una interfaz web usando elementos HTML y Bootstrap.

---

### Explicación ✨

La implementación realizada en este proyecto se centra en la presentación de estructuras de datos tras la ejecución de diversas operaciones, exhibiéndolas en una sección HTML con el uso de Bootstrap. Este enfoque permite visualizar de manera organizada los elementos que han sido modificados por las operaciones efectuadas. En el proceso inicial, se estableció una variable para servir como plantilla tanto al inicio como al final de los documentos HTML, utilizada tanto en la representación de tabla como en forma de lista. Cuando se proporciona un parámetro correspondiente a cualquiera de las tres estructuras de datos, se procesa la operación correspondiente y luego se itera para mostrar cada elemento asociado en la tabla o lista resultante. Esta parte del código se concatena entre las plantillas HTML previamente definidas, creando así una presentación coherente y organizada de los resultados.

En el contexto de las funciones implementadas en este proyecto, su funcionalidad básica se asemeja a la de la práctica 1 realizada previamente. Sin embargo, se ha introducido una novedad al definir rutas que permiten el acceso a estas operaciones a través de URLs específicas desde un navegador web. La estructura de estas URL se adapta según el tipo de operación requerida:

- Para diccionarios se utiliza `.../dictionary/<Diccionario>/<Operación>/<Argumentos>`.
- Para colecciones se utiliza `.../set/<Colección>/<Operación>/<Argumentos>`.
- Para tuplas se utiliza `.../tuple/<Tupla>/<Operación>/<Argumentos>`.

Las funciones internas ejecutan las operaciones respectivas y generan fragmentos de código HTML destinados a mostrar los resultados en el documento, facilitando la visualización de los elementos en la interfaz web.

---

### Implementación (Ejemplos - Diccionario) ✨

**Añadir - Diccionario:**

Para añadir un elemento a un diccionario proporcionado, se puede realizar de la siguiente manera:

1. Acceda a la URL correspondiente, como por ejemplo: `http://127.0.0.1/dictionary/{"Animal 1": "León", "Animal 2": "Tigre", "Animal 3": "Jirafa", "Animal 4": "Elefante"}/add/Animal 5/Coyote`.

2. Al ejecutar esta operación, se generará una vista que mostrará los resultados de la acción.

<p align="center">
  <img src="https://i.imgur.com/lkC07fr.png" alt="Descripción de la imagen">
</p>

**Eliminar - Diccionario:**

Para eliminar un elemento a un diccionario proporcionado, se puede realizar de la siguiente manera:

1. Acceda a la URL correspondiente, como por ejemplo: `http://127.0.0.1/dictionary/{"Animal 1": "León", "Animal 2": "Tigre", "Animal 3": "Jirafa", "Animal 4": "Elefante"}/delete/Animal 2`.

2. Al ejecutar esta operación, se generará una vista que mostrará los resultados de la acción.

<p align="center">
  <img src="https://i.imgur.com/XzyW7i1.png" alt="Descripción de la imagen">
</p>

**Modificar - Diccionario:**

Para modificar un elemento a un diccionario proporcionado, se puede realizar de la siguiente manera:

1. Acceda a la URL correspondiente, como por ejemplo: `http://127.0.0.1/dictionary/{"Animal 1": "León", "Animal 2": "Tigre", "Animal 3": "Jirafa", "Animal 4": "Elefante"}/modify/Animal 2/Lombriz`.

2. Al ejecutar esta operación, se generará una vista que mostrará los resultados de la acción.

<p align="center">
  <img src="https://i.imgur.com/4cMezat.png" alt="Descripción de la imagen">
</p>
