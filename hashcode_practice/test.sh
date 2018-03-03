#!/bin/bash
./run.py example.in
tac example.outref > example.out

./run.py small.in
tac small.outref > small.out

./run.py medium.in
tac medium.outref > medium.out

./run.py big.in
tac big.outref > big.out

rm *.outref
