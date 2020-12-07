import subprocess, os, sys

# script_path = "/Users/dorhun/Desktop/Trainings/Python/Automation/Python_Automation/Exercise Files/Subprocesses/"
script_path = os.path.join(sys.path[0]) + '/'
print(script_path)

try:
    for i in range(0,5):
        subprocess.check_call(['python3',  script_path+"example.py"])

except subprocess.CalledProcessError as e:
    print("Cannot find the script file", e)
