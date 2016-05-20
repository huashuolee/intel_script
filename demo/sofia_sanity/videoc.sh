#!/bin/bash

for ((i=0; i<50; i++));
do
   echo -n $i ' ' 
   adb shell input keyevent 27
   sleep 3
   adb shell input keyevent 27
   sleep 10 
done

