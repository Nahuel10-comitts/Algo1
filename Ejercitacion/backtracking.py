matrix = [  [' ',' ',' ',' ',' ',' ',' ','P'],
            ['P','P','P','P','P',' ','P','P'],
            ['P',' ',' ',' ','P',' ',' ',' '],
            ['P',' ','P',' ','P','P','P',' '],
            ['X',' ','P',' ',' ',' ',' ',' '] ]

def mostrar(m):
   for i in range(0,len(m)):
      for j in range(0,len(m[i])): print (m[i][j], end='')
      print ("")

def buscarSalida(m, f, c):
    print('Analizando {0},{1}'.format(f,c))
    salir = False
    if m[f][c]=='X':
        print('Saliendo por {0},{1}'.format(f,c))
        salir = True
    elif m[f][c]=='P':
        print('Pared en {0},{1}'.format(f,c))
        salir = False
    elif m[f][c]=='.':
        print('Ya pasamos por {0},{1}'.format(f,c))
        salir = False
    else: # m[f][c] == ' '
        print('Visitando {0},{1}'.format(f,c))
        m[f][c]='.'
        if (f<len(m)-1):
            salir = buscarSalida(m, f+1, c)
        if (not salir and c>0):
            salir = buscarSalida(m, f, c-1)
        if (not salir and f>0):
            salir = buscarSalida(m, f-1, c)
        if (not salir and c<len(m[0])-1):
            salir = buscarSalida(m, f, c+1)
    
    return salir

if (buscarSalida(matrix, 0, 0)): mostrar(matrix)
else: print("No se encontró salida desde ahí")



