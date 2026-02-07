const nodemailer = require('nodemailer');

// ============================================
// CONFIGURACIÓN DE NODEMAILER
// ============================================
// Verificar si las credenciales están configuradas
const emailUser = process.env.EMAIL_USER || 'venesenas.app@gmail.com';
const emailPassword = process.env.EMAIL_PASSWORD;

let transporter;
let emailsEnabled = false;

try {
  if (emailPassword && emailPassword !== 'tu_contraseña_de_aplicación') {
    // Crear transportador real si hay credenciales
    transporter = nodemailer.createTransporter({
      service: 'gmail',
      auth: {
        user: emailUser,
        pass: emailPassword
      }
    });
    emailsEnabled = true;
    console.log('✅ Servicio de email configurado correctamente');
  } else {
    console.warn('⚠️ EMAIL NO CONFIGURADO: Correos en modo simulación');
    console.warn('⚠️ Configura EMAIL_USER y EMAIL_PASSWORD en .env');
    emailsEnabled = false;
  }
} catch (error) {
  console.error('❌ Error configurando servicio de email:', error);
  emailsEnabled = false;
}

// ============================================
// TEMPLATE DE EMAIL CON DEGRADADO
// ============================================
const getEmailTemplate = (title, content, buttonText, buttonUrl) => {
  return `
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f5f5f5;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f5f5f5; padding: 20px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color: white; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
          
          <!-- Header con degradado -->
          <tr>
            <td style="background: linear-gradient(135deg, #FFC107 0%, #2196F3 50%, #F44336 100%); padding: 40px 30px; text-align: center;">
              <h1 style="margin: 0; color: white; font-size: 32px; font-weight: bold; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                VeneSeñas
              </h1>
              <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.95); font-size: 16px;">
                Aprende Lengua de Señas Venezolana
              </p>
            </td>
          </tr>

          <!-- Contenido -->
          <tr>
            <td style="padding: 40px 30px;">
              <h2 style="margin: 0 0 20px 0; color: #333; font-size: 24px;">
                ${title}
              </h2>
              <div style="color: #666; font-size: 16px; line-height: 1.6; margin-bottom: 30px;">
                ${content}
              </div>

              ${buttonUrl ? `
              <!-- Botón -->
              <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td align="center" style="padding: 20px 0;">
                    <a href="${buttonUrl}" style="display: inline-block; background-color: #2196F3; color: white; text-decoration: none; padding: 15px 40px; border-radius: 8px; font-size: 16px; font-weight: bold; box-shadow: 0 4px 6px rgba(33, 150, 243, 0.3);">
                      ${buttonText}
                    </a>
                  </td>
                </tr>
              </table>
              ` : ''}

              <p style="color: #999; font-size: 14px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee;">
                Si no solicitaste esto, puedes ignorar este email.
              </p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color: #f9f9f9; padding: 20px 30px; text-align: center; border-top: 1px solid #eee;">
              <p style="margin: 0; color: #999; font-size: 14px;">
                © 2026 VeneSeñas. Todos los derechos reservados.
              </p>
              <p style="margin: 10px 0 0 0; color: #999; font-size: 12px;">
                Este es un correo automático, por favor no respondas.
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
  `;
};

// ============================================
// ENVIAR EMAIL DE RECUPERACIÓN DE CONTRASEÑA
// ============================================
const sendPasswordResetEmail = async (email, resetToken, userName = 'Usuario') => {
  // Modo simulación si no hay credenciales
  if (!emailsEnabled) {
    console.log('📧 [SIMULACIÓN] Email de recuperación enviado a:', email);
    console.log('🔑 [SIMULACIÓN] Token:', resetToken);
    return { 
      success: true, 
      messageId: 'simulated-' + Date.now(),
      simulated: true 
    };
  }

  const resetUrl = `https://tu-app.com/reset-password?token=${resetToken}`;
  
  const content = `
    <p>Hola <strong>${userName}</strong>,</p>
    <p>Recibimos una solicitud para restablecer la contraseña de tu cuenta en VeneSeñas.</p>
    <p>Haz clic en el botón de abajo para crear una nueva contraseña. Este enlace es válido por <strong>1 hora</strong>.</p>
  `;

  const mailOptions = {
    from: '"VeneSeñas" <venesenas.app@gmail.com>',
    to: email,
    subject: '🔐 Restablece tu contraseña - VeneSeñas',
    html: getEmailTemplate(
      '¿Olvidaste tu contraseña?',
      content,
      'Restablecer Contraseña',
      resetUrl
    )
  };

  try {
    const info = await transporter.sendMail(mailOptions);
    console.log('✅ Email enviado:', info.messageId);
    return { success: true, messageId: info.messageId };
  } catch (error) {
    console.error('❌ Error enviando email:', error);
    return { success: false, error: error.message };
  }
};

// ============================================
// ENVIAR EMAIL DE BIENVENIDA
// ============================================
const sendWelcomeEmail = async (email, userName) => {
  const content = `
    <p>¡Hola <strong>${userName}</strong>!</p>
    <p>Bienvenido a <strong>VeneSeñas</strong>, tu aplicación para aprender Lengua de Señas Venezolana (LSV).</p>
    <p>Estamos emocionados de tenerte en nuestra comunidad. Comienza tu viaje de aprendizaje hoy mismo:</p>
    <ul style="color: #666; line-height: 1.8;">
      <li>🎯 Aprende vocabulario básico</li>
      <li>🏆 Gana estrellas y sube de nivel</li>
      <li>📚 Practica con ejercicios interactivos</li>
      <li>🎮 Diviértete mientras aprendes</li>
    </ul>
  `;

  const mailOptions = {
    from: '"VeneSeñas" <venesenas.app@gmail.com>',
    to: email,
    subject: '🎉 ¡Bienvenido a VeneSeñas!',
    html: getEmailTemplate(
      '¡Bienvenido a VeneSeñas!',
      content,
      'Comenzar a Aprender',
      'https://tu-app.com/'
    )
  };

  try {
    const info = await transporter.sendMail(mailOptions);
    console.log('✅ Email de bienvenida enviado:', info.messageId);
    return { success: true, messageId: info.messageId };
  } catch (error) {
    console.error('❌ Error enviando email de bienvenida:', error);
    return { success: false, error: error.message };
  }
};

// ============================================
// ENVIAR EMAIL DE CONFIRMACIÓN DE CAMBIO DE CONTRASEÑA
// ============================================
const sendPasswordChangedEmail = async (email, userName) => {
  const content = `
    <p>Hola <strong>${userName}</strong>,</p>
    <p>Te confirmamos que tu contraseña ha sido cambiada exitosamente.</p>
    <p><strong>¿No fuiste tú?</strong> Si no realizaste este cambio, contacta inmediatamente con nuestro equipo de soporte.</p>
  `;

  const mailOptions = {
    from: '"VeneSeñas" <venesenas.app@gmail.com>',
    to: email,
    subject: '✅ Contraseña Cambiada - VeneSeñas',
    html: getEmailTemplate(
      'Tu contraseña ha sido actualizada',
      content,
      null,
      null
    )
  };

  try {
    const info = await transporter.sendMail(mailOptions);
    console.log('✅ Email de confirmación enviado:', info.messageId);
    return { success: true, messageId: info.messageId };
  } catch (error) {
    console.error('❌ Error enviando email de confirmación:', error);
    return { success: false, error: error.message };
  }
};

module.exports = {
  sendPasswordResetEmail,
  sendWelcomeEmail,
  sendPasswordChangedEmail
};
