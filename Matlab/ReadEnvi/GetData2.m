% Elson
%Need getrawdata,getrawdata2
clc
clear
close all
f='leaf';
str=".hdr";%头文件的后缀
str2=".raw";%Envi原始文件的后缀
fn =insertBefore(str,".",f);
fn2 =insertBefore(str2,".",f);
[Spectradata,samples,bands,lines]=GetEnviinf(fn,fn2);
clearvars -EXCEPT lines samples bands Spectradata

%%
imshow(Spectradata(:,:,100))
save testdata.mat Spectradata bands