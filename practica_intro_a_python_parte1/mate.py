def cantidad_agua_consumida(cant_personas):
  agua_necesaria = 30*cant_personas
  cant_termos = agua_necesaria/1000
  if cant_termos==1:
    return "se consumirĂ¡ " + str(cant_termos) + " termo"
  else:
    return "se consumirĂ¡n " + str(int(cant_termos+1)) + " termos"