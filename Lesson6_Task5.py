# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:17:50 2021

@author: Iljam
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'


pen = Pen('Ручкой')
print(pen.draw())
pencil = Pencil('Карандашем')
print(pencil.draw())
handle = Handle('Маркером')
print(handle.draw())