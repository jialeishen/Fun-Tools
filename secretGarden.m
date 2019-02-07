%Paint secret garden with Matlab
%author:Jialei Shen
%e-mail:shenjialei1992@163.com
%latest:2016.07.31

clear
clc
I=imread('image.jpg');
J=im2bw(I,0.95);
[K,n]=bwlabel(J,8);
m=0.5+0.4*rand(n,3);  %random color range
RGB=label2rgb(K,m,'k');
figure,
imshow(RGB);
