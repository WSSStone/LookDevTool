import os, sys, subprocess, time
from utils.path_helper import handle_spaced_dir

def svn_update_with_timeout(work_dir:str, timeout:int=30) -> int:
    os.chdir(work_dir)

    should_run = True
    
    while should_run:
        os.system("svn cleanup")
        try:
            # Record the start time
            start_time = time.time()

            print(f"Starting 'svn update' in {work_dir}...")
            # Run the 'svn update' command with a timeout
            result = subprocess.run(['svn', 'update', work_dir], timeout=timeout, check=True)
        
            if result.returncode == 0:
                # Calculate the total time taken for the update
                elapsed_time = time.time() - start_time
                print(f"'svn update' completed successfully in {elapsed_time:.2f} seconds.")
                should_run = False
                break  # Exit the loop on success

        except subprocess.TimeoutExpired:
            print(f"'svn update' timed out after {timeout} seconds. Retrying...")

            # Kill the running process (subprocess.run handles this automatically on timeout)
            # Retrying will be handled in the next loop iteration
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during 'svn update': {e}")
            # You can decide whether to retry or exit the loop here based on the error

def main(argv):
    if len(argv) < 2:
        print("Empty Input")
        return
    
    work_dir = handle_spaced_dir(argv)
    
    svn_update_with_timeout(work_dir)

if __name__ == '__main__':
    main(sys.argv)