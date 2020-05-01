from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

esio = Usuario("Esio")
gustavo = Usuario("Gustavo")

lance_do_gustavo = Lance(gustavo, 150.0)
lance_do_esio = Lance(esio, 100.0)



leilao = Leilao("Carro")

leilao.lances.append(lance_do_gustavo)
leilao.lances.append(lance_do_esio)


for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor} .')


avaliador = Avaliador()

avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')