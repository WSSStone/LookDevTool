import os, sys, subprocess, time
from utils.path_helper import handle_spaced_dir

def svn_update_with_timeout(work_dir:str, timeout:int=300) -> int:
    os.chdir(work_dir)

    should_run = True
    
    while should_run:
        os.system("svn cleanup")
        try:
            start_time = time.time()

            print(f"Starting 'svn update' in {work_dir}...")
            # run svn update in new thread with timeout
            result = subprocess.run(['svn', 'update', work_dir],
                                    timeout=timeout,
                                    check=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        
            # if subprocess finishes
            if result.returncode == 0:
                elapsed_time = time.time() - start_time
                print(f"'svn update' completed successfully in {elapsed_time:.2f} seconds.")
                should_run = False
                # exit
                break

        # if subprocess does not finish within $timeout$ seconds, raise TimeoutExpired exception
        except subprocess.TimeoutExpired:
            print(f"'svn update' timed out after {timeout} seconds. Retrying...")
            
        # other errors
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during 'svn update': {e}")

def main(argv):
    if len(argv) < 2:
        print("Empty Input")
        return
    
    work_dir = handle_spaced_dir(argv)
    
    svn_update_with_timeout(work_dir, timeout=60)

if __name__ == '__main__':
    main(sys.argv)
