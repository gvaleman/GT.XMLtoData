#Importando librerías
import xml.etree.ElementTree as ET
import pandas as pd

# Cargar y parsear el archivo XML
tree = ET.parse('result_Genome_Detective.xml') #Especificar la ruta al archivo XML
root = tree.getroot()

# Lista para almacenar los datos
data = []

# Iterar a través de cada secuencia y extraer la información
for sequence in root.findall('sequence'):
    sequence_name = sequence.get('name')
    sequence_length = sequence.get('length')
    
    # Buscar el elemento result para esta secuencia (el archivo XML contiene la cadena "result)
    result = sequence.find(".//result[@id='blast']")
    if result is not None:
        # Inicializar valores por defecto para cada campo
        aligned = result.find('aligned').text if result.find('aligned') is not None else None
        start = result.find('start').text if result.find('start') is not None else None
        end = result.find('end').text if result.find('end') is not None else None
        nt_identity = result.find('nt-identity').text if result.find('nt-identity') is not None else None
        aa_identity = result.find('aa-identity').text if result.find('aa-identity') is not None else None
        alignment_method = result.find('alignment-method').text if result.find('alignment-method') is not None else None

        # Extraer <protein-aa-mutations>
        protein_aa_mutations = result.find('protein-aa-mutations').text if result.find('protein-aa-mutations') is not None else None

        # Agregar los datos a la lista
        data.append({
            'sequence_name': sequence_name,
            'sequence_length': sequence_length,
            'aligned': aligned,
            'start': start,
            'end': end,
            'nt-identity': nt_identity,
            'aa-identity': aa_identity,
            'alignment_method': alignment_method,
            'protein_aa_mutations': protein_aa_mutations
        })

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Opcional: Guardar el DataFrame en un archivo CSV
