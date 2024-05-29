#!/usr/bin/env python3

import time
import sys

def print_now(str):
    print(str)
    sys.stdout.flush()

time.sleep(2)
print_now("INICIAR_PROCESO loop.txt") # pid=0
time.sleep(1)
print_now("INICIAR_PROCESO loop.txt") # pid=1
time.sleep(1)
print_now("INICIAR_PROCESO loop.txt") # pid=2
time.sleep(1)
print_now("PROCESO_ESTADO")
time.sleep(1)
print_now("FINALIZAR_PROCESO 2")
time.sleep(1)
print_now("PROCESO_ESTADO")
time.sleep(3600)
