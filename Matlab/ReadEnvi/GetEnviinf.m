function [imageda,samples,bands,lines]=GetEnviinf(fn,fn2)
% Designed by Elson Chen
% Get basic information of Envi data
% [imageda,samples,bands,lines]=GetEnviinf(fn,fn2)
% fn:光谱数据头文件名称 eg:'1.hdr'
% fn2：光谱数据文件名
% imageda:光谱数据, samples by lines by bands
% samples
% bands
% lines

%% 获得samples、bands、lines
fid = fopen(fn,'r');
R = [];
while ~feof(fid)
    tl = fgetl(fid);
    id = findstr(tl,'samples');%If does not find the str then return 0
    if ~isempty(id)
        eval(tl)%执行tl中的数据
        %         break
    end
    id = findstr(tl,'lines');%If does not find the str then return 0
    if ~isempty(id)
        eval(tl)%执行tl中的数据
        %         break
    end
    id = findstr(tl,'bands');%If does not find the str then return 0
    if ~isempty(id)
        eval(tl)%执行tl中的数据
        break
    end
    %         id = findstr(tl,'data type');%If does not find the str then return 0
    %     if ~isempty(id)
    %         datatype=str2num(tl(isstrprop(tl,'digit')));
    %         break
    %     end;
end;
%% 获得envi存储的数据类型
while ~feof(fid)
    tl = fgetl(fid);
    id = findstr(tl,'data type');%If does not find the str then return 0
    if ~isempty(id)
        datatype=str2num(tl(isstrprop(tl,'digit')));
        break
    end;
end

d={'bit8' 'int16' 'int32' 'float32' 'float64' 'uint16' 'uint32' 'int64' 'uint64'};

switch datatype
    case 1
        t=d(1);
    case 2
        t=d(2);
    case 3
        t=d(3);
    case 4
        t=d(4);
    case 5
        t=d(5);
    case 12
        t=d(6);
    case 13
        t=d(7);
    case 14
        t=d(8);
    case 15
        t=d(9);
    otherwise
        error('Unknown image data type');
end
data_type=char(t)

%% 获得光谱数据
f=fopen(fn2);
a=fread(f,data_type);%使用fread写的时候要注意顺序
imageda = reshape(a,samples,bands,lines);%%
%注意:不同仪器的这个顺序可能不同。这个顺序,samples和lines的顺序尚不清楚，bands一定在前
imageda=permute(imageda,[1 3 2]);
fclose('all')
clc
end