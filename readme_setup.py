import multiprocessing, os, re, shutil, subprocess, sys, time
import argparse

parser = argparse.ArgumentParser(description="wtf")
parser.add_argument('yourProjectName', help='folder Name your project will exsist as')
parser.add_argument('yourHost', help='prod: IP, dev: http://localhost:8000')
parser.add_argument('-pid', type=int, required=False, help='internally used pid to cancel init process')

venvsPath = os.getcwd()
cloneProjectName = "100_django_template"
yourProjectName = parser.parse_args().yourProjectName
print(f"your new project will be in: {venvsPath}/{yourProjectName}")
yourProjectPath = os.path.join(venvsPath, yourProjectName)
djProjectPath = os.path.join(yourProjectPath, "web_project")
newEnvActPy = os.path.join(yourProjectPath, "venv", "Scripts", "activate_this.py")

def main(*args):
    # enter project name
    # name of the project folder, that contains django project and django venv
    myStuffPath = os.path.join(venvsPath, "99_snipp_block", "dj_conf_files", "my_stuff.py")
    existingEnvironments = os.listdir(venvsPath)
    if yourProjectName in existingEnvironments:
        raise Exception(f"UUUUPPPPSSS: AN Environement with name {yourProjectName} already exists in {venvsPath} \n{existingEnvironments}")
    else:
        print("ready to go")
    os.chdir(venvsPath)
    os.rename(cloneProjectName, yourProjectName)
    subprocess.call(["python3", "-m", "venv", os.path.join(yourProjectPath, "venv")], shell=True)
    # this copies files to allow subprocess to activate your environment
    shutil.copyfile(os.path.join(yourProjectPath, "resources", "activate_this.py"), newEnvActPy)

    try:
        print(myStuffPath)
        shutil.copyfile(myStuffPath, os.path.join(yourProjectPath, "web_project", "web_project", "my_stuff.py"))
    except:
        raise Exception("copying my_stuff.py failed because path does not exist! You have to manually adjust my_stuff.py. Its location is same as settings.py")

    exec(open(newEnvActPy).read(), {'__file__': newEnvActPy})
    # all relevant programs are installed and/or updated
    # feel free to add or remove programs
    subprocess.call(["python", "-m", "pip", "install", "--upgrade", "pip"], shell=True)
    subprocess.call(["pip", "install", "--upgrade", "setuptools"], shell=True)

    # i use pyperclip inside some service scripts, its not needed for this repo to run, you can remove it
    subprocess.call(["pip", "install", "pyperclip"], shell=True)

    # this installs the requirements.txt
    subprocess.call(["pip", "install", "-r", os.path.join(yourProjectPath, "resources", "requirements.txt")], shell=True)

    djProjectPaht = os.path.join(yourProjectPath, "web_project")
    os.chdir(djProjectPaht)
    print(f"your manage.py is under {os.getcwd()}")
    subprocess.call(['python', 'manage.py', 'makemigrations'], shell=True)
    subprocess.call(['python', 'manage.py', 'migrate'], shell=True)
    return djProjectPath, newEnvActPy


def run_server(*args):
    exec(open(newEnvActPy).read(), dict(__file__ = newEnvActPy))
    os.chdir(djProjectPath)
    subprocess.call(['python', 'manage.py', 'runserver'], shell=True)
    return True


def test_server():
    import requests, time
    from datetime import datetime as dt
    from datetime import timedelta as td
    time.sleep(5)
    # timeCheck = requests.get("http://localhost:8000").text.find(f"{dt.now() - td(hours=2):%H:%M}")
    # success = True if timeCheck != -1 else False
    match = re.compile(r"(<CHPID>)(\d{3,6})(</CHPID>)")
    prcId = re.search(match, requests.get(parser.parse_args().yourHost).text)[2]
    subprocess.call(['TASKKILL', '/PID', str(prcId), '/F'], shell=True)
    if prcId:
        print(f"\n\n\tSUCCSESS: Server ran successfully with prcId: {prcId}\n\n")
    else:
        print(f"\n\n\tWARNING: Server run could not be confirmed\n\n")
    return True


# In[ ]:


if __name__ == '__main__':
    setupPath = os.path.join(venvsPath, "readme_setup.py")
    os.chdir("/".join(venvsPath.split('\\')[:-1]))
    installPath = os.path.join(os.getcwd(), "readme_setup.py")
    if os.path.isfile(installPath):
        if parser.parse_args().pid:
            print(f"in if with: {os.getpid()} and {(parser.parse_args().pid)}")
            subprocess.call(["TASKKILL", "/PID", str(parser.parse_args().pid), "/F"], shell=True)
            time.sleep(1)
            print(f"killed {parser.parse_args().pid} but continuing")
            prcId = None
            a = multiprocessing.Process(target=main, args=(cloneProjectName, yourProjectName, venvsPath, yourProjectPath, djProjectPath, newEnvActPy))
            b = multiprocessing.Process(target=run_server, args=(cloneProjectName, yourProjectName, venvsPath, yourProjectPath, djProjectPath, newEnvActPy))
            c = multiprocessing.Process(target=test_server)
            a.start()
            a.join()
            print("install is done")
            b.start()
            c.start()
            c.join()
            print(f"now deleting readme_setup.py from {os.getcwd()}")
            subprocess.call(["del", "readme_setup.py"], shell=True)
            print("INSTALL COMPLETE")
        else:
            print("file already exists, delete readme_setup.py first and retry")
    else:
        shutil.copyfile(setupPath, installPath)
        print(f"in else with: {os.getpid()}")
        if  not parser.parse_args().pid:
            print("calling subprocess")
            subprocess.call(['readme_setup.py', '100_django_template', 'http://localhost:8000', '-pid', str(os.getpid())], shell=True)
        else:
            print(f"in subprocess with: {parser.parse_args().pid}")


"""

lone repo into folder in which this repo will exist --> (cd [venvs folder] && git clone https://github.com/lmielke/100_django_template.git)

Copy the readme_setup.py file into your venvs folder --> (cd 100_django_template && copy readme_setup.py .. && cd ..)

[description]
"""




