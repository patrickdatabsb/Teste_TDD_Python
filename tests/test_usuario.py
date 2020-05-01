from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture()
def henrique():
    return Usuario('Henrique', 100.0)


@pytest.fixture()
def leilao():
    return Leilao("Carro")


def test_deve_subitrair_valor_da_carteira_do_usuario_quando_ele_propor_um_lance(henrique,leilao):
    henrique.propoe_lance(leilao, 50.0)

    assert henrique.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_valor_carteira(henrique, leilao):
    henrique.propoe_lance(leilao, 1.0)

    assert henrique.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_e_igual_que_valor_carteira(henrique,leilao):
    henrique.propoe_lance(leilao, 100.0)

    assert henrique.carteira == 0.0


def test_nao_deve_permitir_propor_lance_quando_o_valor_e_maior_que_valor_carteira(henrique,leilao):
    with pytest.raises(LanceInvalido):
        henrique.propoe_lance(leilao, 200.0)
