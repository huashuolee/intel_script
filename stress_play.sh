#!/bin/bash
adb devices
echo "input device number: "
read devices
for(( n=1 ; ;n++ ));do
    echo $n
    adb -s $devices shell am start -a android.intent.action.VIEW -d file:///sdcard/kauai_1080p_MPEG4_AVC_H.264_AAC_new.mp4 -t video/* 
    sleep 340
    adb -s $devices shell input keyevent 4
    adb -s $devices shell input keyevent 4
    adb -s $devices shell input keyevent 4
done
