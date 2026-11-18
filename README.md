# cybersecurity-tools
Herramientas de pentesting web y reconocimiento creadas desde cero en Android/Termux.

## Herramientas incluidas

- `xss_scanner.py`: Escáner de XSS reflejado con múltiples payloads.
- `file_scanner.py`: Buscador de archivos sensibles expuestos (.env, .git, backups).
- `recon_tool.py`: Menú interactivo de reconocimiento (puertos, cabeceras, fuzzing).
- `proxy.py`: Proxy MitM básico para interceptar y modificar peticiones HTTP.
- `blind_sqli.py`: Exploit de Blind SQLi basado en respuestas condicionales.
- `cracker.py`: Cracker de hashes MD5 por diccionario.
- `fuerza_bruta.py`: Fuerza bruta de hashes MD5 por combinación de caracteres.

## Requisitos

- Python 3
- Librerías: `requests`, `beautifulsoup4`

## Uso

Cada script incluye instrucciones en su interior. Ejecutar con `python nombre_script.py`.

## Aviso legal

Estas herramientas son para fines educativos y de pruebas autorizadas. No las uses en sistemas sin permiso.