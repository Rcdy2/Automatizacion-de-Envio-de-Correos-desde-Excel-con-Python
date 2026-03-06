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

![](iconos_repo/correoAvisoFinal.png)
![](iconos_repo/correoRecordatorio.png)
## Problemática
En la mayoría de empresas, la información operativa se gestiona en Excel. Ventas tiene un Excel con clientes, RH tiene un Excel con empleados, Logística tiene un Excel con proveedores. Cuando necesitan enviar comunicaciones masivas (cobranzas, boletas, notificaciones, promociones), el proceso es siempre el mismo y es manual:
Una persona del área abre el Excel, filtra el primer registro, copia los datos, abre su correo, redacta un mensaje, busca el archivo adjunto en las carpetas del servidor, lo adjunta, envía, y marca en el Excel que ya realizó el envío. Luego repite para el siguiente registro.

**El problema concreto:**
- Tomar 5-10 minutos por registro significa que para 100 registros se pierde casi un día completo de trabajo
- Los errores son frecuentes: adjuntar archivo equivocado, copiar mal un nombre, omitir destinatarios
- No hay trazabilidad: si en el futuro preguntan por un envío específico, no hay forma de verificarlo directamente
- El proceso depende del personal del área: si se enferma o renuncia, se detiene generando retrasos

## Proceso actual (AS-IS)
![](iconos_repo/AsIs.png)

**Problemas identificados:**
- Proceso manual y repetitivo que consume horas de trabajo
- Alto riesgo de error humano en cada paso
- Sin registro centralizado ni trazabilidad
- Difícil de escalar cuando el volumen crece

## Proceso automatizado (TO-BE)
![](iconos_repo/ToBe.png)

**Beneficios obtenidos:**
- Registros procesados automaticamente en segundos
- Cero errores de personalización o adjuntos
- Auditoría completa 
- El proceso no depende de una persona específica
- Escalable a cualquier volumen

## Comparacion de mejoras en los procesos
![](iconos_repo/Automatizacion.png)


## Arquitectura del Sistema 
**1. Arquitectura en Capas**

![](iconos_repo/Arquitecturadelsistema.png)


**2. Diagrama de Componentes**
![](iconos_repo/DiagramaComponentes.png)

## **Componentes - Estructura del Proyecto**
| Modulo / Archivo | Responsabilidad |
| :--- | :--- |
| `main.py` | **Orquestador principal**: lee CSV, itera sobre registros y coordina el flujo. |
| `data_processor.py` | Carga el CSV con `pandas`, prepara diccionario de datos por cliente. |
| `email_sender.py` | Construye el mensaje MIME (HTML + adjuntos) y envía vía SMTP. |
| `logger_config.py` | Configura los logs `logging` para guardarlos en archivo y salida por consola asegurando persistencia. |
| `config/empresa.py` | Datos de la empresa (nombre, teléfono, dirección, etc). |
| `config/credentials.py` | Credenciales SMTP. |
| `datos/` | Contiene el archivo CSV de datos (exportado desde Excel). |
| `plantillas/` | Archivos HTML con el diseño para los diferentes tipos de correos definiendo varibales de entrada |
| `adjuntos/` | PDFs u otros archivos a adjuntar. |
| `icon/` | Logo de la empresa para incrustar en el cuerpo del correo. |
| `logs_auditoria/` | Archivos de log con registro detallado de cada envío realizado para auditoria. |


## Diagrama de Secuencia (Interacción entre componentes)
![](iconos_repo/secuencias.png)
