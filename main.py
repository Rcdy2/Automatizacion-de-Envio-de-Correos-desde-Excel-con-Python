import os
from logs_auditoria.logger_config import logger
from email_sender import enviar_correo
from data_processor import cargar_datos, preparar_datos_cliente

from config.credentials import USER_MAIL
from config.empresa import *

def cargar_plantilla(tipo):
    nombre = "aviso_final.html" if tipo == "AvisoFinal" else "recordatorio.html"
    ruta = os.path.join("plantillas", nombre)
    
    logger.info(f"Cargando plantilla: {nombre}")
    with open(ruta, 'r', encoding='utf-8') as f:
        return f.read()

def reemplazar_variables(plantilla, datos):
    resultado = plantilla
    for clave, valor in datos.items():
        resultado = resultado.replace(f"{{{clave}}}", str(valor))
    return resultado

def main():

    logger.info("INICIANDO AUTOMATIZACIÓN DE COBRANZAS")
    
    df = cargar_datos('datos/Correos.csv')
    
    config_empresa = {
        'nombre_empresa': NOMBRE_EMPRESA,
        'departamento': DEPARTAMENTO,
        'telefono': TELEFONO,
        'email_contacto': EMAIL_CONTACTO,
        'direccion': DIRECCION,
        'url_pagos': URL_PAGOS,
        'email_comprobantes': EMAIL_COMPROBANTES
    }

    RUTA_LOGO = os.path.join('icon', 'empresa1SF.png')
    
    resultados = {
        'exitosos': 0,
        'fallidos': 0
    }
    
   
    for idx, fila in df.iterrows():
        logger.info(f"Procesando {idx + 1}/{len(df)}: {fila['Nombre']}")
        
        try:
            
            datos = preparar_datos_cliente(fila, config_empresa)
            
            plantilla = cargar_plantilla(datos['tipo'])
            cuerpo_html = reemplazar_variables(plantilla, datos)
            
           
            ruta_adjunto = os.path.join('adjuntos', datos['adjunto'])
            exito = enviar_correo(
                destinatarios=[datos['email']],
                usuario=f"{DEPARTAMENTO} <{USER_MAIL}>",
                asunto=datos['asunto'],
                cuerpo_html=cuerpo_html,
                adjunto_ruta=ruta_adjunto,
                ruta_logo=RUTA_LOGO
            )
            
            if exito:
                resultados['exitosos'] += 1
            else:
                resultados['fallidos'] += 1
                
        except Exception as e:
            logger.error(f"Error procesando {fila['Nombre']}: {str(e)}")
            resultados['fallidos'] += 1
    
    # Auditoria final resumen del dia
    logger.info("=" * 50)
    logger.info("RESUMEN FINAL")
    logger.info(f"Envio de Correos Exitosos: {resultados['exitosos']}")
    logger.info(f"Envio de Correos Fallidos: {resultados['fallidos']}")
    logger.info(f"Total de correos enviados: {len(df)}")

if __name__ == '__main__':
    main()