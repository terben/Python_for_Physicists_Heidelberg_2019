# How to download and use course materials

The course is hosted on `github` and updated daily with new materials.

There are two possibilities to obtain and to use the course materials:

- You can follow the course and use the materials entirely within a
  Web-Browser - no need to install or to setup *anything*!

  Just click the following button [![Binder](https://ingress.binderhub.astro.uni-bonn.de/badge_logo.svg)](https://ingress.binderhub.astro.uni-bonn.de/v2/gh/terben/Python_for_Physicists_Heidelberg_2019/master) to launch an interactive session of the course materials.

  **Note:** You can work and modify the materials in this way.
    However, all your changes are lost as soon as you leave the
    Web-Browser session! To save your changes, you need to manually
    save the modified notebooks (`File` -> `Download as` ->
    `Notebook`)

- Download the materials from `github` aud use them on your own computer
  (CIP-pool or own laptop). This is definitely preferred to the option above.

  In the following, I describe necessary steps in a
  `Unix/Linux/OSX`-enviroenment. Please ask me for `Windows`-

  Those familiar with `git` and `github` should download and
  administrate the course materials with `git`-commands.

  A way to obtain the materials easily without `git`-knowledge is:

  1. Create a directory, where you want to store course materials. This
  only needs to be done once for the whole course.

  2. Go to that directory and execute and download the script
     `get_current_course_materials.sh` via

     ```
     user$ wget https://github.com/terben/Python_for_Physicists_Heidelberg_2019/raw/master/retrieve_materials/get_current_course_materials.sh
     ```

     or via [this link](https://github.com/terben/Python_for_Physicists_Heidelberg_2019/raw/master/retrieve_materials/get_current_course_materials.sh). This only needs to be done once for the whole
     course.

  3. At the begining of each course-day, go to the directory and execute:

     ```
     user$ bash get_current_course_materials.sh
     Cloning into 'Python_for_Physicists_Heidelberg_2019'...
     .
     .
     user$ ls
     python_course_2019-04-01 ... # 2019-04-01 needs to be subtituted
                                  # by the current date
     user$ cd python_course_2019-04-01/Python_for_Physicists_Heidelberg_2019
     user$ bash start-jupyter-notebook.sh   # to start working on the notebooks
     ```

     After that, do **on a Heidelberg CIP-Pool computer**

     ```
     user$ bash start-jupyter-notebook.sh # to start working on the notebooks
     ```

     and on your own laptop

     ```
     user$ jupyter notebook
     ```

     **Note:** Please **do not** do the call `jupyter notebook` on one
       of the CIP-Pool computers! If you do, you might get into a
       conflict with another users notebook-session!
