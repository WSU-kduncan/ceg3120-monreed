**status** - Shows status of the local repository. This status includes:
1. number of local commits that have not been synced with remote (GitHub)
2.  list of files in local folder than are NOT being tracked by git
3.  list of files in local folder that have changes that need to be committed 
<!-- -->

	> git status 

**clone** - Used to 'copy' a GitHub repository into your personal terminal system so that file or folder insertion/deletion/edits can and will be tracked and published to the original repository on GitHub.com. 

	> git clone <https://github.com/repository>  

**add** - Used to prepare newly created or edited files/folders for tracking in your original Github.com repository. Does not actually commit the updates, but rather, tells your repository that you are planning on committing the changes you've made.  

	> git add <file/folder name>

**rm** - Used to remove a file or folder from both your original GitHub repository and your personal filesystem clone. 

	> git rm <file/folder name>

**commit** - Used to solidify any and all edits/insertions/deletions that have been staged for tracking in your personal filesystem repository.  

	> git commit 

**push** - Used to actually publish the committed changes from your personal filesystem to your original GitHub repository. 

	> git push 

**fetch** - Used to gather any commits within your remote GitHub repository that don't already exist within your local filesystem. These changes are stored in your local clone, but are not yet merged with it. 

	> git fetch 

**merge** - Used to unify all sequences of commits into one updated 'checkpoint' and apply the changes that were simply waiting in your local system after git fetch is executed. 

	> git merge 

**pull** - Used to execute both git fetch and git merge in one step. Since this is immediately applying fetched changes, you should be certain of your changes.

	> git pull 

**branch** - Used to create/delete/edit branches, which are independent workspaces aside from your 'main' branch. 

	> git branch -a (List all branches)
	> git branch <Name> (Create branch with name 'Name')
	> git branch -d <Name> (Delete branch 'Name')
	
 

**checkout** - Used to switch between which branch/working directory you are operating in. Also serves to update the main working directory with the code that was created or modified in a separate branch. Basically, once you're certain the new code won't break everything, you use `git checkout` to apply the changes. 

	> git checkout <Name> (Switch to branch 'Name')
	> git checkout -b <Name> (Create new branch and immediately switch to it)
	> git checkout -b <New_Branch> <Old_Branch> (Create new branch 'New_Branch' but base it off of existing branch 'Old_Branch')

**.git folder** - A folder present in any GitHub repository that allows the user to see all of the information about the project/repository and all commit information and history. 
**.gitignore file** - This command is used to tell GitHub which files or directories you want to ignore so far as tracking goes. Basically, they'll be present on your local filesystem but not be included when it comes to commits and pushes to the main repository. 

**Pull requests** - A pull request is a way to start discussion when a member on a project team is ready to apply new changes to a repository or alert the others on your team when you have pushed new changes to a branch in said repository. 

**SSH authentication to repositories** - Includes generating a key on your local filesystem and adding that key to your SSH and GPG keys section in your GitHub settings so that you are authorized access to clone repositories on that system. Command to create key:

	> ssh-keygen -t ed25519 -C "user@email.com"
 
	
