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
        Гамма-кодирование Элиаса 
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
        Гамма-декодирование Элиаса 
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
        Дельта-кодирование Элиаса
        """
        if k == 1:
            return str(k)
        Gamma = EliasCoding.elias_gamma_encode(1 + math.floor(math.log(k, 2)))
        binary_without_MSB = NumberRepr.binary_without_msb(k)
        return Gamma+binary_without_MSB

    @abstractmethod
    def elias_delta_decode(x): 
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








