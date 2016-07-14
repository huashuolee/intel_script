#! /bin/bash


export pkgnum=`wc ./list |awk 'NR== 1 {print $1}'`

for((n=1; n < pkgnum; n++)) ; do
echo $n
echo "=========================================="
export pkg=`cat ./list | awk 'NR=='$n' {print $1}'`
python pytest.py -c ../test_repo/case_profile/$pkg
echo "Press any key to contine ..."
read pause
done
