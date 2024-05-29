#!/usr/bin/env python3

import time
import utils

time.sleep(2)
utils.print_now("INICIAR_PROCESO loop.txt") # pid=0
time.sleep(0.2)
utils.print_now("INICIAR_PROCESO loop.txt") # pid=1
time.sleep(0.2)
utils.print_now("INICIAR_PROCESO loop.txt") # pid=2
time.sleep(0.2)
utils.print_now("PROCESO_ESTADO")
time.sleep(0.2)
utils.print_now("FINALIZAR_PROCESO 2")
time.sleep(0.2)
utils.print_now("PROCESO_ESTADO")
time.sleep(3600)
