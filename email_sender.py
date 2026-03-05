import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import os
from logs_auditoria.logger_config import logger

def enviar_correo(destinatarios, usuario, asunto, cuerpo_html, adjunto_ruta, ruta_logo=None):
   
    from config.credentials import USER_MAIL, PASSWORD
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(USER_MAIL, PASSWORD)

            msg = MIMEMultipart()
            msg['From'] = usuario
            msg['Subject'] = asunto
            msg['To'] = ', '.join(destinatarios)
            
            msg.attach(MIMEText(cuerpo_html, 'html'))


            #Adjunta Img
            if ruta_logo and os.path.exists(ruta_logo):
                with open(ruta_logo, 'rb') as img:
                    logo = MIMEImage(img.read())
                    logo.add_header('Content-ID', '<logo_empresa>')
                    logo.add_header('Content-Disposition', 'inline', filename=os.path.basename(ruta_logo))
                    msg.attach(logo)
                logger.info(f"Logo adjuntado: {os.path.basename(ruta_logo)}")
            else:
                logger.warning(f"Logo no encontrado: {ruta_logo}")
                

            # Adjuntar PDF
            if os.path.exists(adjunto_ruta):
                with open(adjunto_ruta, 'rb') as adj:
                    parte = MIMEApplication(adj.read(), Name=os.path.basename(adjunto_ruta))
                    parte['Content-Disposition'] = f'attachment; filename="{os.path.basename(adjunto_ruta)}"'
                    msg.attach(parte)
                logger.info(f"PDF adjuntado: {os.path.basename(adjunto_ruta)}")
            else:
                logger.warning(f"PDF no encontrado: {adjunto_ruta}")

            server.sendmail(USER_MAIL, destinatarios, msg.as_string())
            logger.info(f"Correo enviado a {destinatarios[0]}")
            return True
            
    except Exception as e:
        logger.error(f"Error enviando correo: {str(e)}")
        return False
    