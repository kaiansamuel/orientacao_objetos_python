class TV:
    def __init__(self):
        self.cor = 'preta'
        self.ligado = False
        self.tamamnho = 55
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

tv_sala = TV()
tv_quarto = TV()

tv_sala.cor = 'Branca'


print(tv_sala.cor)
print(tv_quarto.cor)

tv_quarto.tamamnho = 30
print(tv_sala.tamamnho)
print(tv_quarto.tamamnho)
print(self.mudar_canal('Amazon Prime'))

