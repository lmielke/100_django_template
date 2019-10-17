# 100_django_template


```python
!jupyter nbconvert --to script readme_setup.ipynb
```

    [NbConvertApp] Converting notebook readme_setup.ipynb to script
    [NbConvertApp] Writing 5672 bytes to readme_setup.py
    


```python
from IPython.display import Image
# imports needed to run installation routine
import os, shutil, subprocess
```

# 1. What am I

This is a simple django template with some pre implemented features such as:
- user signup, email confirmation,
- user logon, password create/change
- user authorization middleware
- blog style article/blog page to allow in tool documentation and commenting
- some param settings to allow multiple domains to map to this template (you may not need this, to remove, you have to make some changes the existing models and forms)
- some pre defined css sheet

# 2. Setup and installation using this notebook

This will clone the repository to your local drive, create a environment and install the requirements.txt, create a new git repro and commit all files
1. clone repo into your venvs location, using: git clone https://github.com/lmielke/100_django_template.git
2. in your cmd type: python
3. in your python cmd type: import readme_setup
4. enter ProjectName and ProjectPath when prompted


```python
# enter project name
# name of the project folder, that contains django project and django venv
cloneProjectName = "100_django_template"
yourProjectName = input("input your project name: ")
```

    input your project name:  101_django_template
    


```python
# enter project location
# this is the name of your Project Folder where the all your projects and venvs live
venvsPath = "/".join(os.getcwd().split("\\")[:-1])
inputVenvsPath = input(f"enter project location, press [Enter] if location is {venvsPath}: ")
venvsPath = inputVenvsPath if inputVenvsPath else venvsPath
go = input(f"repo: {yourProjectName} will be installed in: {venvsPath}, [Y/N]: ")
if go == "Y":
    print("\nstarting installation")
else:
    raise Exception("instalation aborted, to retry import readme_setup again")
```

    enter project location, press [Enter] if location is C:/python_venvs:  
    repo: 101_django_template will be installed in: C:/python_venvs, [Y/N]:  Y
    

    
    starting installation
    


```python
# some secrets are imported into settings.py from my_stuff.py
# a default my_stuff.py already exists inside the same folder as settings.py

# to continue with the default my_stuff.py file just assign a None value below and continue
myStuffPath = os.path.join(venvsPath, "99_snipp_block", "dj_conf_files", "my_stuff.py")
```

## 2.1. Install Preparation
### 2.1.1 Define relevant paths

### 2.1.2 Notebook does some prep work such as checking if venv exists and create some relevant paths


```python
# checks if venv already exists
# no need to modify
existingEnvironments = os.listdir(venvsPath)
if yourProjectName in existingEnvironments:
    raise Exception(f"UUUUPPPPSSS: AN Environement with name {yourProjectName} already exists in {venvsPath} \n{existingEnvironments}")
else:
    print("ready to go")
```

    ready to go
    

### 2.1.3. venv directory will be renamed to what you specified above


```python
os.chdir(venvsPath)
os.rename(cloneProjectName, yourProjectName)
```

# 2.2. Install Environment


```python
# this creates a empty environment inside yourVenvPath
yourProjectPath = os.path.join(venvsPath, yourProjectName)
subprocess.call(["python", "-m", "venv", os.path.join(yourProjectPath, "venv")], shell=True)
```




    0




```python
# this copies files to allow subprocess to activate your environment
newEnvActPy = os.path.join(yourProjectPath, "venv", "Scripts", "activate_this.py")
shutil.copyfile(os.path.join(yourProjectPath, "resources", "activate_this.py"), newEnvActPy)
```




    'C:\\python_venvs\\101_django_template\\venv\\Scripts\\activate_this.py'




```python
# this copies my private my_stuff.py file from your local location into the venv
# if you have assigned None to the myStuffPath this step will do nothing
# you have to manually adjust your my_stuff.py file however. Its location is same as settings.py
try:
    print(myStuffPath)
    shutil.copyfile(myStuffPath, os.path.join(yourProjectPath, "web_project", "web_project", "my_stuff.py"))
except:
    raise Exception("copying my_stuff.py failed because path does not exist! You have to manually adjust my_stuff.py. Its location is same as settings.py")
```

    C:\python_venvs\99_snipp_block\dj_conf_files\my_stuff.py
    

### 2.2.1. Installs all content of new environment, i.e. requirements.txt ect.


```python
exec(open(newEnvActPy).read(), dict(__file__ = newEnvActPy))
# all relevant programs are installed and/or updated
# feel free to add or remove programs
subprocess.call(["python", "-m", "pip", "install", "--upgrade", "pip"], shell=True)
subprocess.call(["pip", "install", "--upgrade", "setuptools"], shell=True)

# i use pyperclip inside some service scripts, its not needed for this repo to run, you can remove it
subprocess.call(["pip", "install", "pyperclip"], shell=True)

# this installs the requirements.txt
subprocess.call(["pip", "install", "-r", os.path.join(yourProjectPath, "resources", "requirements.txt")], shell=True)
```




    0



### 2.2.2. Try migrations


```python
# this makes migrations although there should be none
os.chdir(os.path.join(yourProjectPath, "web_project"))
print(f"your manage.py is under {os.getcwd()}")
subprocess.call(['python', 'manage.py', 'makemigrations'], shell=True)
subprocess.call(['python', 'manage.py', 'migrate'], shell=True)
```

    your manage.py is under C:\python_venvs\101_django_template\web_project
    




    0




```python
os.chdir(venvsPath)
```

# The installation is now complete.

Dont forget to:
1. change the my_stuff.py file (its in the same dir as settings.py)
2. Activate your environment: To activate it, type {{yourVenvPath}}\Scripts/activate.bat (on windows)
3. Create your admin user: To create it, go to the web_project folder and and run: manage.py createsuperuser
4. Test your installation!!! To test it, go to the web_project folder and and run: python manage.py runserver

# 3. Manual Setup
## 3.1. Run above steps manually :)


```python

```
