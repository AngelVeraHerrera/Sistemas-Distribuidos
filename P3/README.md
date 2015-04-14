# Seminario nº 3 - Twitter, Python y Flask

En este seminario tenemos que hacer una página web realizada con Python y el framework Flask que se conecte a la API de twitter para realizar una consulta sobre algún término. Mostrando luego ese resultado en un mapa utilizando Google Maps.

Consiste de estos módulos:

  - Módulo de conexión a la API de Twitter.
  - Módulo de obtención de la información.
  - Modulo principal donde se aloja la web.

El funcionamiento final consiste en tener una web con un campo de búsqueda, al escribir y pulsar se envía el parámetro por POST y es recogido por una sección en la página web. Una vez recogido, se genera la búsqueda y se obtienen todas las coordenadas. Con las coordenadas, generamos el mapa y lo pasamos por parámetro a la web, mostrándose el mapa con los marcadores.
