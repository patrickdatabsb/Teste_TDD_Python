from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.esio = Usuario("Esio",500.0)
        self.gustavo = Usuario("Gustavo", 500.0)

        self.lance_do_esio = Lance(self.esio, 100.0)
        self.lance_do_gustavo = Lance(self.gustavo, 150.0)

        self.leilao = Leilao("Carro")

    # test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_esio)
        self.leilao.propoe(self.lance_do_gustavo)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gustavo)
            self.leilao.propoe(self.lance_do_esio)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gustavo)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_tres_lance(self):
        vini = Usuario('Vini',500.0)

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_esio)
        self.leilao.propoe(self.lance_do_gustavo)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o leilao não tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_esio)

        quantidade_lances_recebido = len(self.leilao.lances)

        self.assertEqual(1, quantidade_lances_recebido)

    # se o ultimo usuario for diferente, deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_ultimo_usuario_seja_diferente(self):
        vini = Usuario('Vini',500.0)

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_esio)
        self.leilao.propoe(lance_do_vini)

        quantidade_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_lances_recebido)

    # se o ultimo usuario for o mesmo, não deve permitir propor o lance

    def test_nao_deve_permitir_propor_um_lance_caso_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_do_esio)

        with self.assertRaises(LanceInvalido):
            lance_do_esio2 = Lance(self.esio, 200.0)
            self.leilao.propoe(lance_do_esio2)





