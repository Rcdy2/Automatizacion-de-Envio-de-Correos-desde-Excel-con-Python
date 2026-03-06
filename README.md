# Automatizacion-de-Envio-de-Correos-desde-Excel-con-Python

## Descripción General
Este proyecto consiste en un script desarrollado en Python que automatiza el proceso de envío masivo de correos electrónicos personalizados a partir de datos contenidos en archivos CSV exportados desde Excel. La herramienta permite leer registros, personalizar plantillas HTML con información específica de cada destinatario, adjuntar documentos (PDF, imágenes, etc.) y enviar los correos de forma automatizada, generando además un registro de auditoría detallado de cada acción.

**Las 4 tareas principales del sistema:**
- Leer y procesar datos desde archivo CSV (exportado de Excel)
- Seleccionar y personalizar la plantilla HTML según el tipo de comunicación
- Adjuntar documentos específicos para cada destinatario
- Enviar correos y registrar cada acción en logs para auditoría

**Capacidad del sistema:**
- Cuentas personales (Gmail, Hotmail): hasta 500 envíos diarios
- Cuentas corporativas: hasta 2000 envíos diarios

# Tipos de correos generados
El sistema utiliza plantillas HTML diseñadas que se personalizan automáticamente con los datos de cada destinatario. Dependiendo de la necesidad de comunicación, se pueden configurar diferentes tipos de mensajes en este caso se aplicaron dos tipos de correos:

- **Correo tipo Aviso Final:** Diseñado para comunicaciones urgentes o de última instancia. Utiliza una paleta de colores en tonos rojos que transmite formalidad y urgencia, incluye advertencias explícitas y destaca visualmente los montos y fechas críticas.
![](iconos_repo/correoAvisoFinal.png)

- **Correo tipo Recordatorio:** Orientado a comunicaciones preventivas o de cortesía. Emplea una paleta de colores institucionales en tonos azules que transmite confianza y profesionalismo, ofreciendo opciones y facilidades antes de llegar a solicitudes más formales.
![](iconos_repo/correoRecordatorio.png)

Ambas plantillas son completamente personalizables, se puede modificar el texto, los colores, la estructura y las variables según los requerimientos de cada empresa o área (las plantillas realizadas son de ejemplos).


## Problemática
En la mayoría de empresas, la información operativa se gestiona en Excel. Ventas tiene un Excel con clientes, RH tiene un Excel con empleados, Logística tiene un Excel con proveedores. Cuando necesitan enviar comunicaciones masivas (cobranzas, boletas, notificaciones, promociones), el proceso es siempre el mismo y es manual:
Una persona del área abre el Excel, filtra el primer registro, copia los datos, abre su correo, redacta un mensaje, busca el archivo adjunto en las carpetas del servidor, lo adjunta, envía, y marca en el Excel que ya realizó el envío. Luego repite para el siguiente registro.

**El problema concreto:**
- Tomar 5-10 minutos por registro significa que para 100 registros se pierde casi un día completo de trabajo
- Los errores son frecuentes: adjuntar archivo equivocado, copiar mal un nombre, omitir destinatarios
- No hay trazabilidad: si en el futuro preguntan por un envío específico, no hay forma de verificarlo directamente
- El proceso depende del personal del área: si se enferma o renuncia, se detiene generando retrasos

## Proceso actual (AS-IS)
El diagrama AS-IS muestra el flujo de trabajo manual que actualmente siguen las empresas para enviar comunicaciones masivas mediante correos. Este proceso, al depender completamente del personal, presenta múltiples puntos de fallo y cuellos de botella que afectan la productividad del equipo.
![](iconos_repo/AsIs.png)

**Problemas identificados:**
- Proceso manual y repetitivo que consume horas de trabajo
- Alto riesgo de error humano en cada paso
- Sin registro centralizado ni trazabilidad
- Difícil de escalar cuando el volumen crece

## Proceso automatizado (TO-BE)
El diagrama TO-BE ilustra cómo el sistema transforma radicalmente el flujo de trabajo, eliminando la intervención manual en tareas repetitivas. La automatización permite que el script se encargue de todo el proceso operativo repetitivo.
![](iconos_repo/ToBe.png)

**Beneficios obtenidos:**
- Registros procesados automaticamente en segundos
- Cero errores de personalización o adjuntos
- Auditoría completa 
- El proceso no depende de una persona específica
- Escalable a cualquier volumen

## Comparacion de mejoras en los procesos
La siguiente imagen integra ambos flujos (AS-IS y TO-BE) en una vista comparativa donde se permite visualizar claramente la transformación del proceso. En el lado izquierdo se observa el flujo manual con todos sus pasos secuenciales y su clara dependencias humanas; en el lado derecho, el flujo automatizado donde el script reemplaza las tareas repetitivas. Esta comparación evidencia la reducción de pasos, la eliminación de cuellos de botella y el impacto directo en la eficiencia operativa.
![](iconos_repo/Automatizacion.png)


## Arquitectura del Sistema 
**1. Arquitectura en Capas**
La arquitectura en capas muestra la organización estructural del sistema, separando claramente las responsabilidades en niveles independientes. Esta separación permite que cada capa pueda modificarse o reemplazarse sin afectar a las demás, facilitando el mantenimiento y la escalabilidad.
![](iconos_repo/Arquitecturadelsistema.png)


**2. Diagrama de Componentes**
Este diagrama de componentes detalla los módulos específicos que conforman el sistema y cómo se relacionan entre sí. Cada componente tiene una función claramente definida, lo que permite entender rápidamente el flujo de datos y la lógica de negocio implementada.
![](iconos_repo/DiagramaComponentes.png)

## **Componentes - Estructura del Proyecto**
| Modulo / Archivo | Responsabilidad |
| :--- | :--- |
| `main.py` | **Orquestador principal**: lee CSV, itera sobre registros y coordina el flujo. |
| `data_processor.py` | Carga el CSV con `pandas`, prepara diccionario de datos por cliente. |
| `email_sender.py` | Construye el mensaje MIME (HTML + adjuntos) y envía vía SMTP. |
| `logger_config.py` | Configura los logs con `logging` para guardarlos en archivo y consola asegurando persistencia y seguridad. |
| `config/empresa.py` | Datos de la empresa (nombre, teléfono, dirección, etc) para personalizar los correos. |
| `config/credentials.py` | Almacena las credenciales SMTP. |
| `datos/` | Contiene el archivo CSV con los datos a exportar(exportado desde Excel). |
| `plantillas/` | Archivos HTML con el diseño para los diferentes tipos de correos, utilizando variables de entrada |
| `adjuntos/` | Carpeta con los PDFs u otros archivos a adjuntar por destinatario. |
| `icon/` | Logo de la empresa para incrustar en el cuerpo del correo. |
| `logs_auditoria/` | Archivos de log con registro detallado de cada envío realizado, fundamentales para auditoria. |


## Diagrama de Secuencia (Interacción entre componentes)
Mediante este diagrama de secuencia representamos la interacción entre los diferentes componentes durante la ejecución del sistema. Muestra el orden en que se llaman los módulos, cómo fluye la información entre ellos y los puntos de decisión en el proceso, permitiendo comprender el comportamiento de la aplicación.
![](iconos_repo/secuencias.png)
