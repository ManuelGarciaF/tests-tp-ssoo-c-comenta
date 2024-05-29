#!/usr/bin/env python3

import time
import sys

def print_now(str):
    print(str)
    sys.stdout.flush()

time.sleep(2)
print_now("INICIAR_PROCESO io.txt")
time.sleep(8)
print_now("PROCESO_ESTADO")
time.sleep(1)
print_now("FINALIZAR_PROCESO 0")
time.sleep(1)
print_now("PROCESO_ESTADO")
time.sleep(3600)
