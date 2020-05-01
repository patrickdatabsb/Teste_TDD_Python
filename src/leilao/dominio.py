from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self,leilao,valor):
        if valor > self.__carteira:
            raise LanceInvalido('Não tem saldo suficiente na carteira')

        lance = Lance(self,valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    # def propoe_lance(self, leilao, valor):
    #     if not self._valor_eh_valido(valor):
    #         raise LanceInvalido('Não pode propor um lance com o valor maior que o valor da carteira')
    #
    #     lance = Lance(self, valor)
    #     leilao.propoe(lance)
    #
    #     self.__carteira -= valor


    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    # def _valor_eh_valido(self, valor):
    #     return valor <= self.__carteira



class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self.lance_valiado(lance):
            if not self.tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)


    @property
    def lances(self):
        return self.__lances[:]

    def tem_lances(self):
        return self.__lances

    def usuario_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        raise LanceInvalido('O mesmo usuário não pode dar dois lanças seguidos')

    def valor_maior_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance não pode ser maior que a carteira')


    def lance_valiado(self, lance):
        return not self.tem_lances() or self.usuario_diferentes(lance) and self.valor_maior_lance_anterior(lance)
