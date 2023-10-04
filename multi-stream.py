import concurrent.futures

def run_script(script_name):
    try:
        import subprocess
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

if __name__ == "__main__":
    script_list = ["PAST_SEM/Data_Science/ADAS-Blind-Spot-Detection/rear.py", "PAST_SEM/Data_Science/ADAS-Blind-Spot-Detection/right.py", "PAST_SEM/Data_Science/ADAS-Blind-Spot-Detection/front.py", "PAST_SEM/Data_Science/ADAS-Blind-Spot-Detection/left.py"]  # Add more file names as needed

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(run_script, script_list)