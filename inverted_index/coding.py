import math 

from abc import ABC, abstractmethod

class NumberRepr(ABC):
    @abstractmethod
    def Unary(x): 
        """
        Инвертированное унарное представление числа
        """
        return (x-1)*'0'+'1'

    @abstractmethod
    def Binary(x, l = 1): 
        """
        Бинарное представление числа
        """
        s = '{0:0%db}' % l 
        return s.format(x) 

    @abstractmethod
    def binary_without_msb(x):
        """
        Бинарное представление числа без старшего бита
        """
        binary = "{0:b}".format(int(x))
        binary_without_MSB = binary[1:]
        return binary_without_MSB


class EliasCoding(ABC):
    @abstractmethod
    def elias_gamma_encode(x): 
        """
        Гамма-кодирование Элиаса для отдельного числа
        """
        if x == 0 or x == 1:  
            return str(x)
        log2 = lambda x: math.log(x, 2) 
        n = 1 + int(log2(x)) 
        l = int(log2(x)) 
        b = x - 2**l
        return NumberRepr.Unary(n) + NumberRepr.Binary(b, l) 


    @abstractmethod
    def elias_gamma_decode(x): 
        """
        Гамма-декодирование Элиаса для отдельного числа
        """
        x = list(x) 
        K = 0
        while True: 
            if not x[K] == '0': 
                break
            K = K + 1
        x = x[K:2*K+1] 
        n = 0
        x.reverse() 
        for i in range(len(x)): 
            if x[i] == '1': 
                n = n+math.pow(2, i) 
        return int(n) 

    @abstractmethod
    def elias_delta_encode(k):
        """
        Дельта-кодирование Элиаса для отдельного числа
        """
        if k == 1:
            return str(k)
        Gamma = EliasCoding.elias_gamma_encode(1 + math.floor(math.log(k, 2)))
        binary_without_MSB = NumberRepr.binary_without_msb(k)
        return Gamma+binary_without_MSB

    @abstractmethod
    def elias_delta_decode(x): 
        """
        Дельта-декодирование Элиаса для отдельного числа
        """
        x = list(x) 
        L=0
        while True: 
            if not x[L] == '0': 
                break
            L= L + 1

        x=x[2*L+1:]  
        x.insert(0,'1')  
        x.reverse() 
        n=0
        for i in range(len(x)):  
            if x[i]=='1': 
                n=n+math.pow(2,i) 
        return int(n) 


    def decode_gamma_string(encoded_posting_list: str):
        """
        Декодирование гамма кода Элиаса для строки, содержащей несколько чисел 
        """
        decoded_posting_list = []
        while encoded_posting_list != '':
            length = encoded_posting_list.index('1') + 1
            if length > 1:
                length = 2*length-1
                current_encoded_number = encoded_posting_list[:length]
                encoded_posting_list = encoded_posting_list[length:]
            else:
                current_encoded_number = encoded_posting_list[0]
                encoded_posting_list = encoded_posting_list[1:]

            decoded_posting_list.append(EliasCoding.elias_gamma_decode(current_encoded_number))
        return decoded_posting_list


    def decode_delta_string(encoded_posting_list: str):
        """
        Декодирование дельта кода Элиаса для строки, содержащей несколько чисел 
        """
        decoded_posting_list = []
        while encoded_posting_list != '':
            m = encoded_posting_list.index('1')
            if m > 0:
                l_part = encoded_posting_list[m+1:2*m+1]
                l = 2**m + int(l_part, 2)
                k = l-1
                index = 2*m+1 + k
                current_encoded_number = encoded_posting_list[:index]
                encoded_posting_list = encoded_posting_list[index:]  
            else:
                current_encoded_number = encoded_posting_list[0]
                encoded_posting_list = encoded_posting_list[1:]                  

            decoded_posting_list.append(EliasCoding.elias_delta_decode(current_encoded_number))
        return decoded_posting_list








