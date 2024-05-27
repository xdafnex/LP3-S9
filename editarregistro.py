# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:24:52 2024

@author: Dell
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ UPDATE EDITORIAL
                SET
                    NOMBRE = 'Editorial Imprenta Unión'
                WHERE
                    IDEDITORIAL = 1
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
