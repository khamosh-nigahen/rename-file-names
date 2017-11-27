import os

def rename_files():
    #list out all the file names
    print_files_name = os.listdir(r"/Users/puneetjain/Downloads/prank")
    print print_files_name
    
    #change the path where os can find files
    cwd_path = os.getcwd()
    os.chdir(r"/Users/puneetjain/Downloads/prank")

    #rename all the files
    for file_name in print_files_name:
        print "old file name :" + file_name
        print "new file name :" + file_name.translate(None, "1234567890") + "\n"
        
        os.rename(file_name,  file_name.translate(None, "1234567890"))
        
    os.chdir(cwd_path)

rename_files()
