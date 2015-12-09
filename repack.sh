#!/bin/bash
#
# Little script to helps me to create a new version
# of a check_mk plugin.
#


if [ $# -lt 1 ]; then
  echo "The package filename is mandatory"
  exit 1
fi

old="$(pwd)"
pkt="${1}"
pktname="$(echo ${pkt} | cut -f1 -d\-)"
tmp="$(mktemp -d ./.XXXXX)"
cp ${pkt} ${tmp}/${pkt}.tar.gz
cd ${tmp}
tar zxf ${pkt}.tar.gz
rm ${pkt}.tar.gz
for f in $(ls -1 *.tar); do
  dname="$(echo ${f} | cut -f1 -d\.)"
  mkdir ${dname}
  tar xf ${f} -C ${dname}
  rm ${f}
  find ${dname} -type f | egrep -v '(info)' | while read f; do
    cp -a ${old}/${f} ${f}
  done
  cd ${dname}
  tar cf ../${f} *
  cd ..
  rm -rf ${dname}
done
version=$(grep "'version':" info | cut -f4 -d\')
newversion=$(echo ${version} + 0.1 | bc)
sed "s/'version': .*/'version': '${newversion}',/g" info > info_new
mv info_new info
tar zcf ../${pktname}-${newversion}.mkp *

cd ${old}
rm -rf ${tmp}
exit 0
