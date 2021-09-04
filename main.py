import schedule
import os
import random

def auto_commit_job():
    print("==> Auto commit job start...")
    with open('autocommit.py', 'w',encoding='utf-8') as f:
        f.write(random.randint(1, 1000) * random.choice('abcdefghijk1235546'))
    import os
    os.system("git add .")
    
    files = [i for i in os.walk('./dotlib')][0][2]
    print(files)
    
    os.system('git commit -m "change %s"'%random.choice(files))
    os.system('git push -u origin feature_autocommit')



if __name__ == "__main__":
   
    schedule.every(10).seconds.do(auto_commit_job)
    import time
    while True:
        schedule.run_pending()
        time.sleep(5)
