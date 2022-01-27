# Proyecto N#2 - Programación con Python

Utilizando la **base de datos de demostración que tiene SQLite**, la cual contiene datos de una aplicación de un sitio de música ficticio se desea hacer una prueba de concepto para un sitio real. El dueño de la tienda real quiere construir una aplicación para lo cual contrata un equipo de desarrollo del cual usted forma parte. Su función en el equipo es la del desarrollo del **backend**.

En una primera fase se requiere que el API exponga algunos endpoints con la finalidad de ir haciendo la prueba de concepto. Es así que el API va a ser bastante sencillo y **no tendrá funcionalidad de seguridad**, en otras palabras no requiere que tenga funciones de chequeo de usuario y password, ni emisión de `jwt` o verificación usando `Oauth2`.

## Instrucciones

- El proyecto debe ser desarrollado en **Python**, usando **FastAPI** para generar el API solicitado

- Los endpoints que se requieren son los siguientes:

  1. Proporcione una lista de artistas

  2. Proporcione una lista de los álbunes de un artista, seleccionándolo con el `id` del artista

  3. Proporcione una lista de las canciones de un albúm, seleccionándolo con el `id` del albúm

  4. Proporcione una lista de canciones de un artista, seleccionándolo con el `id` del artista

  5. Proporcione el detalle completo (_es decir, todos los campos de la tabla_) de una canción, incluyendo el nombre del género musical y el nombre del tipo de media donde está localizado

- Los nombres de los endpoint deben ser los siguientes:

  1. `music-store/api/v1/singers/`: lista total de artistas

  2. `music-store/api/v1/singers/{id}/`: lista de álbumes de un artista

  3. `music-store/api/v1/albums/{id}/`: lista de canciones del álbum de un artista

  4. `music-store/api/v1/singer/{id}/`: lista total de canciones de un artista

  5. `music-store/api/v1/song/{id}/`: detalle de una canción por su id

- La respiesta debe estar en formato JSON

- La estructura de carpetas debe ser la misma que se ha usado en los ejemplos de clase

- El proyecto debe correr en `localhost:8000` y mostrar la documentación con el swagger incorporado de FastApi
