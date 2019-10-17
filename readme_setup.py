#!/usr/bin/env python
# coding: utf-8

# # 100_django_template

# In[2]:


from IPython.display import Image
# imports needed to run installation routine
import os, shutil, subprocess


# # 1. What am I

# This is a simple django template with some pre implemented features such as:
# - user signup, email confirmation,
# - user logon, password create/change
# - user authorization middleware
# - blog style article/blog page to allow in tool documentation and commenting
# - some param settings to allow multiple domains to map to this template (you may not need this, to remove, you have to make some changes the existing models and forms)
# - some pre defined css sheet

# # 2. Setup and installation using this notebook

# This will clone the repository to your local drive, create a environment and install the requirements.txt, create a new git repro and commit all files
# 1. clone repo into your venvs location, using: git clone https://github.com/lmielke/100_django_template.git
# 2. copy the readme_setup.py file to a location outside the new project folder
# 3. cd into the readme_setup.py location and type: python
# 4. in your python cmd type: import readme_setup
# 5. enter ProjectName and ProjectPath when prompted
# 6. remove readme_setup.py file

# In[3]:


# enter project name
# name of the project folder, that contains django project and django venv
cloneProjectName = "100_django_template"
yourProjectName = input("input your project name: ")


# In[4]:


# enter project location
# this is the name of your Project Folder where the all your projects and venvs live
venvsPath = "/".join(os.getcwd().split("\\")[:-1])
inputVenvsPath = input(f"enter project location, press [Enter] if location is {venvsPath}/{yourProjectName}: ")
venvsPath = inputVenvsPath if inputVenvsPath else venvsPath
go = input(f"repo: {cloneProjectName} will be renamed and venv installed in: {venvsPath}/{yourProjectName}, [Y/N]: ")
if go == "Y":
    print("\nstarting installation")
else:
    raise Exception("instalation aborted, to retry import readme_setup again")


# In[5]:


# some secrets are imported into settings.py from my_stuff.py
# a default my_stuff.py already exists inside the same folder as settings.py

# to continue with the default my_stuff.py file just assign a None value below and continue
myStuffPath = os.path.join(venvsPath, "99_snipp_block", "dj_conf_files", "my_stuff.py")


# ## 2.1. Install Preparation
# ### 2.1.1 Define relevant paths

# ### 2.1.2 Notebook does some prep work such as checking if venv exists and create some relevant paths

# In[6]:


# checks if venv already exists
# no need to modify
existingEnvironments = os.listdir(venvsPath)
if yourProjectName in existingEnvironments:
    raise Exception(f"UUUUPPPPSSS: AN Environement with name {yourProjectName} already exists in {venvsPath} \n{existingEnvironments}")
else:
    print("ready to go")


# ### 2.1.3. venv directory will be renamed to what you specified above

# In[14]:


os.chdir(venvsPath)
os.rename(cloneProjectName, yourProjectName)


# # 2.2. Install Environment

# In[15]:


# this creates a empty environment inside yourVenvPath
yourProjectPath = os.path.join(venvsPath, yourProjectName)
subprocess.call(["python", "-m", "venv", os.path.join(yourProjectPath, "venv")], shell=True)


# In[29]:


# this copies files to allow subprocess to activate your environment
newEnvActPy = os.path.join(yourProjectPath, "venv", "Scripts", "activate_this.py")
shutil.copyfile(os.path.join(yourProjectPath, "resources", "activate_this.py"), newEnvActPy)


# In[26]:


# this copies my private my_stuff.py file from your local location into the venv
# if you have assigned None to the myStuffPath this step will do nothing
# you have to manually adjust your my_stuff.py file however. Its location is same as settings.py
try:
    print(myStuffPath)
    shutil.copyfile(myStuffPath, os.path.join(yourProjectPath, "web_project", "web_project", "my_stuff.py"))
except:
    raise Exception("copying my_stuff.py failed because path does not exist! You have to manually adjust my_stuff.py. Its location is same as settings.py")


# ### 2.2.1. Installs all content of new environment, i.e. requirements.txt ect.

# In[30]:


exec(open(newEnvActPy).read(), dict(__file__ = newEnvActPy))
# all relevant programs are installed and/or updated
# feel free to add or remove programs
subprocess.call(["python", "-m", "pip", "install", "--upgrade", "pip"], shell=True)
subprocess.call(["pip", "install", "--upgrade", "setuptools"], shell=True)

# i use pyperclip inside some service scripts, its not needed for this repo to run, you can remove it
subprocess.call(["pip", "install", "pyperclip"], shell=True)

# this installs the requirements.txt
subprocess.call(["pip", "install", "-r", os.path.join(yourProjectPath, "resources", "requirements.txt")], shell=True)


# ### 2.2.2. Try migrations

# In[32]:


# this makes migrations although there should be none
os.chdir(os.path.join(yourProjectPath, "web_project"))
print(f"your manage.py is under {os.getcwd()}")
subprocess.call(['python', 'manage.py', 'makemigrations'], shell=True)
subprocess.call(['python', 'manage.py', 'migrate'], shell=True)


# In[33]:


os.chdir(venvsPath)


# # The installation is now complete.
# 
# Dont forget to:
# 1. change the my_stuff.py file (its in the same dir as settings.py)
# 2. Activate your environment: To activate it, type {{yourVenvPath}}\Scripts/activate.bat (on windows)
# 3. Create your admin user: To create it, go to the web_project folder and and run: manage.py createsuperuser
# 4. Test your installation!!! To test it, go to the web_project folder and and run: python manage.py runserver

# # 3. Manual Setup
# ## 3.1. Run above steps manually :)

# In[ ]:




