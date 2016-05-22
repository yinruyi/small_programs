
for i=1:1514
    video_feature_temp = video_feature(:,:,:,i);
    voice_feature_temp = voice_feature(i,:,:);
    %combine video feature temp
    temp = video_feature_temp(:,:,1);
    for j=2:31
        temp = [temp;video_feature_temp(:,:,j)];
    end
    video_feature_temp = temp';%20*465result
    voice_feature_temp = squeeze(voice_feature_temp);
    voice_feature_temp = voice_feature_temp';%20*2result
    result_temp = ccaFuse(video_feature_temp,voice_feature_temp);%cca
    result_temp = result_temp';
    result_temp = [result_temp(1,:),result_temp(2,:)];%result
    result(i,:) = result_temp;
end
