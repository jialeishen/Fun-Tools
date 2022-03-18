%A bot completing coloring puzzles automatically. 
%author:Jialei Shen
%e-mail:jshen20@syr.edu
%latest:2016.07.31

clear
clc
I=imread('image.jpg'); %import a black and white coloring puzzle image
J=im2bw(I,0.95);
[K,n]=bwlabel(J,8);
m=0.5+0.4*rand(n,3);  %random color range
RGB=label2rgb(K,m,'k');
figure,
imshow(RGB);
