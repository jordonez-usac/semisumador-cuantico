#MODULOS QISKIT Y MATPLOTLIB
from qiskit_aer import Aer
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

#CREANDO SIMULADOR CUANTICO
simulator = Aer.get_backend('qasm_simulator')

#DEFINIENDO COMBINACIONES DE BITS DE ENTRADA A, B (0 Y 1)
combos = [(0,0), (0,1), (1,0), (1,1)]

#RECORRER COMBINACIONES DE A Y B
for (a, b) in combos:
    #CREAR CARPETA PARA CADA COMBINACIÓN DE A Y B
    carpeta = f"Reporte A = {a} y B = {b}"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    #CREAR CIRCUITO CUANTICO CON 3 QUBITS Y 2 BITS CLASICOS
    qc = QuantumCircuit(3, 2)

    #INICIALIZAR QUBITS EN LOS ESTADOS PROPORCIONADOS
    if a == 1:
        qc.x(0) #APLICANDO LA PUERTA X (NOT) AL QUBIT A PARA CAMBIAR SU ESTADO
    if b == 1:
        qc.x(1) #APLICANDO LA PUERTA X (NOT) AL QUBIT B PARA CAMBIAR SU ESTADO

    #VISUALIZAR Y GUARDAR EL CIRCUITO CUANTICO INICIAL
    plt.figure(figsize=(2,4))
    qc.draw(output='mpl')
    plt.title(f"Grupo No.6 - Circuito Cuántico Inicial A = {a} y B = {b}")
    plt.savefig(f"{carpeta}/Circuito Cuántico Inicial A = {a} y B = {b} (1).png", bbox_inches='tight')
    plt.close()

    #APLICAR PUERTAS CUANTICAS PARA REALIZAR LA SUMA (A + B)
    qc.cx(0, 1)

    #VISUALIZAR Y GUARDAR EL CIRCUITO CUANTICO DESPUES DE APLICAR CNOT 
    plt.figure(figsize=(2,4))

    qc.draw(output='mpl')
    plt.title(f"Grupo No.6 - Circuito Cuántico Después de Aplicar CNOT A = {a} y B = {b}")
    plt.savefig(f"{carpeta}/Circuito Cuántico Suma A = {a} y B = {b} (2).png", bbox_inches='tight')
    plt.close()

    #APLICAR LA PUERTA TOFFOLI (CCNOT) PARA CALCULAR EL ACARREO (A . B)
    qc.ccx(0, 1, 2)

    #VISUALIZAR Y GUARDAR EL CIRCUITO CUANTICO DESPUES DE APLICAR CCNOT
    plt.figure(figsize=(8,4))
    qc.draw(output='mpl')
    plt.title(f"Grupo No.6 - Circuito Cuántico Después de Aplicar CCNOT A = {a} y B = {b}")
    plt.savefig(f"{carpeta}/Circuito Cuántico Acarreo A = {a} y B = {b} (3).png", bbox_inches='tight')
    plt.close()

    #MEDIR LOS QUBITS Y GUARDAR LOS RESULTADOS
    qc.measure(1, 0) #MEDIR QUBIT DE LA SUMA (S)
    qc.measure(2, 1) #MEDIR QUBIT DEL ACARREO (C)

    #VISUALIZAR Y GUARDAR EL CIRCUITO CUANTICO DESPUES DE MEDIR
    plt.figure(figsize=(8,4))
    qc.draw(output='mpl')
    plt.title(f"Grupo No.6 - Circuito Cuántico Final Después de Medir A = {a} y B = {b}")
    plt.savefig(f"{carpeta}/Circuito Cuántico Final A = {a} y B = {b} (4).png", bbox_inches='tight')
    plt.close()

    #SIMULAR EL CIRCUITO CUANTICO Y OBTENER LOS RESULTADOS
    result = simulator.run(qc).result()

    #OBTENER DISTRIBUCIÓN DE PROBABILIDAD DE LOS RESULTADOS
    counts = result.get_counts(qc)

    #MOSTRAR Y GUARDAR LA DISTRIBUCIÓN DE PROBABILIDAD DE LOS RESULTADOS EN UN HISTOGRAMA
    plot_histogram(counts)
    plt.title(f"Grupo No.6 -Distribución de Resultados A {a} = y B = {b}")
    plt.savefig(f"{carpeta}/Histograma Resultados A = {a} y B = {b} (5).png")
    plt.close()

    #MOSTRAR EL RESULTADO MÁS PROBABLE
    resultado = max(counts, key=counts.get) #OBTENER EL RESULTADO MÁS PROBABLE
    suma = resultado[0] #OBTENER EL RESULTADO DE LA SUMA (S)
    acarreo = resultado[1] #OBTENER EL RESULTADO DEL ACARREO (C)

    #GUARDAR LOS RESULTADOS EN UN ARCHIVO DE TEXTO
    with open(f"{carpeta}/Resultados A = {a} y B = {b} (6).txt", "w") as f:
        f.write(f"Resultado de la Suma (S): {suma}\n"),
        f.write(f"Distribución de Probabilidad de los Resultados: {counts}\n")
    
    #VISUALIZAR Y GUARDAR EL ESTADO DE LOS QUBITS DE ENTRADA
    estados = ['0', '1']
    x_labels = ['A', 'B']
    y_values = [a, b]

    plt.bar(x_labels, y_values, color=['blue', 'orange'])
    plt.ylim(-0.5, 1.5)
    plt.ylabel('Estado del qubit')
    plt.title(f'Grupo No.6 - Estados de los Qubits de Entrada A = {a} y B = {b}')
    plt.axhline(y = 0, color = 'black', linewidth = 0.5, linestyle='--')
    plt.axhline(y = 1, color = 'black', linewidth = 0.5, linestyle='--')

    for i, v in enumerate(y_values):
        plt.text(i, v + 0.1, str(v), ha = 'center', va='bottom')

    #GUARDAR EL GRÁFICO DE BARRAS DE LOS ESTADOS DE LOS QUBITS DE ENTRADA  
    plt.savefig(f"{carpeta}/Estados Qubits de Entrada A = {a} y B= {b} (7).png")
    plt.close()

    #GUARDAR UN RESUMEN DETALLADO DE LO QUE OCURRIÓ EN EL CIRCUITO CUÁNTICO
    with open(f"{carpeta}/Resumen A = {a} y B = {b} (8).txt", "w") as f:
        f.write(f"Resumen del Circuito Cuántico para A={a} y B={b}:\n\n")
        f.write(f"Se inicializan los qubits A y B en los estados {a} y {b}, respectivamente.\n")
        f.write(f"Se aplica una puerta CNOT para obtener la suma de A y B.\n")
        f.write(f"Se aplica una puerta Toffoli (CCNOT) para obtener el acarreo de A y B.\n")
        f.write(f"Se mide el qubit 1 para la suma y el qubit 2 para el acarreo.\n")
        f.write(f"ek resultado más probable es suma = {suma} y acarreo = {acarreo}.\n")
        f.write(f"Se genera un histograma con la distribución de probabilidad de los resultados.\n")
        f.write(f"Por último, se muestran los estados de entrada de los qubits A y B.\n")

