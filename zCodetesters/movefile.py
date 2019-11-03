import os, shutil
path =os.path.join(os.path.dirname(os.path.abspath(__file__)),"testFolder","tesp.csv")
print("path:",path)
path2 =os.path.join(os.path.dirname(os.path.abspath(__file__)),"tesp.csv")
print("path2:",path2)
shutil.copyfile(path,path2)
