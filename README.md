# gcc_architectures

This repository contains lists of compiler flags used by the GCC 13 compiler suite when a certain CPU architecture is set via the `-march=` command-line option. Based on the given CPU architecture certain compiler flags will be set internally.

## [`./architectures/`](./architectures)

A list of supported CPU architectures in combination with `-march=...` is given [here](https://gcc.gnu.org/onlinedocs/gcc/x86-Options.html). The corresponding GCC compiler flags for the 64-bit targets can be found in [`./architectures/`](./architectures). The program `diff` is helpful to find changes between architectures, e.g. to find differences in compiler flags between `-march=x86-64` and `-march=x86-64-v2` (`diff -u x86-64.txt x86-64-v2.txt | grep '^[+-]' | tail -n+3`).

### `x86-64-v2` vs `x86-64`:

```
+  -mcrc32                              [enabled]
+  -mcx16                               [enabled]
-  -mno-sse4                            [enabled]
+  -mmwait                              [enabled]
+  -mpopcnt                             [enabled]
+  -msahf                               [enabled]
+  -msse3                               [enabled]
+  -msse4                               [enabled]
+  -msse4.1                             [enabled]
+  -msse4.2                             [enabled]
+  -mssse3                              [enabled]
```

### `x86-64-v3` vs `x86-64-v2`:

```
+  -mavx                                [enabled]
+  -mavx2                               [enabled]
+  -mbmi                                [enabled]
+  -mbmi2                               [enabled]
+  -mf16c                               [enabled]
+  -mfma                                [enabled]
+  -mlzcnt                              [enabled]
+  -mmovbe                              [enabled]
+  -mxsave                              [enabled]
```

### `x86-64-v4` vs `x86-64-v3`:

```
+  -mavx512bw                           [enabled]
+  -mavx512cd                           [enabled]
+  -mavx512dq                           [enabled]
+  -mavx512f                            [enabled]
+  -mavx512vl                           [enabled]
```

## [`./optlevel/`](./optlevel)

Different optimization levels can be set by the `-O` flag in GCC: `-O0`, `-O1`, `-O2`, `-O3`, `-Og`, `-Os`, `-Ofast`. This will internally set certain compiler flags for certain optimization techniques. The different optimization flags are explained in the [documentation](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html). 


### `-O3` vs `-O2`:
```
+  -fgcse-after-reload                  [enabled]
+  -fipa-cp-clone                       [enabled]
+  -floop-interchange                   [enabled]
+  -floop-unroll-and-jam                [enabled]
+  -fpeel-loops                         [enabled]
+  -fpredictive-commoning               [enabled]
+  -fsplit-loops                        [enabled]
+  -fsplit-paths                        [enabled]
+  -ftree-loop-distribution             [enabled]
+  -ftree-partial-pre                   [enabled]
+  -funroll-completely-grow-size        [enabled]
+  -funswitch-loops                     [enabled]
+  -fversion-loops-for-strides          [enabled]
```

### `-Ofast` vs `-O3`:
```
+  -fallow-store-data-races             [enabled]
+  -fassociative-math                   [enabled]
+  -fcx-limited-range                   [enabled]
+  -ffinite-math-only                   [enabled]
-  -fmath-errno                         [enabled]
+  -freciprocal-math                    [enabled]
-  -fsemantic-interposition             [enabled]
-  -fsigned-zeros                       [enabled]
-  -ftrapping-math                      [enabled]
+  -funsafe-math-optimizations          [enabled]
```

### `-O2` vs `-Os`:
```
+  -falign-functions                    [enabled]
+  -falign-jumps                        [enabled]
+  -falign-labels                       [enabled]
+  -falign-loops                        [enabled]
+  -foptimize-strlen                    [enabled]
+  -ftree-loop-vectorize                [enabled]
+  -ftree-slp-vectorize                 [enabled]
+  -funroll-loops                       [enabled]
```

### `-O2` vs `-O1`:
```
+  -falign-functions                    [enabled]
+  -falign-jumps                        [enabled]
+  -falign-labels                       [enabled]
+  -falign-loops                        [enabled]
+  -fcaller-saves                       [enabled]
+  -fcode-hoisting                      [enabled]
+  -fcrossjumping                       [enabled]
+  -fcse-follow-jumps                   [enabled]
+  -fdevirtualize                       [enabled]
+  -fdevirtualize-speculatively                 [enabled]
+  -fexpensive-optimizations            [enabled]
+  -fgcse                               [enabled]
+  -fhoist-adjacent-loads               [enabled]
+  -findirect-inlining                  [enabled]
+  -finline-functions                   [enabled]
+  -finline-small-functions             [enabled]
+  -fipa-bit-cp                         [enabled]
+  -fipa-cp                             [enabled]
+  -fipa-icf                            [enabled]
+  -fipa-icf-functions                  [enabled]
+  -fipa-icf-variables                  [enabled]
+  -fipa-ra                             [enabled]
+  -fipa-sra                            [enabled]
+  -fipa-vrp                            [enabled]
+  -fisolate-erroneous-paths-dereference        [enabled]
+  -flra-remat                          [enabled]
+  -foptimize-sibling-calls             [enabled]
+  -foptimize-strlen                    [enabled]
+  -fpartial-inlining                   [enabled]
+  -fpeephole2                          [enabled]
+  -free                                [enabled]
+  -freorder-blocks-and-partition       [enabled]
+  -freorder-functions                  [enabled]
+  -frerun-cse-after-loop               [enabled]
+  -fschedule-insns2                    [enabled]
+  -fstore-merging                      [enabled]
+  -fstrict-aliasing                    [enabled]
+  -ftree-loop-distribute-patterns      [enabled]
+  -ftree-loop-vectorize                [enabled]
+  -ftree-pre                           [enabled]
+  -ftree-slp-vectorize                 [enabled]
+  -ftree-switch-conversion             [enabled]
+  -ftree-tail-merge                    [enabled]
+  -ftree-vrp                           [enabled]
+  -funroll-loops                       [enabled]
```

### `-O1` vs `-O0`:
```
+  -fbranch-count-reg                   [enabled]
+  -fcombine-stack-adjustments          [enabled]
+  -fcompare-elim                       [enabled]
+  -fcprop-registers                    [enabled]
+  -fdefer-pop                          [enabled]
+  -fdse                                [enabled]
+  -fforward-propagate                  [enabled]
+  -fguess-branch-probability           [enabled]
+  -fif-conversion                      [enabled]
+  -fif-conversion2                     [enabled]
+  -finline                             [enabled]
+  -finline-functions-called-once       [enabled]
+  -fipa-modref                         [enabled]
+  -fipa-profile                        [enabled]
+  -fipa-pure-const                     [enabled]
+  -fipa-reference                      [enabled]
+  -fipa-reference-addressable          [enabled]
+  -fmove-loop-invariants               [enabled]
+  -fmove-loop-stores                   [enabled]
+  -fomit-frame-pointer                 [enabled]
+  -freorder-blocks                     [enabled]
+  -fshrink-wrap                        [enabled]
+  -fsplit-wide-types                   [enabled]
+  -fssa-phiopt                         [enabled]
+  -fthread-jumps                       [enabled]
+  -ftoplevel-reorder                   [enabled]
+  -ftree-bit-ccp                       [enabled]
+  -ftree-builtin-call-dce              [enabled]
+  -ftree-ccp                           [enabled]
+  -ftree-ch                            [enabled]
+  -ftree-coalesce-vars                 [enabled]
+  -ftree-copy-prop                     [enabled]
+  -ftree-dce                           [enabled]
+  -ftree-dominator-opts                [enabled]
+  -ftree-dse                           [enabled]
+  -ftree-fre                           [enabled]
+  -ftree-pta                           [enabled]
-  -funreachable-traps                  [enabled]
+  -ftree-sink                          [enabled]
+  -ftree-slsr                          [enabled]
+  -ftree-sra                           [enabled]
+  -ftree-ter                           [enabled]
```
