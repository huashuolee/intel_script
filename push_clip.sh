#! /bin/bash

adb devices

ss=""
[[ -n $1 ]] && ss="-s $1"

export pkgnum=`wc ./$2 |awk 'NR== 1 {print $1}'`
adb $ss shell mkdir /sdcard/$2
for((n=1; n <= pkgnum; n++)) ; do
echo $n
export pkg=`cat ./$2 | awk 'NR=='$n' {print $1}'`
adb $ss push $pkg /sdcard/$2
echo "push clip"$pkg
sleep 2
done
adb $ss shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///mnt/sdcard/
