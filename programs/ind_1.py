#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def outer(type = "max"):
    '''
    Внешняя функция
    '''
    def inner(lst):
        '''
        Внутренняя функция
        '''
        if type == "max":
            return max(lst)
        
        else:
            return min(lst)
        
    return inner


if __name__ == "__main__":
    print(outer("max")([1,2,3,5,7,10]))
    print(outer("min")([1,2,3,5,7,10]))
    print(outer()([1,2,3,5,7,10]))