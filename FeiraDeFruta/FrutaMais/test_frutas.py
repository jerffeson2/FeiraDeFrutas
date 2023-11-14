
import pytest
from frutas import FeiraDeFrutas


@pytest.fixture
def feira():
    return FeiraDeFrutas()


def test_adicionar_fruta(feira):
    feira.adicionar_fruta('Maçã', 10)
    estoque = feira.verificar_estoque()
    assert estoque == {'Maçã': 10}


def test_comprar_fruta_com_sucesso(feira):
    feira.adicionar_fruta('Banana', 15)
    feira.comprar_fruta('Banana', 5)
    estoque = feira.verificar_estoque()
    assert estoque == {'Banana': 10}


def test_comprar_fruta_sem_sucesso(feira):
    feira.adicionar_fruta('Pera', 8)
    feira.comprar_fruta('Pera', 10)
    estoque = feira.verificar_estoque()
    assert estoque == {'Pera': 8}


def test_comprar_fruta_inexistente(feira):
    feira.adicionar_fruta('Manga', 10)
    with pytest.raises(Exception):
        feira.comprar_fruta('Abacaxi', 5)


def test_verificar_estoque_inicial_vazio(feira):
    estoque = feira.verificar_estoque()
    assert estoque == {}


if __name__ == "__main__":
    pytest.main()
