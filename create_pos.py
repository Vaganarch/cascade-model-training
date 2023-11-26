import os, random
import shutil

for i in range(0, 100):
    file_path = random.choice(os.listdir("D:/opencv_training/classes_pins_dataset"))
    path_1 = "D:/opencv_training/classes_pins_dataset/" + file_path
    path_2 = "D:/opencv_training/pos"
    shutil.copy(path_1, path_2)
    print(file_path)
    #temp = open(temp, "w")
    #temp.write()
    #temp.close()