# Automatizacion-de-Envio-de-Correos-desde-Excel-con-Python

## Descripción General
Este script automatiza el proceso de envío masivo de correos electrónicos desarrollado en Python, que se integra directamente con archivos Excel (CSV). La herramienta permite leer datos desde un archivo CSV (exportado desde Excel), personalizar plantillas HTML con la información específica de cada destinatario segun el tipo de correos que se maneje (Recordatorios, avisos,etc), adjuntar documentos digitales (facturas, reportes, contratos, etc.) y enviar los correos de forma automatizada, registrando detalladamente cada acción en un archivo para su auditoría.
El sistema realiza cuatro tareas principales:
1. Leer y procesar datos desde archivos Excel (CSV)
2. Seleccionar y personalizar plantillas HTML según el tipo de correo
3. Adjuntar documentos específicos para cada destinatario
4. Enviar correos electrónicos y registrar cada acción en logs de auditoría

## Problemática que Resuelve
Las empresas manejan diariamente grandes volúmenes de información en archivos Excel: listados de clientes, reportes de ventas, órdenes de compra, facturación, nóminas de empleados, tickets de soporte, entre muchos otros. Esta información, almacenada en formato Excel, requiere frecuentemente ser comunicada por correo electrónico a diferentes destinatarios de manera personalizada.

El proceso manual tradicional presenta las siguientes limitaciones:
- Procesos manuales ineficientes: Un colaborador debe abrir el archivo Excel, acceder al correo electrónico, redactar o copiar una plantilla, buscar manualmente los datos de cada destinatario, localizar el archivo adjunto correspondiente en las carpetas del sistema, verificar la información y finalmente enviar. Este ciclo se repite tantas veces como destinatarios existan.
- Pérdida de tiempo operativo: Para un lote de 100 correos, este proceso manual puede consumir entre 5 y 8 horas de trabajo continuo, representando un costo operativo significativo y restando tiempo a funciones de mayor valor agregado.
- Alta propensión a errores humanos: La naturaleza repetitiva de la tarea aumenta la probabilidad de equivocaciones como enviar información a destinatarios incorrectos, adjuntar archivos que no corresponden al cliente, omitir destinatarios o duplicar envíos, generando reclamos y afectando la imagen corporativa.
- Falta de trazabilidad: No existe un registro automático y confiable de qué correos fueron enviados, a quién, cuándo y con qué resultado, lo que dificulta auditorías internas, la resolución de reclamos y el análisis de gestión.
- Escalabilidad limitada: El modelo manual no permite aumentar el volumen de comunicaciones sin incrementar proporcionalmente el personal o las horas dedicadas a esta tarea, restringiendo el crecimiento operativo.

![](iconos_repo/DiagramaComponentes.png)
![](iconos_repo/Automatizacion.png)
