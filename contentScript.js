// Obtener URL de la página actual
var currentUrl = window.location.href;

// Enviar solicitud GET a la URL de la página actual
fetch(currentUrl)
  .then(response => response.text())
  .then(html => {
      // Crear un objeto DOM con el HTML de la página
      const parser = new DOMParser();
      const dom = parser.parseFromString(html, 'text/html');

      // Obtener los datos de la página utilizando la función get_geekbench_data
      const results = get_geekbench_data(currentUrl);

      // Modificar el HTML de la página para añadir los datos obtenidos
      const singleCorePerformanceSection = dom.querySelector('div[data-test-id="single-core-performance"]');

      // Crear un elemento div para mostrar los datos
      const dataElement = document.createElement('div');
      dataElement.innerHTML = `Single-Core Frequency: ${results.single_core_frequency} GHz`;

      // Añadir el elemento al DOM
      singleCorePerformanceSection.appendChild(dataElement);

      // Actualizar el HTML de la página con los cambios realizados
      document.documentElement.innerHTML = dom.documentElement.innerHTML;
  });
