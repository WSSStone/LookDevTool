import os, sys, subprocess, time
from utils.path_helper import handle_spaced_dir

def svn_update_with_timeout(work_dir:str, timeout:int=300) -> int:
    os.chdir(work_dir)

    should_run = True
    proc = None
    
    while should_run:
        if proc is None:
            # reset status
            os.system("svn cleanup")
            
            start_time = time.time()

        try:
            if proc is None:
                print(f"Starting 'svn update' in {work_dir}...")
                proc = subprocess.Popen(['svn', 'update', work_dir],
                                        bufsize=0,
                                        universal_newlines=True,
                                        stdout=subprocess.PIPE,
                                        text=True,
                                        stdin=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,
                                        creationflags=subprocess.CREATE_NEW_CONSOLE)
        
            # timeout if subprocess print nothing
            output = proc.stdout.readline()
            if len(output) > 0:
                start_time = time.time()
                print(f"['svn update']: {output}")
                output = None
            else:
                if time.time() - start_time >= timeout:
                    print(f"'svn update' timed out after {timeout} seconds. Retrying...")
                    proc.terminate()
                    proc = None
                    continue
                
            # if subprocess finishes
            if proc.poll() is not None:
                if proc.returncode == 0:
                    elapsed_time = time.time() - start_time
                    print(f"'svn update' completed successfully in {elapsed_time:.2f} seconds.")
                else:
                    print(f"'svn update' completed with error code {proc.returncode}.")
                proc.terminate()
                proc.wait()
                proc = None
                should_run = False
                break

        except subprocess.TimeoutExpired:
            print(f"'svn update' timed out after {timeout} seconds. Retrying...")
            
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during 'svn update': {e}")
            
        except KeyboardInterrupt:
            proc.terminate()
            proc.wait()

def main(argv):
    if len(argv) < 2:
        print("Empty Input")
        return
    
    work_dir = handle_spaced_dir(argv)
    
    svn_update_with_timeout(work_dir, timeout=10)

if __name__ == '__main__':
    main(sys.argv)
