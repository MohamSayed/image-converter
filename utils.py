"""
* description:
    1) Append all directory and sub of the given list of directories to import path,
    i.e:
       utils.system.append(["core", "data", "UI", "project"])
    
       You can path exclude list too.

    2) return dir & subdirs of given path, like ud in linux.

    3) return files list from the given path & its subdirs.

"""
import os
import sys


class System():
    def dirs_tree(self, path):
        directories = []
        for root, _, _ in os.walk(path):
            directories.append(repr(root))
        return directories

    def files_tree_list(path, extensions=[]):
        """
           *  path: start path
           *  extensions: if you want to get specific file extension; pass in the extensions
                         else, leave it as default
        """
        files = []
        for file_or_dir in os.listdir(path):
            if os.path.isdir(path + os.sep + file_or_dir):
                print("* subdir was found")
                files.extend(System.files_tree_list(
                    path + os.sep + file_or_dir, extensions=extensions))
            else:
                if extensions:
                    for extension in extensions:
                        if extension in file_or_dir.lower():
                            files.append(path + os.sep + file_or_dir)
                else:
                    files.append(path + os.sep + file_or_dir)

        return files

    def files_list(path, extensions=[]):
        files = []
        for file_or_dir in os.listdir(path):
            if os.path.isdir(path + os.sep + file_or_dir):
                pass
            else:
                if extensions:
                    for extension in extensions:
                        if extension in file_or_dir.lower():
                            files.append(path + os.sep + file_or_dir)
                else:
                    files.append(path + os.sep + file_or_dir)

        return files

    def walk(self, dirs, excludes=[]):
        dir_list = []
        for dir in dirs:
            for i in os.listdir(dir):
                if not i in excludes:
                    dir_list.append(i)
        return dir_list

    def append(self, dirs, excludes=[]):
        for dir in self.walk(dirs, excludes=excludes):
            sys.path.append(dir)


if __name__ == "__main__":
    # print(System.dirs_tree("build"))
    # print(System.walk(["build"]))
    for i in System.files_tree_list("blank", extensions="jpg"):
        print(i)
