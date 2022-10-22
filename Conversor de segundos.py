Segundos = input('Por favor, entre com o número de segundos que deseja converter: ')
Segundos_1 = int(Segundos)
Dias = Segundos_1 // 86400
DiasRestos = Segundos_1 % 86400
Horas = DiasRestos// 3600
HorasRestos = Horas % 3600
Minutos = HorasRestos / 60
MinutosRestos = Minutos % 60
Segundos_2 = MinutosRestos 

print(Dias, "dias, ", Horas, "horas e", Minutos, "minutos e ", Segundos_2,"segundos.")
