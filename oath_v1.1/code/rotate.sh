#!/bin/bash

#-------------------------------------------------------------------------------
#Unless stated otherwise, all data in the OATH Dataset is licensed under a
#<a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons 4.0 
#Attribution License (CC BY 4.0)</a> and the accompanying source code is 
#licensed under a <a href="https://opensource.org/licenses/BSD-2-Clause">
#BSD-2-Clause License</a>.
#In particular, all actual image data included in the tarball are modified from 
#the <a href="https://www.nasa.gov/mission_pages/themis/spacecraft/asi.html">
#THEMIS all-sky imagers </a>.
#
#We thank H. Frey for giving us permission to include these data.
#Copyright for these data remains with NASA.
#
#We acknowledge NASA contract NAS5-02099 and V. Angelopoulos for use of data 
#from the THEMIS Mission. Specifically: S. Mende and E. Donovan for use of the
#ASI data, the CSA for logistical support in fielding and data retrieval from
#the GBO stations, and NSF for support of GIMNAST through grant AGS-1004736.
#-------------------------------------------------------------------------------

mkdir ../images/cropped_scaled_rotated
linecount=0
headerlength=19
while IFS="," read class2 class6 picNum label angle
do
  if [ "${linecount}" -lt "${headerlength}" ]
  then
    ((linecount++))
    continue
  fi
  infile="../images/cropped_scaled/${picNum}.png"
  outfile="../images/cropped_scaled_rotated/${picNum}_${angle}.png"
  convert ${infile} -background black -distort SRT ${angle} +repage ${outfile}
  ((linecount++))
done < "../classifications/classifications.csv"

exit 1
