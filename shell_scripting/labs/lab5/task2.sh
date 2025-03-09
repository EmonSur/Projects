#!/bin/bash

# Step 1: Create Remote Repository
# (Remote repository is a repository hosted in a location seperate from your local machine. It allows multiple users to collaborate and share changes).
rm -rf remote_repo ann_repo bob_repo  # Clean up if directories exist
mkdir remote_repo
cd remote_repo
git init --bare  # Create a bare remote repo
cd ..

# Step 2: Ann's Work - Initialize Local Repo & Push First Commit
mkdir ann_repo && cd ann_repo
git init
git config user.name "Ann"
git config user.email "ann@example.com"

# Link to remote repository
git remote add origin ../remote_repo
# Now git will register the repository created earlier as a remote repository. I can now pull/push changes to/from ../remote_repo using git push/pull origin <branch>

# Create main.py
cat > main.py <<EOF
import helper  

def main():
    print("This is Ann's main script.")
    helper.greet()  # Calls function from helper.py  

if __name__ == "__main__":
    main()
EOF

# Commit and push Ann's initial code
git add main.py
git commit -m "Ann: Initial commit with main.py"
git push origin master

cd ..  # Back to the root directory

# Step 3: Bob Clones the Remote Repository
git clone remote_repo bob_repo
cd bob_repo
git config user.name "Bob"
git config user.email "bob@example.com"

# Create helper.py
cat > helper.py <<EOF
def greet():
    print("Hello from Bob's helper script!")
EOF

# Commit and push Bob's changes
git add helper.py
git commit -m "Bob: Added helper.py"
# Push changes from your local repository to the master branch of the remote repository
git push origin master

cd ..  # Back to the root directory

# Step 4: Ann Merges Bob's Changes
cd ann_repo
git pull origin master  # Fetch Bob's changes

# Ann commits a minor update to main.py (ensuring it calls helper.py)
git add main.py
# This allows you to make a commit without having made any changes.
git commit --allow-empty -m "Ann: Merged Bob's changes and finalized main.py"
# Attempts to pull changes from the master branch of the remote repo into the current local branch
git push origin master

cd ..  # Back to the root directory

# Step 5: Final Verification by Bob
cd bob_repo
git pull origin master  # Get the latest version

# Display commit history in the current repo, including commits from all branches, and displays it in a graphic representation.
git log --all --graph
