#!/bin/bash
echo "Check out the Branch"

cd $PWD/nemu
git checkout -b Simulation origin/ics2022
cd ..

cd $PWD/abstract-machine 
git checkout -b Simulation origin/ics2022
cd ..

cd $PWD/fceux-am 
git checkout -b Simulation origin/ics2021
cd ..

cd $PWD/am-kernels
git checkout -b Simulation origin/ics2021
cd ..

cd $PWD/nanos-lite
git checkout -b Simulation origin/ics2021
cd ..

cd $PWD/navy-apps
git checkout -b Simulation origin/ics2021
cd ..

echo "check finish"
