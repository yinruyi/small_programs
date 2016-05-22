%mel coefficient
clear;
clc;
close all;
addpath('H:\dev\small_programs\movie_music\voicebox\voicebox');
[S,FS,Nbits] = wavread('H:\dev\small_programs\movie_music\ffmpeg-0.5\ffmpeg-0.5\234.wav');

C=melcepst(S(1:1018,1),FS,12,20);
for i=1:1514
    voice_feature(i,:,:) = melcepst(S(1018*(i-1)+1:1018*i,1),FS,12,20);
end
    
    
