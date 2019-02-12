from cx_Freeze import setup, Executable
build_exe_options = {"excludes": ["tkinter", 
                     "QtSql", "email", "socket", "http", "PyQt5", "numpy",
                     "_ssl", "_socket", "xml", "html"
                     ]}
setup(name = "image-converter" ,
      version = "0.2" ,
      author = "me6789",
      options = {"build_exe": build_exe_options},
      executables = [Executable("image-converter.py")])