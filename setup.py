from cx_Freeze import setup, Executable


build_exe_options = {"excludes": ["tkinter",
                                  "QtSql", "email", "socket", "http", "numpy",
                                  "_ssl", "_socket", "xml", "html"
                                  ], "include_files": ['ui/']}
setup(name="image-converter",
      version="0.2",
      author="me6789",
      options={"build_exe": build_exe_options},
      executables=[Executable("image-converter-gui.py", base='Win32GUI'), 
                   Executable("image-converter.py")])
