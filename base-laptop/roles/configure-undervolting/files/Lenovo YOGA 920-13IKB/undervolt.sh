#!/bin/bash

# Adjusting the CPU Core to a -110mV undervolt
wrmsr 0x150 0x80000011F1E00000

# Adjusting the iGPU to a -120mV undervolt
wrmsr 0x150 0x80000111F0A00000

#Adjusting the CPU cache to a -110mV undervolt
wrmsr 0x150 0x80000211F1E00000
