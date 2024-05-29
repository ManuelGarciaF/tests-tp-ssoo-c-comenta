#!/usr/bin/env python3

import time
import utils

time.sleep(2)
utils.print_now("INICIAR_PROCESO io.txt")
time.sleep(8)
utils.print_now("PROCESO_ESTADO")
time.sleep(0.2)
utils.print_now("FINALIZAR_PROCESO 0")
time.sleep(1)
utils.print_now("PROCESO_ESTADO")
time.sleep(3600)
