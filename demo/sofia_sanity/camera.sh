#!/bin/bash

for ((i=0; i<=50; i++));
do
   echo -n $i ' '
   adb shell input keyevent 23
   sleep 5 
done

