# Git Cheat Sheet (concise)

## Setup (once per machine)
```bash
git config --global user.name "<Your Name>"
git config --global user.email "<your-email>@example.com"
git config --global init.defaultBranch main
```

## Create / Clone
```bash
git init                      # start new repo in current folder
git clone <repo-url>          # copy remote repo locally
cd <repo>
```

## Daily Workflow
```bash
git status                    # what changed
git add .                     # stage all changes
git commit -m "msg"           # save snapshot

git remote add origin <url>   # link to GitHub (first time)
git push -u origin main       # push first time (sets upstream)
git pull                      # get latest from remote
```

## Inspect Changes & History
```bash
git log --oneline --graph --decorate   # nice history
git show <commit>                      # details of a commit
git diff                               # unstaged changes
git diff --staged                      # staged changes
```

## Branching & Merging
```bash
git branch                             # list branches
git switch -c feature-x                # create & switch
git switch main                        # go back to main
git merge feature-x                    # merge to current branch
git branch -d feature-x                # delete merged branch
```

## Stash (save work-in-progress)
```bash
git stash               # stash changes
git stash list          # see stashes
git stash pop           # re-apply latest and remove it
```

## Undo / Fix
```bash
git restore <file>              # discard local changes in file
git restore --staged <file>     # unstage file

git reset --soft HEAD~1         # undo last commit, keep changes staged
git reset --mixed HEAD~1        # undo last commit, keep changes unstaged
git reset --hard HEAD~1         # ⚠️ discard commit & changes

git revert <commit>             # make a commit that undoes <commit>
```

## Remote Management
```bash
git remote -v                   # show remotes
git remote add origin <url>     # add remote
git remote set-url origin <url> # change remote URL
```

## Tags & Releases
```bash
git tag -a v0.1 -m "first tag"  # create annotated tag
git push --tags                 # push all tags
```

## .gitignore (common Python)
```
venv/
__pycache__/
*.pyc
.env
.DS_Store
```

## Clean untracked files (use with care)
```bash
git clean -fdx   # ⚠️ removes ALL untracked files/folders
```

## Resolve Merge Conflicts (quick)
1) Open conflicted files, decide correct code.
2) Stage fixed files: `git add <file>`
3) Commit merge: `git commit`

## GitHub PR (short)
```bash
git switch -c feature-x
# commit your work
git push -u origin feature-x
```
Open a Pull Request on GitHub → review → merge.

### GitHub CLI (optional)
```bash
gh auth login
gh pr create -f -B main -t "title" -b "desc"
gh pr status
```

---
**Tips**: Commit small, pull often; write clear messages; use branches for features.
