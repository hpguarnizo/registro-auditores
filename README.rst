Registro de Auditores
=====================

El Registro de Auditores, es una aplicación web desarrollada en Django con la finalidad de automatizar el proceso de registro de las personas que deseen formar parte del grupo de un grupo de auditores autorizados.

Requerimientos
==============

Accesos al sistema
------------------

- [Listo]: Registro de nuevos usuarios (Auditores, Administrador, [Pendiente]: Proveedores).
- [Listo]: Inicio de sección para usuarios registrados.
- [Listo]: Incorporación de Capcha.
- [Listo]: Validación de clave fuerte.
- [Listo]: Recuperación de clave (Validación mediante correo electrónico).
- [Listo]: Validación de usuario.

Módulo de administrador
-----------------------

- [Listo]: Gestión de usuarios.
- [Listo]: Gestión de auditores (Estatus: No Acreditado – Acreditado – Desacreditado; Se deberá indicar el motivo).
- [Pendiente]: Gestión de PSCs (Agregar, Modificar, Eliminar y gestionar estatus activo/inactivo).
- [Listo]: Confirmación de la cita para la entrevista por correo electrónico.
- [Listo]: Recordatorio del vencimiento de la acreditación como auditor por correo electrónico.
- [Listo]: Gestión de evaluación de los candidatos a auditor y renovación de los auditores.
- [Pendiente]: Gestión de carga del certificado electrónico.
- [Pendiente]: Implementación del applet para firmar los datos ingresados.
- [Listo]: Cambio de contraseña.

Módulo de información personal, académica y experiencia profesional
-------------------------------------------------------------------

- [Listo]: Formularios de ingreso de datos personal.
- [Listo]: Formularios de ingreso de información académica.
- [Listo]: Formulario de ingreso de experiencia profesional.
- [Listo]: Formulario de ingreso de competencias.
- [Listo]: Formulario de ingreso de habilidades.
- [Listo]: Formulario de ingreso para otros conocimientos.
- [Listo]: Formulario de ingreso de idiomas.
- [Listo]: Formulario de programación de citas.
- [Listo]: Gestión de carga del certificado electrónico.
- [Listo]: Implementación del applet para firmar los datos ingresados.
- [Listo]: Cambio de contraseña.

Seguridad
---------

- [Listo]: Implementar medidas de seguridad y validaciones de ingreso de datos en los formularios (tamaño de campos, tipo de datos, validaciones lógicas, entre otros), con la intención de evitar por ejemplo ataques de Crosssite scripting XSS, inyección de código SQL entre otros ataques comunes.
- [Parcial]: Gestión de paginas de error.
- [Pendiente]: Implementar módulos de seguridad como por ejemplo: web mod_security, mod_evasive y greensql.
- [Pendiente]: Implementar sistema de Prevención/Detección de intrusos para bloquear/alertar sobre solicitudes HTTP maliciosas, se sugiere una herramienta llamada OSSEC.
- [Pendiente]: Destrucción de variables sesión.
- [Pendiente]: Ocultar los datos del servidor web.
- [Listo]: Manipulación de cookies seguras.
- [Listo]: Enmascaramiento de URL en la barra de direcciones del navegador.

Instalación
===========

1) Clonación de repositorio (debe tener permisos para ello)::

 $ git clone https://github.com/suscerte/registro-auditores.git

2)  Ingresar en el archivo clonado::

 $ cd registro-auditores

4)  Generar el entorno virtual dentro del directorio creado::

 $ virtualenv virtualenv/

5)  Activar el entorno virtual::

 $ . virtualenv/bin/activate

6)  Instalar paquetes adicionales (compresor de estáticos, barra para debug, entre otros)::

 $ pip install -r requirements.txt

7)  Sincronizar la base de datos con los modelos existentes::

 $ python manage.py syncdb

8) Migrar data necesaria::
 $ python manage.py migrate

9)  Cargar data inicial (lista de idiomas, estados, entre otros)::

 $ python manage.py loaddata main/fixtures/*

10)  Sincronizar los archivos estáticos::

 $ python manage.py collectstatic

11)  Comprimir los archivos estáticos (opcional)::

 $ python manage.py compress

12)  Iniciar el servidor::

 $ python manage.py runserver

13)  Abrir la aplicación en el navegador con la dirección: http://localhost:8000
