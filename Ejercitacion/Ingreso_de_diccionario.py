def input_dictionaty ():
    paso = {}
    continue_add = True
    while continue_add :
        partido = str(input("ingrese un partido politico :"))
        if  partido != "" :
            votos_p = int(input("Ingrese los votos validos del partido politico :"))
            votos_in = int(input("Ingrese los votos invalido del partido politico :"))
            if not partido in paso :
                paso[partido] = [votos_p, votos_in]
            else:
                paso[partido][0] += votos_p
                paso[partido][1] += votos_in
        else :
            continue_add = False
    return paso

def ganador_vot(paso) :
    partido_gana = ""
    votos_gana = -1
    for partido in paso :
        if paso[partido][0] > votos_gana :
            partido_gana = partido
            votos_gana = paso[partido][0]
    return partido_gana, votos_gana

def pasaro_paso(paso) :
    votos_tot = 0
    vot_min = 0
    for partido in paso :
        votos_tot += paso[partido][0]
        vot_min = votos_tot *0.1
    return vot_min

def filtro(paso, vot_min) :   
    pasan = ()
    no_pasan = () 
    for partido in paso :
        if paso[partido][0] > vot_min :
            pasan += partido
        else :
            no_pasan += partido
    return pasan, no_pasan

def ranking_vot_inv(paso) :
    ranking = sorted(paso.items()( key = lambda tupla_vot : tupla_vot[1][1]), reverse = True)
    return ranking
