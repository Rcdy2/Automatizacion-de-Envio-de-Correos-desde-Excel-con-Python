import pandas as pd
import os
from logs_auditoria.logger_config import logger

def cargar_datos(archivo_csv):
    
    try:
        df = pd.read_csv(archivo_csv, delimiter=';', encoding='latin-1')
        logger.info(f"Datos cargados: {len(df)} registros")
        return df
    except Exception as e:
        logger.error(f"Error cargando CSV: {str(e)}")
        raise

def preparar_datos_cliente(fila, config_empresa):
    monto_formateado = f"S/ {float(fila['Monto']):,.0f}".replace(',', ' ')
    
    numero_doc = fila['Adjunto'].split('_')[-1].replace('.pdf', '') if '_' in fila['Adjunto'] else 'N/A'
    
    datos = {
        'nombre_cliente': fila['Nombre'],
        'email': fila['Email'],
        'empresa_cliente': fila['Empresa'],
        'dias_mora': str(int(float(fila['Dias_Mora']))),
        'fecha_vencimiento': fila['Fecha_Vencimiento'],
        'asunto': fila['Asunto'],
        'tipo': fila['Tipo'],
        'adjunto': fila['Adjunto'],
        'monto_formateado': monto_formateado,
        'numero_doc': numero_doc,
        **config_empresa  
    }
    
    return datos