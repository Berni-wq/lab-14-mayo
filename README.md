# lab-14-mayo
Parte 1: N-Reinas y Complejidad Espacial en Tiempo Constante

ANÁLISIS DE PUNTOS CRÍTICOS Y ERRORES COMUNES 

1. Error en el Tamaño de los Arreglos (Índices fuera de rango)
Un fallo común es no calcular correctamente el tamaño de los arreglos unidimensionales necesarios para la optimización:
- Columnas (cols): Debe ser de tamaño N.
- Diagonales (diag y anti): Para un tablero de N x N, existen 2N - 1 diagonales.
- El Riesgo: Si se declaran las diagonales con tamaño N, el programa lanzará un error de "index out of bounds" (índice fuera de rango) al intentar acceder a posiciones calculadas como 'row + col' o 'row - col + N - 1'.

2. El "Desfase" en la Diagonal Principal
La guía de laboratorio exige el uso de la fórmula: diag[i - j + N - 1].
- El Fallo: Si el programador intenta usar únicamente 'i - j', obtendrá valores negativos (por ejemplo, en la fila 0, columna 7: 0 - 7 = -7). Los índices de un arreglo no pueden ser negativos en la mayoría de los lenguajes de programación.
- Solución: Es obligatorio sumar el desplazamiento '+ N - 1' para asegurar que todos los índices resultantes sean positivos y mapeen correctamente al arreglo unidimensional.

3. Confusión entre Nodos Visitados y Soluciones
El entregable de la Parte 1 solicita explícitamente el número total de NODOS VISITADOS para N=8 y N=12.
- El Fallo: Un error recurrente es imprimir el número de soluciones encontradas (por ejemplo, 92 para N=8) en lugar de la cantidad total de llamadas recursivas realizadas por el algoritmo.
- Requerimiento: Se debe implementar un contador global que se incremente al inicio de cada función recursiva. Esto es fundamental para evidenciar la reducción de llamadas gracias a la poda algebraica y de factibilidad.

4. No usar la Validación en Tiempo Constante
La rúbrica de evaluación penaliza el uso de bucles (for o while) para revisar la disponibilidad de las diagonales.
- El Fallo: Aunque un código con bucles funcione, no cumple con el objetivo de optimización espacial y temporal O(1).
- Solución Correcta: La validación debe ser una instrucción 'if' simple que consulte directamente los arreglos booleanos: 
  'if not cols[j] and not diag[i - j + N - 1] and not anti[i + j]:'







Parte 2: Sudoku y Heurística de Selección MRV

ESTE PROYECTO IMPLEMENTA UN RESOLUTOR DE SUDOKU EN PYTHON
ESPECÍFICAMENTE DISEÑADO PARA TABLEROS DE NIVEL "DIABÓLICO",
UTILIZANDO EL ALGORITMO DE BACKTRACKING OPTIMIZADO CON LA
HEURÍSTICA MRV (MINIMUM REMAINING VALUES).
1. DESCRIPCIÓN DEL PROYECTO

EL OBJETIVO DE ESTE CÓDIGO ES DEMOSTRAR LA EFICIENCIA DE LAS
HEURÍSTICAS EN PROBLEMAS DE SATISFACCIÓN DE RESTRICCIONES.
MIENTRAS QUE UN TABLERO ESTÁNDAR PUEDE RESOLVERSE CASI SIN
ERRORES, UN NIVEL "DIABÓLICO" PUEDE REQUERIR MILES DE PASOS
DE RETROCESO (BACKTRACKS) SI NO SE UTILIZA UNA ESTRATEGIA
DE SELECCIÓN INTELIGENTE

2. DOCUMENTACIÓN TÉCNICA

A. CLASE SUDOKUSOLVER:
   - __INIT__: INICIALIZA EL CONTADOR DE RETROCESOS A 0.
   - IS_VALID: VERIFICA SI UN NÚMERO CUMPLE LAS REGLAS EN SU
     FILA, COLUMNA Y CUADRANTE DE 3X3.
   - GET_NEXT_CELL_MRV: EL NÚCLEO DE LA OPTIMIZACIÓN. BUSCA
     LA CELDA VACÍA QUE TENGA EL MENOR NÚMERO DE OPCIONES
     VÁLIDAS POSIBLES. ESTO REDUCE EL ÁRBOL DE BÚSQUEDA.
   - SOLVE: MÉTODO RECURSIVO QUE APLICA EL BACKTRACKING.

B. HEURÍSTICA MRV (MINIMUM REMAINING VALUES):
   ESTA TÉCNICA SE BASA EN LA FILOSOFÍA DE "FALLAR RÁPIDO".
   AL COMPLETAR PRIMERO LAS CELDAS MÁS RESTRINGIDAS, EL
   ALGORITMO DETECTA CONFLICTOS MUCHO ANTES QUE UN MÉTODO
   INGENUO O SECUENCIAL.

3. ANÁLISIS DE RENDIMIENTO 
SEGÚN LAS PRUEBAS REALIZADAS EN EL INFORME:
- SUDOKU ESTÁNDAR: EL CONTEO DE BACKTRACKS FUE DE 0 PASOS.
- SUDOKU DIABÓLICO: DEBIDO A LA ALTA COMPLEJIDAD, EL REGISTRO
  ALCANZÓ HASTA LOS 5,000 PASOS DE BACKTRACKING

ESTE INCREMENTO EN LOS PASOS JUSTIFICA LA IMPLEMENTACIÓN DE
ALGORITMOS MÁS AVANZADOS COMO MRV Y LA GESTIÓN EFICIENTE DE
ESTRUCTURAS DE DATOS EN PYTHON.

4. REQUISITOS Y EJECUCIÓN

REQUISITOS:
- PYTHON 3.X

INSTRUCCIONES:
1. DESCARGAR EL ARCHIVO 'SUDOKU_DIABOLICO.PY'.
2. ABRIR UNA TERMINAL EN LA CARPETA DEL ARCHIVO.
3. EJECUTAR EL COMANDO:
   python sudoku_diabolico.py

