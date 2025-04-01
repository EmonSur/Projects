#!/bin/sh

set -e
set -x

HERE=${PWD}
EXAMPLE=${HERE}/example
PROJECT=project
SHARED=shared
LOCAL=local
ANN=ann
BOB=bob
EVE=eve
RAY=ray
EMON=emon
REPO=${EXAMPLE}/${ANN}/${SHARED}/${PROJECT}

rm -rf ${EXAMPLE}

ann_local( ) {
    cd ${EXAMPLE}/${ANN}/${LOCAL}
    sh -c "$1" # sh runs a new shell instance, -c tells to execute command as a string
}

ann_shared( ) {
    cd ${REPO}
    sh -c "$1"
}

ann_project( ) {
    cd ${EXAMPLE}/${ANN}/${LOCAL}/${PROJECT}
    sh -c "$1"
}

bob_local( ) {
    cd ${EXAMPLE}/${BOB}/${LOCAL}
    sh -c "$1"
}

eve_local( ) {
    cd ${EXAMPLE}/${EVE}/${LOCAL}
    sh -c "$1"
}

ray_local( ) {
    cd ${EXAMPLE}/${RAY}/${LOCAL}
    sh -c "$1"
}

emon_local( ) {
    cd ${EXAMPLE}/${EMON}/${LOCAL}
    sh -c "$1"
}

create_bare_repository( ) {
    mkdir ${REPO} -p

    for USR in ${ANN} ${BOB} ${EVE} ${RAY} ${EMON}; do
        mkdir ${EXAMPLE}/${USR}/${LOCAL} -p
    done
    ann_shared 'git init --bare --shared'
}

Ann_local_git_repo(){
    ann_local   "mkdir ${PROJECT}"
    ann_project 'git init'
}

Ann_config(){
	ann_project 'git config --local user.name Ann'
	ann_project 'git config --local user.email 11111@CS3306.ucc'
}

populate_bare_repository( ) {
    ann_project 'cat > ProjectLog.txt <<EOF
This is a project that implements a calculator.

Tasks:
Ann: Division class and calculator.py script 
Eve: Adder class
Bob: Subtractor class
Ray: Multiplier class
Emon: examine and merge
EOF'
    ann_project "git add ProjectLog.txt"
    ann_project "git commit -am 'Initial commit'"
    ann_project "git remote add origin file://${REPO}"
    ann_project 'git push --set-upstream origin master'
}

clone_repository( ) {
    bob_local   "git clone ${REPO}"
    eve_local   "git clone ${REPO}"
    ray_local   "git clone ${REPO}"
    emon_local  "git clone ${REPO}"
}


# Ann sets up shared repository.
create_bare_repository

# Ann sets up local git repository.
Ann_local_git_repo

# Ann performs local configuration
Ann_config

# Ann populates the bare repository
populate_bare_repository

# Others clone the shared repository
clone_repository

# Configure local git settings for others
local_git_configuration() {
    USER=$1
    NAME=$2
    EMAIL=$3

    cd ${EXAMPLE}/${USER}/${LOCAL}/${PROJECT}
    git config --local user.name "${NAME}"
    git config --local user.email "${EMAIL}"
}

# Set git configurations for others
local_git_configuration ${BOB} "bob" "22222@CS3306@gmail.com"
local_git_configuration ${EVE} "eve" "33333@CS3306@gmail.com"
local_git_configuration ${RAY} "ray" "44444@CS3306@gmail.com"
local_git_configuration ${EMON} "emon" "121367643@CS3306@gmail.com"

# Ann creates Divider class and divider branch
create_divider_branch() {
    # (cd into respository instead of using ann_project "git checkout -b divider" to prevent uncessarily long terminal messages) 
    cd ${EXAMPLE}/${ANN}/${LOCAL}/${PROJECT}
    
    # Ann creates divider branch
    git checkout -b divider

    cat > divider.py <<EOF
class Divider:
    def __init__(self):
        self.result = 0
    def divide(self, a, b):
        if a % b == 0:
            self.result = a // b
        else:
            self.result = a / b
    def display(self):
        print(int(self.result) if isinstance(self.result, int) else round(self.result, 2))
EOF

    # Ann adds divider.py to branch
    git add divider.py

    # Ann commits changes to branch
    git commit -m "Created divider.py class"
    
    # Ann pushes updated divisor branch
    git push origin divider
}

# Eve creates Adder class and adder branch
create_adder_branch() {
    cd ${EXAMPLE}/${EVE}/${LOCAL}/${PROJECT}

    # Eve creates create adder branch
    git checkout -b adder

    cat > adder.py <<EOF
class Adder:
    def __init__(self):
        self.result = 0
    def add(self, a, b):
        self.result = a + b
    def display(self):
        print(int(self.result) if isinstance(self.result, int) else round(self.result, 2))
EOF

    # Eve adds adder.py to branch
    git add adder.py

    # Eve commits changes to branch
    git commit -m "Created adder.py class"

    # Eve pushes updated adder branch
    git push origin adder
}

# Bob creates Subtractor class and subtractor branch
create_subtractor_branch() {
    cd ${EXAMPLE}/${BOB}/${LOCAL}/${PROJECT}

    # Bob creates subtractor branch
    git checkout -b subtractor

    cat > subtractor.py <<EOF
class Subtractor:
    def __init__(self):
        self.result = 0
    def subtract(self, a, b):
        self.result = a - b
    def display(self):
        print(int(self.result) if isinstance(self.result, int) else round(self.result, 2))
EOF

    # Bob adds subtractor.py to branch
    git add subtractor.py

    # Bob commits changes to branch
    git commit -m "Created subtractor.py class"

    # Bob pushes updated subtractor branch
    git push origin subtractor
}

# Ray creates Multiplier class and multiplier branch
create_multiplier_branch() {
    cd ${EXAMPLE}/${RAY}/${LOCAL}/${PROJECT}
    
    # Ray creates multiplier branch
    git checkout -b multiplier

    cat > multiplier.py <<EOF
class Multiplier:
    def __init__(self):
        self.result = 0
    def multiply(self, a, b):
        self.result = a * b
    def display(self):
        print(int(self.result) if isinstance(self.result, int) else round(self.result, 2))
EOF

    # Ray adds multiplier.py to branch
    git add multiplier.py
    
    # Ray commits changes to branch
    git commit -m "Created multplier.py class"

    # Ray pushes updated multiplier branch
    git push origin multiplier
}

# Create and push all branches
create_divider_branch
create_adder_branch
create_subtractor_branch
create_multiplier_branch

# Ann merges all branches into master
ann_merge_branches() {
    cd ${EXAMPLE}/${ANN}/${LOCAL}/${PROJECT}

    # Ann moves to master branch
    git checkout master

    # Ann fetches latest changes from origin
    git fetch origin

    # Ann merge branches
    git merge origin/divider --no-edit
    git merge origin/adder --no-edit
    git merge origin/subtractor --no-edit
    git merge origin/multiplier --no-edit

    # Ann pushes updated master branch
    git push origin master
}

# Ann merges the branches into master
ann_merge_branches

# Ann creates calculator class
create_calculator_branch(){
    cd ${EXAMPLE}/${ANN}/${LOCAL}/${PROJECT}

    # Ann creates calculator branch
    git checkout -b calculator

    cat > calculator.py << EOF
from adder import Adder
from subtractor import Subtractor
from multiplier import Multiplier
from divider import Divider # Import the new Divider class

# Example Usage
calculator_adder = Adder()
calculator_adder.add(13, 6)
calculator_adder.display() # Adder outputs: 19

calculator_subtractor = Subtractor()
calculator_subtractor.subtract(12, 7)
calculator_subtractor.display() # Subtractor outputs: 5

calculator_multiplier = Multiplier()
calculator_multiplier.multiply(6, 5)
calculator_multiplier.display() # Adder outputs: 30

calculator_divider = Divider()
calculator_divider.divide(20, 4)
calculator_divider.display() # Divider outputs: 5
EOF

    # Ann adds calculator.py to branch
    git add calculator.py

    # Ann commits changes to branch
    git commit -m "Added calculator.py class"
    git branch

    # Ann pushes updated calculator branch
    git push origin calculator
}

# Create and push calculator branch
create_calculator_branch

# Emon reviews and merges calculator branch
review_and_merge_calculator(){
    cd ${EXAMPLE}/${EMON}/${LOCAL}/${PROJECT}

    # Emon fetches latest changes from origin
    git fetch origin

    # Emon changes to calculator branch to review it
    git checkout calculator

    # Emon checks if calculator code works as expected
    python3 calculator.py

    # Emon displays visual representation of commit history
    git log --oneline --graph --decorate --all

    # Emon shows status of current directory
    git status

    # Emon moves to master branch before merging
    git checkout master

    # Emon merges without new commit message
    git merge calculator --no-edit

    # Emon pushes updated master branch
    git push origin master   
    echo "Running calculator..."
}

review_and_merge_calculator

# Emon appends concluding remarks to project log
append_concluding_remarks(){
    cd ${EXAMPLE}/${EMON}/${LOCAL}/${PROJECT}

    echo "All the Python files were created successfully." >> ProjectLog.txt
    echo "All the calculator operations are working fine." >> ProjectLog.txt
    echo "The project has been successfully completed." >> ProjectLog.txt

    # Emon adds ProjectLog.txt to branch
    git add ProjectLog.txt

    # Emon checks if content of ProjectLog.txt is correct
    cat ProjectLog.txt

    # Emon commits changes to branch
    git commit -m "Added concluding remarks to Projectlog.txt"

    # Emon pushes updated master branch
    git push origin master
}

append_concluding_remarks

# Emon uploads calculator 
publish_calculator() {
    cd ${EXAMPLE}/${EMON}/${LOCAL}/${PROJECT}

    # Emon ensures is on the master branch
    git checkout master

    # Emon pushes the updated master branch to origin
    git push origin master

    # Emon pushes the updated master branch to origin
    git push origin master

    echo "Calculator has been published successfully!"
}


# Emon pushes the updated master branch to origin
publish_calculator

remove_stale_branches() {
    USER=$1
    cd ${EXAMPLE}/${USER}/${LOCAL}/${PROJECT}

    # Move to master branch
    git checkout master

    # Fetch the latest updates from origin
    git fetch --prune

    # Delete all development branches locally
    for BRANCH in divider adder subtractor multiplier calculator; do
	git branch
        git branch -D $BRANCH 2>/dev/null || true

    done
}

# Remove stale local branches for all team members
for user in ${ANN} ${BOB} ${EVE} ${RAY} ${EMON}; do
    remove_stale_branches $user
done


final_inspection() {
    USER=$1
    cd ${EXAMPLE}/${USER}/${LOCAL}/${PROJECT}

    # User fetches the latest changes from origin
    git fetch origin

    # User retrieves latest changes from branch
    git pull

    # User ensures the user is on the master branch
    git checkout master

    python3 calculator.py

    # User reset master to match the latest origin/master
    git reset --hard origin/master

    # User displays commit history graph
    git log --oneline --graph
}

# Eve and Bob perform final inspection
final_inspection ${EVE}
final_inspection ${BOB}