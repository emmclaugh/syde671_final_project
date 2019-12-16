% generate list of all images
cd("C:\Users\npellegr\Documents\data_odometry_color\dataset\sequences\09\image_2\")
mask_folder = sprintf("%s\\masks_",cd);
if ~exist(mask_folder,'dir')
    mkdir(mask_folder); 
end
imageList = dir('*.png');

move_list = [0:64,489:530,935:967,1057:1505];
im_dim = size(imread(imageList(1).name));

% for image in list
for im_num = 1:length(imageList)
    %open image
    filename = imageList(im_num).name;
    image = imread(filename);
    %generate base mask
    mask = zeros(im_dim(1),im_dim(2));
    
    %if no moving object move to next
    file_number = str2num(filename(1:(end-4)));
    if(~ismember(file_number,move_list))
        % save mask image
        imwrite (mask, sprintf("%s\\mask_%06d.png", mask_folder, file_number));
        continue;
    end
    
    %display and sample 
    fig = figure; imshow(image);
    fprintf("file number %d\n", file_number);
    disp("Select bounding rectangle"); pts = round(getrect(fig));
    %disp("Select top left point"); [x1,y1] = getpts(fig);
    %disp("Select bottom right point"); [x2,y2] = getpts(fig);
    close(fig)

    if(pts(3:4) == [0,0]) %should not run into this case
        % save mask image
        imwrite (mask, sprintf("%s\\mask_%06d.png", mask_folder, file_number));
        continue;
    end
    
    % compute bottom right corner
    pts(3) = pts(1)+pts(3);
    pts(4) = pts(2)+pts(4);
    % ensure corners are within bounds of image
    pts(1) = min(max(pts(1),1),im_dim(2));
    pts(3) = min(max(pts(3),1),im_dim(2));
    pts(2) = min(max(pts(2),1),im_dim(1));
    pts(4) = min(max(pts(4),1),im_dim(1));
    % mask based on bounded selection
    mask(pts(2):pts(4),pts(1):pts(3)) = 1;
    
    % save mask image
    imwrite (mask, sprintf("%s\\mask_%06d.png", mask_folder, file_number));
end