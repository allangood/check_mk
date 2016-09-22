#!/bin/bash
#
# by Allan GooD
#

modname="$1"

dirs="agents checkman checks doc inventory notifications pnp-templates web"

basedir="$(pwd)"
for info in $(find ${modname} -name info); do
  pktdir="$(dirname ${info})"
  pktname="$(grep \'name\' ${info} | cut -f4 -d\')"
  pktversion="$(grep \'version\' ${info} | cut -f4 -d\')"
  echo "${pktname} - ${pktversion}"
  cd "${pktdir}"
  for dir in ${dirs}; do
    if [ -d "${dir}" ]; then
      cd "${dir}"
      tar cf ../${dir}.tar *
      cd ..
    fi
  done
  tar zcf "${pktname}-${pktversion}.mkp" info *.tar
  rm *.tar
  cd ${basedir}
done

exit 0
