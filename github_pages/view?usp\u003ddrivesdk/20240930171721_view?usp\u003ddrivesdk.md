# view?usp\u003ddrivesdk

 1 
 
  
Estudios Contables  


![Image 0 from page 0](images/image_0_0.png)

![Image 1 from page 0](images/image_0_1.png)

 
 
 
 2 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024  Codificación Propia  
 
A continuación, te detallamos los pasos a seguir para poder utilizar Codificación Pro pia 
en el módulo Sueldos y Jornales  Web.  
¡Esperamos que te sea de utilidad!  
 
Esta opción del módulo posibilita que el usuario elija, para una empresa específica, 
trabajar con una cantidad determinada de conceptos de liquidación del total de 
conceptos definidos en el menú Archivo.  
 
Esta elección le otorgará agilidad en los procesos, pudiendo asimismo modificar el 
número de código y la descripción de los conceptos seleccionados para esa empresa 
en particular.  
 
1. Crear la Codificación Propia en la Empresa  
 
La habilitación puede realizarse en el momento de definición de la empresa o con 
posterioridad (luego de haber utilizado Conceptos de Liquidación) desde Empresa  > 
Codificación Propia  > Habilitar/Deshabilitar Conceptos Propios.   
En este último caso, el sistema advertirá que en la empresa ya existen conceptos 
utilizados en los empleados (tanto en Conceptos fijos como en Novedades) y 
preguntará si se desea darlos de alta automáticamente en la Codificación Propia.  
 
 
 
2. Dar de alta los Conceptos en la Codificación Propia  
 
► [Agregar Conceptos ]: Al ingresar en este botón accederá a la lista de Conceptos de 
Liquidación ya definidos desde el menú Archivo  > Conceptos de Liquidación.  Haciendo 
clic en el casillero de selección ☑ podr á ir marcando todos los que desee formen parte 
de los conceptos particulares de la empresa elegida. Para terminar, pulsar el bot ón 
[Seleccionar] o [Cancelar].  
 


![Image 0 from page 1](images/image_1_0.png)

![Image 1 from page 1](images/image_1_1.png)

 
 
 
 3 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024   
 
Si se desea agregar más de una vez al mismo concepto, se deberá volver a ingresar y 
seleccionarlo nuevamente.  
 
Importante : no se encuentran disponibles para seleccionar los conceptos que el 
sistema lleva identificados como Librerías obligatorias Estos son : 000001, 000903 a 
000908, 000920, 000925, 000926, 000930 a 000933 y 000950 . Por defecto serán leídos 
del archivo general.  
 
► Grilla de conceptos: En la grilla inferior se muestran todos los conceptos 
seleccionados para la empresa elegida.  
 
• Código Concepto : esta columna refleja los números de códigos originales de 
cada concepto, tal cual como existen definidos en el menú Archivo. Es sólo 
como referencia, no puede alterarse.  
• Código Alternativo : en esta columna se ingresan los números de códigos que el 
usuario va a ver como propios. Al seleccionarlos se muestran los mismos 
códigos que los originales, pero pueden modificarse para asignarle la 
numeración que se desee. No existe aquí ningún rango n umérico a respetar a 
excepción del orden lógico de cálculo.  
 
Importante : tener en cuenta que el número de orden alternativo del concepto afecta 
el orden del cálculo. Si se desea que el importe de un concepto sea base de cálculo de 
otro, debe tener un código anterior al del concepto que necesita de su importe.  
 
3. Situaciones Prácticas  
 
Ejemplo  1:  
Al concepto de Jubilación, se le deberá asignar un código alternativo posterior al 
código que se le asigne al último que haya definido como remuneraciones sujetas a 
descuento, como se indica, ya que sino no tendrá base de cálculo.  
 
Código 001000 – SUELDO MENSUAL  
Código 001001 – ANTIGÜEDAD  
Código 001002  – JUBILACIÓN  


![Image 0 from page 2](images/image_2_0.png)

![Image 1 from page 2](images/image_2_1.png)

 
 
 
 4 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024   
Atención: el código 000001  está reservado para el  __INICIALIZADOR__  (es una Librería 
del sistema). No puede asignársele a otro concepto que no responda a estas 
características.  
 
Descripción:  se muestra por defecto la misma que corresponde al código definido en 
Archivo. Puede cambiarse por la que desee el usuario que figure en el recibo de 
sueldo.  
 
Sugerencia : con esta opción puede insertarse varias veces el mismo concepto, sin la 
necesidad de crear desde el menú Archivo > Conceptos de Liquidación  diferentes 
conceptos cuyas fórmulas son iguales. Automáticamente al asignarle diferente código 
alternativo y diferente descripción, será considerado como un concepto diferente.  
 
Ejemplo  2:  
Se necesita que salga impreso en el recibo de sueldo el código de la Obra Social, 
reflejando el nombre de la misma. Para esto basta con seleccionar el código 031000 
OBRA SOCIAL , tantas veces como se necesite y asignarle diferentes códigos 
alternativos y descripción. Luego elegir el que corresponda desde los Conceptos Fijos 
de cada empleado.  
 
• (+/-), Quincena, Cond. Nov, Cond. Car. y Totalizadores: para estos campos por 
defecto se sugieren los mismos datos que corresponden al código definido en 
Archivo. Pueden cambiarse por los que desee el usuario.  
 
• Dec. en Línea: en esta columna se reflejará la clasificación asociada a cada 
concepto para componer la información requerida por Declaración en Línea, 
botón Datos complementarios. Se mostrará por defecto la definida en Útiles  > 
Conceptos de Liquidación  > Clasificación Declaración en Línea.  Podrá 
personalizarse haciendo clic sobre el campo y seleccionando la clasificación que 
necesite asociar.  
 
• Cód. AFIP LSD: en esta columna se podrá asociar el Código AFIP Datos 
complementarios. Se mostrará por defecto la definida en Útiles  > Conceptos de 
Liquidación  > Realizar Codificación AFIP - Libro de Sueldos Digital. Podrá 
personalizarse haciendo clic sobre el campo y seleccionando la clasificación que 
necesite asociar.  
 
• ☑ Librería: la marca de un concepto como Librería, implica que el sistema 
trabajará con las rutinas del código que se está ingresando aquí, ignorando 
todos los conceptos identificados como Librerías desde Archivo  > Conceptos de 
Liquidación.  No hay que marcar esta columna salvo que el código elegido 
responda a esta característica. Si se marca algún concepto como Librería 

![Image 0 from page 3](images/image_3_0.png)

 
 
 
 5 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024  deberán elegirse todos los restantes que el sistema tenga reconocido como 
tales desde los archivos principales.  
 
Importante : la única excepción se da con el código 000001 Inicializador. Si se tiene un 
código 000001 propio, el sistema lo marca automáticamente como Librería y 
considerará el resto de los conceptos identificados como Librerías desde el Archivo 
principal.  
 
► [CODIFICACION AFIP GENERAL]: en caso de haber modificado Cód. AFIP LSD de 
algún concepto, desde esta opción se podrán restablecer las que el concepto posee en 
Archivo > Conceptos de Liquidación.  En una grilla se visualizarán los conceptos con 
alguna modificación, indicando en la columna “Cód. AFIP Codif. Propia” la clasificación 
asignada por el usuario, y en la columna “Cód. AFIP Codif. Gral“, la clasificación del 
archivo general del sistema. Se podrán marcar todos o algunos conceptos cuya 
clasificación se desee recuperar indicándolo con un tilde en la columna de selección.  
 
 
 
► [CLASIFICACION DECLARACIÓN EN LÍNEA]: en caso de haber modificado 
clasificaciones, desde esta opción se podrán restablecer las que el concepto posee en 
Archivo > Conceptos de Liquidación.  En una grilla se visualizarán los conceptos con 
alguna modificación, indicando en la columna “Personalizado”, la clasificación asignada 
por el usuario, y en la columna “Predeterminada”, la clasificación del archivo general 
del sistema. Se podrán marcar to dos o algunos conceptos cuya clasificación se desee 
recuperar indic ándolo con un tilde en la columna de selección.  
 
♦ [Visualizar] : desde esta opción se podrá visualizar.  
♦ [Modificar] : desde esta opción se podrá modificar.  
♦ [Eliminar] : desde esta opción se podrá dar de baja.  


![Image 0 from page 4](images/image_4_0.png)

![Image 1 from page 4](images/image_4_1.png)

 
 
 
 6 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024   
 
Sugerencia:  Ver Ayuda  > Temas de Ayuda de sueldos y Jornales  > Empresas→ 
Codificación Propia  > Habilitar / Deshabilitar Conceptos Propios , para obtener más 
información acerca del proceso.  
 
 
 
 
 
 
 
 
 
 
 
 


![Image 0 from page 5](images/image_5_0.png)

![Image 1 from page 5](images/image_5_1.png)

