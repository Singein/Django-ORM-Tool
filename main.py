import schedule
import os
import random

def auto_commit_job():
    print("==> Auto commit job start...")
    codes = open("autocommit.py", encoding='utf-8').read()
    codes.replace('\n', random.randint(0, 10) * '\n')
    with open('autocommit.py', 'w',encoding='utf-8') as f:
        f.write(codes)
    import os
    os.system("git add .")
    
    files = [i for i in os.walk('./dotlib')][0][2]
    print(files)
    
    os.system('git commit -m "change %s"'%random.choice(files))
    os.system('git push origin')



if __name__ == "__main__":
    import os
    files = [i for i in os.walk('./dotlib')][0][2]
    print(files)
    auto_commit_job()
    # schedule.every(10).minutes.do(auto_commit_job)
