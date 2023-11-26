# cascade-model-training
 Huấn luyện mô hình phát hiện mặt người bằng phương pháp haar cascade classifier
 - Nguồn ảnh negative: https://github.com/handaga/tutorial-haartraining/tree/master/data/negatives
 - Nguồn ảnh postive: lấy 100 file ảnh bất kì từ https://www.kaggle.com/datasets/hereisburak/pins-face-recognition
 - Bài dựa theo tutorial opencv: https://docs.opencv.org/4.x/dc/d88/tutorial_traincascade.html
 - Số lần huấn luyện: 20 lần
   - Lần huấn luyện lần 20: mất 3 tiếng
 - Chảy thử model trên tập 17,534 ảnh phía trên
   - Tìm ra được khuôn mặt: 277
   - Precision: 1,579787841 %
