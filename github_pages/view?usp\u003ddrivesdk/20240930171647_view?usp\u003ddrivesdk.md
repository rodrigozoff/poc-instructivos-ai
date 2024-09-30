# view?usp\u003ddrivesdk

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Estudios  Contables  
1 

![Image 0 from page 0](images/image_0_0.png)

Estudios  Contables  
2 Estudios  Contable s 
Junio 202 4 
  
  
 
CÁLCULO  DE AGUINALDO  
A continuación, te detallamos las generalidades a tener en cuenta para   
poder realizar la liquidación del Sueldo Anual Complementario en el  módulo  
Sueldos y  Jornales  Web . 
¡Esperamos  que te sea de utilidad!  
 
CONSIDERACIONES PREVIAS  
Antes de calcular, es importante controlar que las remuneraciones del 
semestre hayan sido actualizadas en forma correcta y completa. Esto puede 
revisarse desde Emisiones > Sueldo Anual Complementario > Detalle de 
Remuneraciones por Semestre.  
Si encuentra allí meses en blanco debe proceder a actualizar las liquidaciones 
correspondientes. Si observa valores que no considera correctos, debe 
corregirlos previo al cálculo del Aguinaldo. Puede consultar al efecto nuestro 
instructivo titulado “ ACTUALIZAR TOTALIZADORES PARA ACOMODAR 
TABLAS ” haciendo clic aquí.   
 
CONCEPTO DE LIQUIDACIÓN PREVISTO  
El concepto previsto por el sistema es el 0298 00 AGUINALDO . Este concepto  
podrás  incluirlo en la  liquidación de  distintas  formas:  
• Agregando  el concepto  a cada  empleado  que corresponda  en 
Liquidación > Novedades . 
• Desde la opción Liquidación > Novedades , botón [Modificación Masiva] , 
para cargarlo simultáneamente a todos los empleados de la liquidación 
o a un grupo determinado.  
• Colocando en la Carátula de la liquidación la letra G en el campo  Códigos  
Condiciones , para  liquidar  el concepto  a todos  los empleados  que 
participan  de la liquidación,  sin cargar  en Novedades.  
 
 
 
 
 

![Image 0 from page 1](images/image_1_0.png)

Estudios  Contables  
3 Estudios  Contable s 
Junio 202 4 
  
  
CÁLCULO AUTOMÁTICO  
El sistema tomará la mejor remuneración  del semestre , esto lo puede ver  de la 
Tabla  HABERES  que se  encuentra en el menú Empleados > Tablas de 
Empleados . Por lo  tanto, enfatizamos que es necesario que la misma se 
encuentre completa para el semestre.  La tabla se completa automáticamente 
al ejecutar todos los meses el proceso Actualizar totalizadores  sobre las 
liquidaciones realizadas. Tomará    los valores de las columnas REMCONDES, 
CORRECCIÓN, CORRECC.OTROS,  PREST.REM.EMP y PREST.REM.ART del 
semestre para la selección de la  mejor  remuneración.  
La columna CORRECC.OTROS puede tener datos provenientes de  conceptos 
remunerativos que tengan el totalizador NOSAC  en el campo  Totalización 
Importe. Permite no considerar un concepto en la base de la  mejor 
remuneración. Se utiliza para conceptos que deben considerarse  para el cálculo 
de SAC en otro periodo distinto del de pago, por ejemplo,  0080 00 
RETROACTIVOS.  
La columna  CORRECCIÓN  puede  tener  datos provenientes  de la liquidación   de 
vacaciones, si hay días de vacaciones que correspondieron a meses  distintos al 
de liquidación, y se calcularon colocando la fecha de inicio de  las vacaciones en 
el legajo del empleado. Te sugerimos ver más detalles en  Ayuda > Temas de 
Ayuda de Sueldos y Jornales > Capítulo 9 – Cálculo de Vacaciones . 
 
Toda esta  información, puede visualizarse ingresando el menú  Emisiones  > 
Sueldo  Anual  Complementario  > Detalle  de remuneraciones  por semestre . El 
mejor Total General del semestre será el que el sistema  tomará  como  base  de 
cálculo  de SAC.  
 
Importante : Respecto de los valores acumulados : Si el sueldo del mes de Junio 
o Diciembre, todavía no ha sido  calculado ni actualizado, y tampoco lo liquida 
junto con el aguinaldo, no participará  en la  elección de  la mejor remuneración 
del semestre.  
Asimismo, tener en cuenta que,  si está liquidándose el sueldo y el SAC en un 
recibo conjunto, si realizó y actualizó una liquidación del sueldo exclusivamente 
por el mismo mes, se duplicará el valor del sueldo (el sistema tendrá en cuenta 
que la remuneración está compuesta por el valor  de la liquidación anterior ya 
guardada en tablas más el valor del sueldo que se está liquidando en la carátula 
actual).  

![Image 0 from page 2](images/image_2_0.png)

Estudios  Contables  
4 Estudios  Contable s 
Junio 202 4 
  
  
PROPORCIÓN DEL TIEMPO TRABAJADO  
 
Ingresos del semestre : el sistema proporcionará el SAC desde la fecha de  
ingreso al 30/06 o 31/12, según corresponda. De la misma manera  
proporcionará su correspondiente control de bases imponibles mínimas y  
máximas.  
De existir licencia por maternidad y/o días no trabajados con pago de  
prestaciones dinerarias, no serán considerados tiempo trabajado para el  cálculo  
del SAC. 
 
Licencias por maternidad : Si se informó el período de la licencia, y éste se  
encuentra comprendido en el periodo semestral del SAC, no será  considerado  
como  tiempo  trabajado  a los fines  de su cálculo.  
Esta situación será advertida por el sistema en el proceso de Verificación . Si se  
deseara computar este período como trabajado, se deberá ingresar desde 
Empresa > Complementos , botón [Agregar Disponibles] , y agregar la SACLMAT  
con el valor SI. 
 
Recordar que, para informar el período de licencia por maternidad, se debe 
ingresar en Empleados > Legajo , [Complementos]  y agregar la variable:  
LIC_MATERNIDAD  con el valor ddmmaaaa -ddmmaaaa  (dd=día, mm=mes, 
aaaa=año correspondiente al inicio y fin respectivamente) . 
 
Prestaciones dinerarias : No serán considerados como tiempo trabajado a los 
fines del cálculo del SAC los días por los cuales se hayan abonado prestaciones  
dinerarias.  
Esta situación será advertida por el sistema al ejecutar el proceso de  
Verificación . El sistema  detectará  los períodos  de prestaciones  dinerarias  de los 
datos guardados en tabla ACCIDENTES (Empleados > Tablas de  Empleados ) y 
de las fechas de inicio y reintegro de las situaciones  invalidantes  informadas  en 
Empleados  > Legajo  > botón  Complementos : FSINV  y en Valor completar con 
dd/mm/aaaa  para el inicio y FREINT  y en Valor completar con dd/mm/aaaa  
para el reintegro).  
 
Licencias sin goce de haberes, ausencias injustificadas, etc .: Si se  informaron 
utilizando conceptos con Totalizador Unidad DInj, no serán  considerados  como  
tiempo  trabajado  a los fines  de su cálculo.  
Si se deseara  computar este  periodo  como  trabajado,  se deberá  ingresar  la 
variable  DIASNETOS  y en Valor completar con  NO en Empres a > Complementos  

![Image 0 from page 3](images/image_3_0.png)

Estudios  Contables  
5 Estudios  Contable s 
Junio 202 4 
  
 presionando el botón  [Agregar Disponibles].  
 
Suspensiones Art. 223 BIS - LCT: Si en el semestre se liquidaron días por 
suspensión Art. 223 BIS - LCT, los mismos serán considerados como tiempo 
trabajado a los fines de su cálculo.  
Si no se deseara computar este periodo como trabajado, se deberá ingresar por 
novedades, en el concepto de Aguinaldo, en la columna PORCENTAJE , la 
cantidad de días correspondientes a la suspensión.  
 
CÁLCULO MANUAL  
Si no tuviera completa la tabla de HABERES , o no estuviera de acuerdo  con el 
importe determinado por el sistema, se podrá ingresar el concepto  0298 00 
AGUINALDO en Liquidación > Novedades , indicando directamente el  importe  
que desees abonar.  
 
PASOS PARA LIQUIDAR  
 
Sueldo y SAC en el mismo recibo  
 
Si se desea  ejecutar  un Cálculo  automático , podrá  elegir  entre  una de estas  dos 
opciones:  
 
Opción 1 : en Liquidación > Nuevo  / Selección Liquidación  insertar en el campo 
Códigos  Condiciones  la letra  G, de este  modo  el SAC se calculará  sin necesidad 
de ingresar el código  por la opción  de Novedades.  
 
 


![Image 0 from page 4](images/image_4_0.png)

![Image 1 from page 4](images/image_4_1.png)

Estudios  Contables  
6 Estudios  Contable s 
Junio 202 4 
  
  
Opción  2: en Liquidación  > Novedades  insertar  el código  0298 00 AGUINALDO  
sin informar nada.  Desde el botón [Modificación Masiva]  podrá insertar dicho 
concepto a todos los empleados de una sola vez.  
 
SAC en Recibo Separado del sueldo  
 
Para liquidar el SAC en un recibo separado, en Período Pago  de la Carátula  de 
la liquidación, deberá colocar como tipo de liquidación “ Aguinaldo ”. 
 
Además, deberá utilizar Códigos de Condiciones  que bloqueen el cálculo de los 
Conceptos Fijos, para que sólo salga el aguinaldo en el recibo. La  exclusión de 
conceptos mediante Códigos de Condición podrá efectuarla para todos los 
empleados que participan de la liquidación o sólo para algunos.  
 
Si el concepto que no se debe calcular es, por ejemplo, el código 001000 
SUELDO MENSUAL , dicho concepto tiene en Archivo > Conceptos de 
Liquidación  > Cond. Carátula: -S. En la carátula de la liquidación (en el campo 
Códigos Condiciones ) deberá colocar la letra S (sin signo):  
 
 
 


![Image 0 from page 5](images/image_5_0.png)

![Image 1 from page 5](images/image_5_1.png)

Estudios  Contables  
7 Estudios  Contable s 
Junio 202 4 
  
  
 
En el recibo de sueldo aparecerá, en el lugar correspondiente al Período  
Abonado , la palabra  “Aguinaldo ”. 
 
 
Luego proceder de la forma indicada anteriormente para el Cálculo  automático 
(Pasos para liquidar: Opción 1: Recordar que,  en Código  Condiciones de la 
Carátula, se deberá agregar además la letra G) o el  Cálculo  manual.  
 
Importante : si se realiza un cálculo automático tener en cuenta que el  sistema  
considerará  los meses  que se encuentran  en la Tabla  HABERES . Si el mes de 
Junio o Diciembre  todavía no fue calculado ni actualizado, no participará  en la 
elección de la mejor remuneración del semestre.  


![Image 0 from page 6](images/image_6_0.png)

![Image 1 from page 6](images/image_6_1.png)

![Image 2 from page 6](images/image_6_2.png)

Estudios  Contables  
8 Estudios  Contable s 
Junio 202 4 
  
  
CONTROL DE BASES MÍNIMAS Y MÁXIMAS DE SEGURIDAD SOCIAL Y OBRA 
SOCIAL.  
El sistema automáticamente realizará control de bases mínimas y  máximas por 
separado para el Sueldo y el SAC. Para mayor información,  sugerimos visualizar 
en Ayuda > Temas de Ayuda de Sueldos y Jornales > Capítulo 9 - Procesos Útiles 
> Bases Mínimas y Máximas de Seguridad Social y Obra Social.  
 
CODIFICACIÓN AFIP  
Al concepto 0298 00 AGUINALDO  sugerimos codificarlo con 120000 – Sueldo 
anual complementario . 
 

![Image 0 from page 7](images/image_7_0.png)

