import subprocess

# Function to get the current Git branch
def get_current_git_branch():
    try:
        # Run a Git command to get the current branch
        result = subprocess.check_output(['git', 'branch', '--show-current'], text=True)
        return result.strip()
    except subprocess.CalledProcessError:
        # Handle the case where Git is not installed or there is no Git repository
        return None

# Main program
if __name__ == "__main__":
    # Check the current Git branch
    current_branch = get_current_git_branch()

    # Check if the current branch is "develop"
    if current_branch == "develop":
        print("Hello World, 3")
    else:
        print(f"This program should be run on the 'develop' branch, but you are on '{current_branch}' branch.")
