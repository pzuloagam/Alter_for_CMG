# -*- coding: utf-8 -*-
"""
Created on 12/01/2023

@author: PZuloaga
"""

import pandas as pd


def create_alter(excel_input, txt_output):
    df = pd.read_excel(excel_input)
    file_to_delete = open(txt_output, 'w')
    file_to_delete.close()
    # toma los encabezados de excel como nombres de columnas
    df.columns = df.iloc[0]
    # crea lista a partir de las celdas que tienen nombres de pozos
    # y borra columnas que no se usan
    well_list = df.iloc[0][2:]
    df = df.drop([0])
    df = df.drop(columns=["Date_ini"])
    df = df.reset_index(drop=True)
    Date = df["Date"]
    with open(txt_output, 'a') as f:
        for i in [j for j in range(0, len(Date))]:
            line1 = 'DATE ' + str(Date[i]) + '\n'
            f.write(line1)
            for m in [n for n in range(0, len(well_list))]:
                line2 = 'ALTER ' + "'" + str(well_list[m]) + "' \n"
                f.write(line2)
                line3 = '    ' + str(df.iat[i, m+1]) + '\n'
                f.write(line3)


create_alter('WHP_wells.xlsx', 'out.txt')
