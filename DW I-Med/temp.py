import pandas as pd
import pickle

class Paciente: #Guarda la informacion de cada paciente
    def __init__(self):
     self.prestaciones = None

resumen_bonos = pd.read_csv(
        'dba_resumenbonos-2016_muestra.csv', sep='\t')[['numoperacion', 
        'fecemision', 'rutbeneficiario']]
solicitud_vta = pd.read_csv(
        'dba_cfdetsolicitudvta-2016_muestra.csv', sep = '\t',
        encoding = "ISO-8859-1")[['numoperacion', 'codprestacion', 
        'descprestacion']]

merge_resumen_solicitud = pd.merge(
        resumen_bonos, solicitud_vta, on='numoperacion', how='outer')
ruts = merge_resumen_solicitud.rutbeneficiario.unique()

pacientes = {rut: Paciente() for rut in ruts}
for index, row in merge_resumen_solicitud.iterrows():
    pacientes[row['rutbeneficiario']] = (row['fecemision'], row['codprestacion'])
    

pickle.dump(pacientes, open("pacientes.p", "wb"))
