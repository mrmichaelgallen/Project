C:\Users\Michael\Documents\GitHub\gitproject

git commandline instructions...

To initialize a project in a folder

	git init <project>     // Project is now a repository

Show current items at location

	ls

Status: (Status of files)

	git status

Log: (committ history)	

	git log

To add to commit pending:

	git add .

	or

	git add filename.text

To commit: (snapshot of file)

	git commit -m "type your message about the changes here"


To add and committ at the same time:

	git commit -a -m "message here"


To the differences of files before commit: (view differences within a file)

	git diff

To see the difference of files after commit: (differences in staging)

	git diff --cached

To see oneline of updates:

	git log --oneline

To get what has been modified in short hand:

	git status -s

To see the branches:

	git branch

To create a new branch:

	git brand 'r2_index'

To clone a repository:

	git clone <past ssh link from GitHub>

To switch between branches:

	git checkout <name of branch you want to go to>

To push:

	git push github <name of branch you want sent to GitHub>

To merge:

	git merge master (the one you want to merge)

If you get stuck use shift + zz to release from text

To Pull - moves code from remote repository with a local repository:

	git pull github <name of branch to pull from>

Always to a Pull before a Push to minimize conflicts so you can resolve conflicts locally.
