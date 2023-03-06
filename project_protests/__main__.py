import sys
from project_protests.newspaper.compile_news_data import compile_news_data
import os
from  project_protests.html.dashboard import app 
import subprocess

current_dir = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":

    if len(sys.argv) == 1 :
        print("Will run 'compile_news' without creating the JSON files by\
                default. If you wanna create the JSON files before compiling\
                add 'collect_data' as the last argument.")
        compile_news_data()

    elif len(sys.argv) == 2:
        if sys.argv[1] == "compile_news":
            print("Will run 'compile_news' without creating the JSON files by\
                default. If you wanna create the JSON files before compiling\
                add 'collect_data' as the last argument.")
            compile_news_data()
        elif sys.argv[1] == "dashboard":
            print("Run dashboard")
            # exec(open(os.path.join(current_dir, "html/dashboard.py"))).read()
            # python -m dashboard.py
            app.run_server(port=8059,debug = True)

        elif sys.argv[1] == "run":
            print("Will run both 'compile_news' and 'dashboard' without\
                    creating the JSON files by default. If you wanna create the\
                    JSON files before compiling add 'collect_data' as the last\
                    argument.")
            compile_news_data()
            # exec(open(os.path.join(current_dir, "html/dashboard.py"))).read()
            # python -m dashboard.py
            app.run_server(port=8059,debug = True)
        else:
            print("Incorrect arguments. Send 'compile_news', 'dashboard' or\
                    'run'")
    
    elif len(sys.argv) == 3:
        if sys.argv[1] == "compile_news" and sys.argv[2] == "collect_data":
            compile_news_data(True)
        elif sys.argv[1] == "dashboard":
            print("Too many arguments. Send just 'dashboard'")
        elif sys.argv[1] == "run" and sys.argv[2] == "collect_data":
            compile_news_data(collect_data = True)
            # exec(open(os.path.join(current_dir, "html/dashboard.py"))).read()
            # python -m dashboard.py
            app.run_server(port=8059,debug = True)
        else:
            print("Incorrect arguments. Send 'compile_news', 'dashboard' or\
                    'run'")

    else:
        print("Too many arguments. Send 'compile_news', 'dashboard', or\
                'run'")
