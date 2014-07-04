#! /bin/bash


export pkgnum=`wc ./list |awk 'NR== 1 {print $1}'`

for((n=1; n < pkgnum; n++)) ; do
echo $n
export pkg=`cat ./list | awk 'NR=='$n' {print $1}'`
echo $pkg
export clip=`ls $pkg`
ffplay ${pkg}'/'${clip}
echo "-------------------------------------------"
done
