import os
import time

def main():
    path = (os.path.dirname(__file__)) + "/dustyDish.py" if len(os.path.dirname(__file__)) > 1 else "./dustyDish.py"
    os.system("python3 " + path)
    
if __name__ == '__main__':
    with open('stop.sh', 'w') as f:
        f.write('kill ' + str(os.getpid()) + "\nrm stop.sh")
        stop_path = os.path.dirname(__file__) + "/stop.sh" if len(os.path.dirname(__file__)) > 1 else "./stop.sh" # create stop script
        os.system("sudo chmod +x " + stop_path) #make stop.sh executable
        
    while True:
        main()
        time.sleep(7200)    
    