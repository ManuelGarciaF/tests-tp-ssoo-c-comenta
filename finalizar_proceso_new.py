#!/usr/bin/env python3

import time
import sys

def print_now(str):
    print(str)
    sys.stdout.flush()

time.sleep(2)
for i in range(10):
    print_now("INICIAR_PROCESO loop.txt")
    time.sleep(1)
print_now("INICIAR_PROCESO loop.txt") # pid=10
print_now("PROCESO_ESTADO")
time.sleep(1)
print_now("FINALIZAR_PROCESO 10")
time.sleep(1)
print_now("PROCESO_ESTADO")
time.sleep(3600)
