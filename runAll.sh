#!/bin/bash

rm bin/*
rm html/applets/*
javac -d bin/ -target 1.7 -source 1.7 src/*
cp bin/* html/applets/

echo "Applets updated"
