# view?usp\u003ddrivesdk

 
 1 
 
  
Estudios Contables  


![Image 0 from page 0](images/image_0_0.png)

![Image 1 from page 0](images/image_0_1.png)

 
 
 
 2 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024  Generar Resumen por Mes  
 
A continuación, te detallamos los pasos a seguir al momento de generar un listado con 
información útil para confeccionar el Certificado del Art. 80, en el módulo Suel dos y 
Jornales  Web.  
 
¡Esperamos que te sea de utilidad!  
 
Generalidades:  
 
Para poder generar un listado que te sirva de guía al momento de cargar en la página de 
AFIP la Certificación de Servicios de acuerdo al Art. 80 de la Ley de Contrato de Trabajo, 
te sugerimos ingresar en Exportar  > Generar Resumen por Mes.  
 
Desde este menú se podrá generar un resumen por mes en formato Excel.  
 
Se trabajará con la información de la empresa seleccionada.  
 
Creación : Pasos a seguir : 
 
♦ [Nuevo] : desde esta opción se dará de alta un nuevo Archivo, para terminar,  pulsar el 
botón [Confirmar] o [Cancelar].  
 
► Nombre : nombre mediante el cual se hace referencia al archivo. Es único y no 
admite duplicados.  
► Descripción : colocar la descripción deseada por el usuario.  
  
♦ [Configurar ]: se deberá ingresar a este botón para determinar el contenido del listado, 
seleccionando los conceptos de liquidación, contribuciones y/o totalizadores que se 
desea listar.  
 
► Conceptos : se podrá marcar el o los tipos de conceptos que se desean 
seleccionar.  
 
Ítem  Muestra Conceptos con Totalizador de Importe  
Rem. con Descuento  RemConDes y RemConArt  
Rem. con Descuento  RemSinDes  
Asignaciones  Asignaciones y AsiArt  
Retenciones  Retenciones y RetArt  
Obra social y FSR  ObSoc y Asos(*) 
 

![Image 0 from page 1](images/image_1_0.png)

 
 
 
 3 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024  (*) Nota : En este ítem, además de los conceptos que tengan totalizador ObSoc y 
Asos, se visualizará un renglón sin código, con descripción FDO. SOLIDARIO 
REDISTR., si se desea exponer en forma separada el valor calculado en los 
conceptos de Obra Social que tenga c omo destino el Fondo Solidario de 
Redistribución. Tener en cuenta que al seleccionar FDO. SOLIDARIO REDISTR. los 
importes de los conceptos de Obra social se mostrarán por el valor del aporte neto 
del F.S.R.  
 
[Ver Conceptos ]: al ingresar a este botón, se mostrarán los conceptos disponibles de 
acuerdo a la selección anterior. Marcar y seleccionar los que se desee incluir en el 
listado.  
 
[Agregar Neto ]: permite incorporar al listado el importe del neto a cobrar.  
 
► [Contribuciones Generales ]: dentro de este botón se podrán seleccionar los 
siguientes grupos de contribuciones a listar:  
• Seguridad Social  
• Obra Social  
• ART 
• Seguro de Vida  
•  
► [Contribuciones Particulares ]: dentro de este botón se podrán seleccionar los 
conceptos que calculen contribuciones patronales no consideradas en las 
Contribuciones Generales.  
Atención : si un concepto calcula distintas contribuciones patronales podrá ser agregado 
varias veces en la grilla, presionando Otras Variables.  
 
► [Totalizadores ]: dentro de este botón se podrán seleccionar los siguientes 
totalizadores:  
• Remuneración con Descuento  
• Remuneración sin Descuento  
• Asignaciones  
• Retenciones  
• Obra Social y FSR  
• Neto  
 
► Conceptos y Contribuciones a listar : la grilla incluirá los conceptos y contribuciones 
que el usuario haya seleccionado para el listado, mostrando las siguientes columnas:  
• Sel: permite marcar o desmarcar registros de la grilla, para luego eliminarlos.  
• Código : muestra el código de concepto correspondiente, siempre que se trate 
de un registro agregado desde [Conceptos] o [Contribuciones Particulares]. El 
campo estará vacío si se trata del Neto, FSR o de Contribuciones Generales.  
• Descripción : muestra la descripción del concepto o contribución.  

![Image 0 from page 2](images/image_2_0.png)

 
 
 
 4 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024  • Tipo : muestra el origen del registro, es decir, desde qué botón se ha agregado 
(Concepto, Cont. General, Cont. Particular o Totalizador).  
• Totalizador / Variable : en los registros de tipo “Concepto” mostrará el grupo al 
cual pertenece (Rem. con descuento, Asignaciones, Neto, etc.). En los registros 
de tipo “Cont. Particular” se completará por defecto con la variable 
ACU.CP_XXXX contenida en la fórmula del concepto  seleccionado (donde XXXX 
es el nombre arbitrario asignado a la variable de la contribución).  
  
♦ [Generar ]: se deberá ingresar a este botón para generar el listado.  
 
• Período desde / hasta : se sugiere por defecto el mes y año actual. No obstante, 
podrá indicarse un rango diferente.  
• [Elegir Liquidaciones ]: se muestran todas las liquidaciones que fueron calculadas 
para el período desde / hasta elegido. Por defecto todas están seleccionadas. En 
caso de existir liquidaciones sumarizadas, estarán seleccionadas las sumarizadas 
y no las liquidaciones del mismo periodo que se incluyeron en las mismas.  
Haciendo Clic en el casillero de selección ☑ se podr án marcar o desmarcar 
liquidaciones. Para terminar, pulsar el bot ón [Confirmar] o [Cancelar].  
 
Además,  se muestran las columnas Orden, Descripción, Tipo, Período de Pago, 
Sumarizada y Protegida . 
 
☑ Hay Sumarizadas : si está marcado significa que dentro de las liquidaciones 
seleccionadas existe una sumarizada.  
 
☑ Incluir Liquidaciones de Cálculo Auxiliar : si se marca, en Elegir Liquidaciones se 
mostraran las liquidaciones de Cálculo Auxiliar.  
• Opciones:  
☑ Agrupado por : si se marca esta opción, permitirá generar el resumen 
agrupado por Sucursal, Departamento o Sección, debiendo optar por una de esas 
divisiones.  
 
☑ Suprimir columnas de total 0 (cero) : el listado se genera por defecto con una 
columna por concepto o totalizador seleccionado en [Configuración]. Si se marca 
esta opción, no se mostrarán en el listado aquellas columnas cuyo total sea cero.  
 
☑ Mostrar empleados sin datos : el listado se genera por defecto mostrando sólo 
aquellos empleados que tengan al menos un concepto o totalizador de los 
seleccionados en [Configuración]. Si se marca esta opción, se mostrarán además 
aquellos empleados que no tengan ninguno de los concept os y totalizadores 
seleccionados.  
 
☑ Detallar Liquidaciones : el listado se genera por defecto con la información de 

![Image 0 from page 3](images/image_3_0.png)

 
 
 
 5 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024  cada mes. Si se marca esta opción, se generará una segunda solapa en el Excel, 
con el nombre “Liquidaciones” donde se detallará la información por cada 
liquidación que participa. De esta solapa no participarán las Contribuciones 
Generales.  
 
☑ No detallar empleados : el listado se genera por defecto con la información 
detallada para cada empleado. Si se marca esta opción, se mostrará la 
información global (suma de todos los empleados que participan).  
 
☑ Suprimir dato vacío : suprime del listado las filas que están con todos sus 
valores en cero.  
 
Nombre del archivo : El nombre del archivo estará compuesto por el código de la 
empresa, la leyenda “Resumen por mes” y el rango (desde / hasta mes y año) al 
que corresponde.  
  
• [Filtrar Empleados ]: desde ese botón se pueden seleccionar los empleados que 
participarán de la emisión.  
o Filtros : se debe seleccionar cuál de estos comandos va a ejecutarse. Las 
opciones posible son:  
▪ Todos: la exportación se efectuará con todos los legajos 
existentes en la liquidación seleccionada.  
▪ Por Entorno: permite indicar desde qué legajo hasta cuál otro 
participará del archivo de exportación.  
▪  
También se puede filtrar por Sucursal, Área, Departamento, Sección, Gremio y 
Categoría. Están relacionados con los datos ingresados en el legajo del empleado.  
De no elegirse ningún filtro, la generación del archivo contendrá a todos los empleados 
del universo elegido.  
 
• [Ver empleados ]: desde este botón se pueden consultar los empleados que 
responden a los filtros indicados.  
  
♦ [Exportar ]: presionando este botón se generará un archivo en formato Excel, con una 
solapa “Detalle” que contendrá:  
- Columnas para cada año/mes seleccionado en el rango desde / hasta;  
- Una columna por cada concepto y/o contribución seleccionada en el botón  
 
♦ [Configuración]  con el importe acumulado de dicho mes.  
- Columnas de totales de cada grupo (remuneraciones con descuentos, retenciones, 
etc.)  
- Una fila al final del último período con el total de cada columna.  
 

![Image 0 from page 4](images/image_4_0.png)

 
 
 
 6 Estudios Contables  
Sueldos y Jornales  
Septiembre 2024  La información se agrupará por empleado, a menos que se marque la opción  
☑ No detallar empleados . 
Si en [Configuración] se seleccionaron Totalizadores, éstos se mostrarán en una nueva 
solapa.  
Si se marca  ☑ Detallar Liquidaciones  se generará una nueva solapa con la misma 
información, pero detallando los importes por liquidación.  
  
♦ [Copiar] : desde esta opción se podrá copiar el archivo para crear uno nuevo.  
 
 

![Image 0 from page 5](images/image_5_0.png)

