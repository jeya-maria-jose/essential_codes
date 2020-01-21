close all
clear all
clc
listinfo = dir('./Brain_Ultrasound/');
m = length(listinfo);sz =[];
count = 0;
Images = zeros(512,512,1,325);Labels = Images;
idx = randperm(m-2);
for i =3:m
    I = imread(strcat('./Brain_Ultrasound/',listinfo(idx(i-2)+2).name));
    tmp = listinfo(i).name;
    tmp1 = split(tmp,'.');
    if i>1302
        imwrite(I,strcat('./Brain2_test/',num2str(count,'%04d'),'.png'));
        count =count+1;
    end
end
count=1;
Images = zeros(512,512,1,325);Labels = Images;
for i =3:327
    I = imread(strcat('./Brain_Ultrasound/',listinfo(idx(i-2)+2).name));
    tmp = listinfo(i).name;
    tmp1 = split(tmp,'.');
    if i<1303
        imwrite(I,strcat('./Brain2/',tmp1{1},'.png'));
    end
    sz = [sz;max(max(I))];
    Images(:,:,1,count) = I(:,1:512);
    tmp = double(I(:,513:end));tmp(tmp>150)=255.0;tmp(tmp<151)=0;
    Labels(:,:,1,count) = tmp;
    count = count+1;
end
save('-mat','-v7.3','Images2_m1.mat','Images')
save('-mat','-v7.3','Labels2_m1.mat','Labels')
size(Labels)
count=1;
Images = zeros(512,512,1,325);Labels = Images;
for i =328:652
    I = imread(strcat('./Brain_Ultrasound/',listinfo(idx(i-2)+2).name));
    tmp = listinfo(i).name;
    tmp1 = split(tmp,'.');
    if i<1303
        imwrite(I,strcat('./Brain2/',tmp1{1},'.png'));
    end
    sz = [sz;max(max(I))];
    Images(:,:,1,count) = I(:,1:512);
    tmp = double(I(:,513:end));tmp(tmp>150)=255.0;tmp(tmp<151)=0;
    Labels(:,:,1,count) = tmp;
    count = count+1;
end
save('-mat','-v7.3','Images2_m2.mat','Images')
save('-mat','-v7.3','Labels2_m2.mat','Labels')
size(Labels)
count = 1;
Images = zeros(512,512,1,325);Labels = Images;

for i =653:977
    I = imread(strcat('./Brain_Ultrasound/',listinfo(idx(i-2)+2).name));
    tmp = listinfo(i).name;
    tmp1 = split(tmp,'.');
    if i<1303
        imwrite(I,strcat('./Brain2/',tmp1{1},'.png'));
    end
    sz = [sz;max(max(I))];
    Images(:,:,1,count) = I(:,1:512);
    tmp = double(I(:,513:end));tmp(tmp>150)=255.0;tmp(tmp<151)=0;
    Labels(:,:,1,count) = tmp;
    count = count+1;
end
save('-mat','-v7.3','Images2_m3.mat','Images')
save('-mat','-v7.3','Labels2_m3.mat','Labels')
size(Labels)
Images = zeros(512,512,1,325);Labels = Images;
count = 1;
for i =978:1302
    I = imread(strcat('./Brain_Ultrasound/',listinfo(idx(i-2)+2).name));
    tmp = listinfo(i).name;
    tmp1 = split(tmp,'.');
    if i<1303
        imwrite(I,strcat('./Brain2/',tmp1{1},'.png'));
    end
    sz = [sz;max(max(I))];
    Images(:,:,1,count) = I(:,1:512);
    tmp = double(I(:,513:end));tmp(tmp>150)=255.0;tmp(tmp<151)=0;
    Labels(:,:,1,count) = tmp;
    count = count+1;
end
save('-mat','-v7.3','Images2_m4.mat','Images')
save('-mat','-v7.3','Labels2_m4.mat','Labels')
size(Labels)