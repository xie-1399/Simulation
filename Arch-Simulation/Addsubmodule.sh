#!/bin/bash
nemuPath="https://github.com/NJU-ProjectN/nemu.git"
abstractmachinePath="https://github.com/NJU-ProjectN/abstract-machine.git"
fceusamPath="https://github.com/NJU-ProjectN/fceux-am.git"
amkernelPath="https://github.com/NJU-ProjectN/am-kernels.git"
nanoslitePath="https://github.com/NJU-ProjectN/nanos-lite.git"
navyappsPath="https://github.com/NJU-ProjectN/navy-apps.git"
modulelists=(${nemuPath} ${abstractmachinePath} ${fceusamPath} ${amkernelPath} ${nanoslitePath} ${navyappsPath})

echo "clone some module"

for i in ${modulelists[@]}
do
    git clone --recursive ${i}
done

echo "Finish"
