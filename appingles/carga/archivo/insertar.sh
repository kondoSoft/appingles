#!/bin/bash

PGPASSWORD=rt459pk1 psql -U postgres calificaciones -c "delete from calificaciones_alumnos;"

PGPASSWORD=rt459pk1 psql -U postgres calificaciones -c "\COPY calificaciones_alumnos (ciclo, grado, grupo, salon, nivel, semestre, matricula, lista, nombre, clasificacion_materia, numero_materia, nombre_materia, calif_sep, calif_oct, calif_nov, calif_dic, calif_ene, calif_feb, calif_mar, calif_may, calif_jun, primer_trimestre, promedio) FROM '/opt/sites/appingles/appingles/carga/archivo/califica.txt' ENCODING 'utf-8';"
