from coding import NumberRepr, EliasCoding
from preprocessing import Tokenization

#############################Тесты по унарному представлению числа###################################
def test_unary1():

    assert NumberRepr.Unary(1) == '1'

def test_unary2():

    assert NumberRepr.Unary(6) == '000001'

def test_unary3():

    assert NumberRepr.Unary(13) == '0000000000001'

def test_unary4():

    assert NumberRepr.Unary(958) == '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'

def test_unary5():

    assert NumberRepr.Unary(3) == '001'

#############################Тесты по бинарному кодированию###################################
def test_binary1():
    assert NumberRepr.Binary(3) == bin(3)[2:]

def test_binary2():
    assert NumberRepr.Binary(100) == bin(100)[2:]

def test_binary3():
    assert NumberRepr.Binary(9272429834789) == bin(9272429834789)[2:]

def test_binary4():
    assert NumberRepr.Binary(0) == bin(0)[2:]

def test_binary5():
    assert NumberRepr.Binary(16) == bin(16)[2:]


#############################Тесты по бинарному кодированию без старшего бита###################################
def test_binary_without_msb1():
    assert NumberRepr.binary_without_msb(3) == bin(3)[3:]

def test_test_binary_without_msb2():
    assert NumberRepr.binary_without_msb(100) == bin(100)[3:]

def test_test_binary_without_msb3():
    assert NumberRepr.binary_without_msb(9272429834789) == bin(9272429834789)[3:]

def test_test_binary_without_msb4():
    assert NumberRepr.binary_without_msb(0) == bin(0)[3:]

def test_test_binary_without_msb5():
    assert NumberRepr.binary_without_msb(16) == bin(16)[3:]

#############################Гамма кодирование Элиаса###################################
def test_gamma_encode1():
    assert EliasCoding.elias_gamma_encode(15) == '0001111'

def test_gamma_encode2():
    assert EliasCoding.elias_gamma_encode(100) == '0000001100100'

def test_gamma_encode3():
    assert EliasCoding.elias_gamma_encode(1251) == '000000000010011100011'

def test_gamma_encode4():
    assert EliasCoding.elias_gamma_encode(1) == '1'

def test_gamma_encode5():
    assert EliasCoding.elias_gamma_encode(839479875) == '00000000000000000000000000000110010000010010111001001000011'

#############################Гамма декодирование Элиаса###################################

def test_gamma_decode1():
    assert EliasCoding.elias_gamma_decode('0001111') == 15

def test_gamma_decode2():
    assert EliasCoding.elias_gamma_decode('0000001100100') == 100

def test_gamma_decode3():
    assert EliasCoding.elias_gamma_decode('000000000010011100011') == 1251

def test_gamma_decode4():
    assert EliasCoding.elias_gamma_decode('1') == 1

def test_gamma_decode5():
    assert EliasCoding.elias_gamma_decode('00000000000000000000000000000110010000010010111001001000011') == 839479875

#############################Дельта кодирование Элиаса###################################

def test_delta_encode1():
    assert EliasCoding.elias_delta_encode(14) == '00100110'

def test_delta_encode2():
    assert EliasCoding.elias_delta_encode(1) == '1'

def test_delta_encode3():
    assert EliasCoding.elias_delta_encode(100) == '00111100100'

def test_delta_encode4():
    assert EliasCoding.elias_delta_encode(1488) == '00010110111010000'

def test_delta_encode5():
    assert EliasCoding.elias_delta_encode(48954895485904389) == '000001110000101101111011000011011111010011011101000010011000000101'

#############################Дельта декодирование Элиаса###################################

def test_delta_decode1():
    assert EliasCoding.elias_delta_decode('00100110') == 14

def test_delta_decode2():
    assert EliasCoding.elias_delta_decode('1') == 1

def test_delta_decode3():
    assert EliasCoding.elias_delta_decode('00111100100') == 100

def test_delta_decode4():
    assert EliasCoding.elias_delta_decode('00010110111010000') == 1488

def test_delta_decode5():
    assert EliasCoding.elias_delta_decode('0000010011111000111111011011001000011110011101011') == 489548954859

#############################Тесты токенизатора текста###################################

def test_tokenization1():
    assert Tokenization.tokenize_text('я ты он она был') == []

def test_tokenization2():
    assert Tokenization.tokenize_text('') == []

def test_tokenization3():
    assert Tokenization.tokenize_text('абырвалг') == ['абырвалг']

def test_tokenization4():
    assert Tokenization.tokenize_text('Впрочем, я ни шиша не смыслю в моей болезни и не знаю наверно, что у меня болит.') == ['шиш', 'смысл', 'мо', 'болезн', 'зна', 'наверн', 'бол']

def test_tokenization5():
    assert Tokenization.tokenize_text('ю..бюбюб..б.юбю. дауж') == ['бюбюб', 'юб', 'дауж']