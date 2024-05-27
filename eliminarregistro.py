# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:24:01 2024

@author: Dell
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ DELETE FROM EDITORIAL
                WHERE
                    IDEDITORIAL = 5
            """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
