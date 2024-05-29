#!/usr/bin/env python3

import time
import utils

time.sleep(2)
for i in range(10):
    utils.print_now("INICIAR_PROCESO loop.txt")
    time.sleep(0.2)
utils.print_now("INICIAR_PROCESO loop.txt") # pid=10
utils.print_now("PROCESO_ESTADO")
time.sleep(0.2)
utils.print_now("FINALIZAR_PROCESO 10")
time.sleep(0.2)
utils.print_now("PROCESO_ESTADO")
time.sleep(3600)
