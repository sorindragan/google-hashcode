#!/bin/bash
rm *.out
javac *.java
java Solution "a_example.in" > a_example.out
java Solution "b_should_be_easy.in" > b_should_be_easy.out
java Solution "c_no_hurry.in" > c_no_hurry.out
java Solution "d_metropolis.in" > d_metropolis.out
java Solution "e_high_bonus.in" > e_high_bonus.out
zip hashCode.zip *.java
rm *.class
