#!/usr/bin/gnuplot -persist
# 
# call with gnuplot -e "output_file='nome.png'" -e "data_file='nome'"  plot.gp
# plot the data contained in the datafile into a png image

set term pngcairo dashed size 1024,1024
#set terminal png
set output output_file

set logscale yx

#set yrange [:]
#set xrange [*:]
set xlabel "pagerank"
set ylabel "frequenza"

#set linetype 1 dt 1
#set linetype 2 dt 2
#set linetype 3 dt 3
#set linetype 4 dt 4
set style line 1 lt 7 lc 1 ps 1
set style line 2 lt 2 lc 2 lw 1 pt 2
set style line 3 lt 3 lc 3 lw 1 pt 3
set style line 4 lt 4 lc 4 lw 1 pt 4

plot data_file using 1:2 title 'pagerank' with points ls 1,\
#	 data_file using 1:3 title 'merge' with lines ls 2,\
#	 data_file using 1:4 title 'death' with lines ls 3,\
#	 data_file using 1:5 title 'birth' with lines ls 4
#	 data_file using 1:6 title 'min validation error' with lines ls 4,\
#	 data_file using 1:7 title 'max validation error' with lines ls 4
