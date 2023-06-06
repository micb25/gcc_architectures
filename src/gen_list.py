#!/usr/bin/env python3

import os

# supported 64-bit GCC architectures
archs = "nocona core2 nehalem corei7 westmere sandybridge corei7-avx ivybridge core-avx-i haswell core-avx2 broadwell skylake skylake-avx512 cannonlake icelake-client rocketlake icelake-server cascadelake tigerlake cooperlake sapphirerapids emeraldrapids alderlake raptorlake meteorlake graniterapids bonnell atom silvermont slm goldmont goldmont-plus tremont sierraforest grandridge knl knm x86-64 x86-64-v2 x86-64-v3 x86-64-v4 eden-x2 nano nano-1000 nano-2000 nano-3000 nano-x2 eden-x4 nano-x4 lujiazui k8 k8-sse3 opteron opteron-sse3 athlon64 athlon64-sse3 athlon-fx amdfam10 barcelona bdver1 bdver2 bdver3 bdver4 znver1 znver2 znver3 znver4 btver1 btver2".split()

for arch in archs:
    print(arch)
    os.system('LANG=C gcc -Q -march={} --help=target | grep enabled > ../architectures/{}.txt'.format(arch, arch))

for optlevel in "O1 O2 O3 Os Og".split():
    print(optlevel)
    os.system('LANG=C gcc -Q -{} --help=optimizers | grep enabled > ../optlevel/{}.txt'.format(optlevel, optlevel))

