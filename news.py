import os
import random
from datetime import datetime, timedelta

# User Configuration
email = "bhattarya4533@gmail.com"
username = "arybhatt4533"
days_to_backdate = 365 

os.system(f'git config user.email "{email}"')
os.system(f'git config user.name "{username}"')

def start_committing():
    if not os.path.exists('data.txt'):
        open('data.txt', 'a').close()
    
    print("Bhai, zig-zag pattern generate ho raha hai... Wait karo.")
    
    for i in range(days_to_backdate, -1, -1):
        base_date = datetime.now() - timedelta(days=i)
        is_weekend = base_date.weekday() >= 5 # 5=Sat, 6=Sun
        
        # --- Zig-Zag Logic ---
        rand_val = random.random()
        
        if is_weekend:
            # Weekends par 80% chance hai ki koi kaam na ho
            if rand_val < 0.80:
                continue
            commit_count = random.randint(1, 3) # Agar kiya bhi toh thoda sa
        else:
            # Weekdays par logic
            if rand_val < 0.35: # 35% chance gap ka
                continue
            elif rand_val > 0.92: # 8% chance heavy "Crunch Day" ka
                commit_count = random.randint(15, 25) # Dark Green!
            else:
                commit_count = random.randint(2, 7) # Normal Light/Medium Green

        for _ in range(commit_count):
            # Random time setting
            h = random.randint(9, 23)
            m = random.randint(0, 59)
            s = random.randint(0, 59)
            
            commit_date = base_date.replace(hour=h, minute=m, second=s).strftime('%Y-%m-%d %H:%M:%S')
            
            with open('data.txt', 'a') as f:
                f.write(f'Update log: {commit_date}\n')
            
            os.environ['GIT_AUTHOR_DATE'] = commit_date
            os.environ['GIT_COMMITTER_DATE'] = commit_date
            
            # Alag-alag messages taaki bot na lage
            msg_list = ["refactor: improve performance", "fix: minor bug in logic", "feat: add new module", "docs: update readme", "chore: clean up code"]
            message = random.choice(msg_list)
            
            os.system('git add data.txt')
            os.system(f'git commit --date="{commit_date}" -m "{message}" --quiet')

    print("\n--- Done! Pattern ekdam natural ban gaya hai. ---")
    print("Ab ye command chalao: git push -f origin main")

if __name__ == "__main__":
    start_committing()