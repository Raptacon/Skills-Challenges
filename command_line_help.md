The notation \<something_to_replace\> means you should replace that part of the command with your specific entry. For example, if I had a robot named BreadBox, then I would replace \<robot_name\> with BreadBox.

In the terminal, you can use the up arrow button on your keyboard to look through commands you've previously run.

# OS

- cd \<some_directory_path\>
    - Changes the current directory that your terminal is working within. Windows uses backslashes to separate directory levels within a path
    - Using two dots, like ..\\, tells the terminal to start one directory level up and then look for the directory path you provide

# Git

For all of these commands, your terminal needs to be in a current directory that is within a git repository before executing. The commands will only affect the specific repository you are in.

- git clone \<repo_url\>
    - This copies a remote repository stored in GitHub down to your computer
    - You need to be connected to the Internet to run this command
- git status
    - This allows you to see which branch you are on, what code modifications are staged to be committed, and which modifications are not staged for commit
- git branch
    - This lists the branches that are available within a repository on your local computer 
- git checkout \<existing_branch_name\>
    - This allows you to switch to another branch that already exists
- git checkout -b \<new_branch_name\>
    - This allows you to create a new branch with the name you provide, using the current branch as the starting point
    - It's recommended that you run "git status" first to ensure you're starting from the right branch
- git add \<file_name_or_folder_name\>
    - This stages any modified files in the given file or folder for committing to the repository
- git commit -m "\<your_commit_message\>"
    - This commits (saves) the file modifications to the repository
    - The message you provide should briefly describe what changes you made
- git push
    - This sends all file modifications you've committed to the repository up to GitHub
    - You need to be connected to the Internet to run this command
- git pull
    - This copies down all new file modifications from GitHub to your computer
    - You need to be connected to the Internet to run this commandd
- git merge \<branch_name_with_updates\>
    - This updates the branch you are currently on with any new file modifications from the given branch
    - It's recommended that you run "git status" first to ensure you're updating the right branch

# Python

Depending on your computer, you may need to start the command with py, python, or python3. Please try these until you find the one that works for your computer. In the commands below, we assume "py" is the functional starter.

## RobotPy

- py -m robotpy sim
    - This runs the simulator for testing your robot code 
    - Your terminal needs be in the current directory that contains the robot.py file for the robot code you want to simulate
- py -m robotpy sync
    - This ensures that the RobotPy packages on your local computer match the current versions recommended by the package maintainers
    - You need to be connected to the Internet to run this command
    - You should run this before running the deploy command below
    - Your terminal needs be in the current directory that contains the robot.py file for the robot code you want to deploy
- py -m robotpy deploy
    - This deploys your robot code to the robot's physical RoboRIO
    - You need to be connected to the robot, either by Ethernet or WiFi radio, before running this command
    - Your terminal needs be in the current directory that contains the robot.py file for the robot code you want to deploy

## Virtual Environments

- py -m venv \<your_virtual_environment_name\>
    - This creates a new Python virtual environment
    - Your terminal should be in the current directory that directly contains the requirements.txt file that defines which packages should be installed for this environment before executing
- .\\<your_virtual_environment_name\>\Scripts\activate.ps1
    - This runs the PowerShell script that activates a specific Python virtual environment
    - This is only relevant to Windows operating systems
    - Your terminal needs to be in the current directory that directly contains the virtual environment folder before executing
- set-executionpolicy remotesigned
    - If you are unable to run the PowerShell script above to activate your virtual environment, then you need to execute this command once. Your terminal will always be capable of running PowerShell scripts thereafter
    - This is only relevant to Windows operating systems and should only be executed in PowerShell when running it as an administrator
- pip install -r \<path_to_requirements.txt\>
    - This installs the packages listed in the specified requirements.txt file within the current Python environment
    - You should only execute this command after activating your virtual environment
- deactivate
    - If you are in a virtual environment, this tells your terminal to deactivate that virtual environment
    - If you are not in a virtual environment, this does nothing