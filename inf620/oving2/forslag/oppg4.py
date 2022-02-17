#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
INF620, Øving 2, oppgave 4
@author: Knut Anders Stokke
'''

# 4.a
print('Oppgi to heltall:')
x = int(input())
y = int(input())
utskrifts_format = '%-15s%d'
print(utskrifts_format % ('Sum:', x + y))
print(utskrifts_format % ('Differanse:', x - y))
print(utskrifts_format % ('Produkt:', x * y))
print('%-15s%.2f' % ('Gjennomsnitt:', (x + y)/2))
print(utskrifts_format % ('Distanse:', abs(x - y)))
print(utskrifts_format % ('Maksimum:', max(x, y)))
print(utskrifts_format % ('Minimum:', min(x, y)))

