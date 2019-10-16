# 100_django_template


```python
from IPython.display import Image
# imports needed to run installation routine
import os, shutil, subprocess
baseDir = os.getcwd()
img = os.path.join(baseDir, "django_template.jpg")
sampleImage = Image(img)
```

# 1. What am I

This is a simple django template with some pre implemented features such as:
- user signup, email confirmation,
- user logon, password create/change
- user authorization middleware
- blog style article/blog page to allow in tool documentation and commenting
- some param settings to allow multiple domains to map to this template (you may not need this, to remove, you have to make some changes the existing models and forms)
- some pre defined css sheet

![title](media/django_template.jpg)


```python
# this is to stop you from accidently running the notebook, to continue type: continue
breakpoint()
```

    --Call--
    > c:\users\lars\appdata\local\programs\python\python37\lib\site-packages\ipython\core\displayhook.py(252)__call__()
    -> def __call__(self, result=None):
    

    (Pdb)  continue
    

# 2. Setup and installation using this notebook

This will clone the repository to your local drive, create a environment and install the requirements.txt, create a new git repro and commit all files
1. create a venv directory for the virtual environment (the venv itself is created by this notebook)
2. create a new github repo to manage your code (if you want)
3. run the notebook cell by cell and follow the instructions


```python
# this is the path of my github repo
# do not change this cell
remoteOrigin = "https://github.com/lmielke/100_django_template.git"
cloneProjectName = "100_django_template"
```

## 2.1. Install Preparation
### 2.1.1 Define relevant paths


```python
# change all variables below

# path where your venvs are located
venvsPath = os.path.abspath(r"C:/python_venvs")

# url to your new githup repo if you want to create a new repo
newOrigin = "https://github.com/lmielke/101_django_template.git"

# name of your new environment/repo/project which lives inside your venvs path
yourProjectName = "101_django_template"

# some private content i.e. logon info, sshd info, is not part of the 100_django_template
# therefore I copy these files from a local location
# if you dont have these files, you have to set both values to None
# NOTE: you have to manually change this file after install is complete (run Notebook first)
my_stuff_path = r"C:\python_venvs\99_snipp_block\dj_conf_files\my_stuff.py" # set to None if no file
# set to None if not relevant
sshd_config_path = r"C:\python_venvs\99_snipp_block\dj_conf_files\sshd_config" # set to None if no file
```

### 2.1.2 Notebook does some prep work such as checking if venv exists and create some relevant paths


```python
# check if venv already exists
# no need to modify
existingEnvironments = os.listdir(venvsPath)
if yourProjectName in existingEnvironments:
    print(f"UUUUPPPPSSS: AN Environement with name {yourProjectName} already exists in {venvsPath} \n{existingEnvironments}")
    print("\n\nNOTE: Continuing will override the existing environment and you deserve whatever happens then !!")
else:
    print("ready to go")
```

    ready to go
    


```python
# python creates some relevant paths
# no need to modify
newRepoPath = os.path.join(venvsPath, yourProjectName)
newEnvPath = os.path.join(venvsPath, yourProjectName, 'venv')
yourProjectPath = os.path.join(venvsPath, yourProjectName)
yourVenvPath = os.path.join(yourProjectPath, 'venv')
templateActPy = os.path.join(yourProjectPath, 'resources', 'activate_this.py')
newEnvActPy = os.path.join(yourProjectPath, 'venv', 'Scripts', 'activate_this.py')
newEnvReqTxt = os.path.join(yourProjectPath, 'resources', 'requirements.txt')
djangoProjectPath = os.path.join(yourProjectPath, "web_project")
```

### 2.1.3. Clone the repo to local venvs directory


```python
# this will create a folder with the name you specified inside your venv folder and copy all relevant files from my repo
os.chdir(venvsPath)
subprocess.call(['git', 'clone', remoteOrigin], shell=True)
```




    0



### 2.1.4. venv directory will be renamed to what you specified above


```python
os.chdir(venvsPath)
os.rename(cloneProjectName, yourProjectName)
```

### 2.1.5. Remove old origin and create new one


```python
# to check: open cmd, go to Project folder and type: git remote -v
os.chdir(yourProjectPath)
subprocess.call(["git", "remote", "set-url", "origin", newOrigin], shell=True)
```

# 2.2. Install Environment


```python
# this creates empty environment inside yourVenvPath
subprocess.call(["python", "-m", "venv", yourVenvPath], shell=True)
```




    0




```python
# this copies files to activate your environment
shutil.copyfile(templateActPy, newEnvActPy)
# this copies my private files from my local location into the venv
if my_stuff_path: shutil.copyfile(my_stuff_path, os.path.join(yourProjectPath, "web_project", "web_project", "my_stuff.py"))
if sshd_config_path: shutil.copyfile(sshd_config_path, os.path.join(yourProjectPath, "conf_files", "sshd_config"))
```

### 2.2.1. Installs all content of new environment, i.e. requirements.txt ect.


```python
exec(open(newEnvActPy).read(), dict(__file__ = newEnvActPy))
# all relevant programs are installed and/or updated
subprocess.call(["python", "-m", "pip", "install", "--upgrade", "pip"], shell=True)
subprocess.call(["pip", "install", "--upgrade", "setuptools"], shell=True)
subprocess.call(["pip", "install", "pyperclip"], shell=True)
# this installs the requirements.txt
subprocess.call(["pip", "install", "-r", newEnvReqTxt], shell=True)
```




    0



### 2.2.2. Try migrations


```python
# this makes migrations although there should be none
os.chdir(djangoProjectPath)
print(djangoProjectPath)
subprocess.call(['python', 'manage.py', 'makemigrations'], shell=True)
subprocess.call(['python', 'manage.py', 'migrate'], shell=True)
```

    C:\python_venvs\101_django_template\web_project
    




    0




```python
os.chdir(venvsPath)
```

# The installation is now complete.

Dont forget to:
1. change the my_stuff.py file (its in the same dir as settings.py)
2. ad a sshd_config file if needed (should not be relevant for your right now)
3. Activate your environment: To activate it, type {{yourVenvPath}}\Scripts/activate.bat (on windows)
4. Create your admin user: To create it, go to the web_project folder and and run: manage.py createsuperuser
5. Test your installation!!! To test it, go to the web_project folder and and run: python manage.py runserver

# 3. Manual Setup
## 3.1. Run above steps manually :)


```python

```
