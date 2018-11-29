import os
import time
def remove(file):
    # Inspection Center
    print('Inspection centre is under inspection.')
    time.sleep(0.5)
    if os.path.exists(file): # 如果文件存在
        # 删除文件，可使用以下两种方法。
        print('Check to',file)
        time.sleep(0.5)
        print('Processing.')
        time.sleep(0.5)
        os.remove(file) # 则删除
        time.sleep(0.5)
        print('Processing completed.')
        #os.unlink(my_file)
    else:
        print('no such file',file)
    return