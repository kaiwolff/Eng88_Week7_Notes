App Deployment - Running Notes

Deployment depends on environment

Project may not be a full app - it might just be a library for use in other apps. For example, the password analyser project might be more useful as an importable resource for another program.


“As .exe”

Will generate executable file that runs in the environment. Executable will be a binary that can run on, for example, Linux or Windows.

Writing a setup file

Entry_points: where apps will start running

Notice when importing things, the function imported will be run. Need to encase any running commands into an if statement asking if __name__ == __main__ , which means the function is the primary one being run.


Generally, any of the intro commands will go under a function called main_func() .

Once optimised for deployment: Need to install pyinstaller, and then use pyinstaller [python_file_name]

Pyinstaller will create an executable that can then be used in the target environment

Deploy as docker image

To do this, creating a docker image for the app.

Start by creating a file called Dockerfile

This will contain the configuration for the image

Explaining contents of dockerfile

FROM python:3
WORKDIR /usr/src/app

Define python as the starting point


ADD working_code.py
ADD common_passwords.txt 
ADD password_policy.txt

Add files the code needs to run

CMD [ "python", "./working_code.py" ]



How to execute the code


An app that requires user input, when running inside a docker image, doesn’t understand this idea by default. Therefore Docker needs to be told with the -it flag 


Once docker image is made and tested, if we add dockerhub username before it (e.g docker build -t kaiwolff/password-tools .

Can push this image to dockerhub similarly to a git push. Need to make sure docker login was executed first.

Can push either binary or source c ode. Pushing source code is beneficial

Can also connect dockerhub and github, and then, everytime you update github, dockerhub will build the image for you. Can also have private repos for the purpose of operating on commercially sensitive software.



Re-attempting building an executable

Running pyinstaller (need to make sure this is done via path, as the sudo apt installed version is not compatible with python 3.9)

This will create two new directories, dist and build. The executable will be inside dist.

#### Commands used

`sudo apt remove python3-pyinstaller`

`sudo apt-get install python3-distutils python3-apt`

`pip show pyinstaller`

`/home/kali/.local/bin/pyinstaller`


When building an app, there are best practices to consider:


When building a project, try to have a main directory named after the project, and then another directory with the same name. The second directory will have all the code contained in it. Generally, try to name the core portion of code main.py

The parent directory should contain the readme, vagrantfile, Dockerfile, etc. Anything concerned with the deployment of the program.

Each subdirectory should have a __init__.py file . This can be kept empty. This tells python that the subdirectory is necessary when importing the python from the parent directory.

Pip freeze

Pip freeze will give a list of what has been installed by pip. This is useful as it allows us to correctly set up the container we need. List can be exported by piping the output into a file, e.g

`pip freeze > requirements.txt`




The virtual environment starts out with no installed packages, so it is a good way to determine what packages are required for a code to work.Includes version information so that variation in this will not be able to break the ability to execute the app.


###Dockerfile modification

Can use RUN to run a pip install -r of a file containing the requirements


Using WORKDIR, can redirect working directory to the directory which contains the source code.


Dockerfile has many options, could try setting up a dockerfile that installs mysql and sets up the database


If you want to add everything int eh source code directory just put in

ADD [directory name] /[target name]

Remember to add a slash at the end so that tbhe things aren’t added to the same file, replacing each other in the process.

Back to pyinstaller

When building usign pyinstaller, the executable would need any associated files in the correct directory. Pyinstaller will not know how to move any dependent input or config files by itself

To associate them ,have to use the --add-data flag, followed by filenames

The command thus might become

`/home/kali/.local/bin/pyinstaller [main.py filepath] --add-data [filepath_1] --add-data [filepath_2]
`
And so on, covering all necessary files.

Can use a setup file in order to add multiple files (as it would obe quite annoying to run a command that covers a large number of additional files).

`--clean `

The above is a useful flag to start a pyinstaller process from scratch to avoid a buildup of junk files.

In this course, we will mainly be usign docker containers, as dockerhub enables the fully working thing to be published and it is easy to pull apps from dockerhub and run on AWS
