
# Linux Cheat Sheet (concise)

## File & Directory Operations
```bash
ls -l        # long listing
ls -ltr      # sort by time, reverse order
ls -a        # show hidden files
cd /path     # change directory
pwd          # print current directory
mkdir dir    # create directory
rm file      # remove file
rm -rf dir   # remove directory recursively
cp src dst   # copy file
cp -r src dst# copy directory recursively
mv src dst   # move or rename
```

## Permissions & Ownership
```bash
chmod 755 file      # set permissions
chmod -R 644 dir    # recursive permissions
chown user file     # change owner
chown user:group f  # change owner and group
```

## User Management
```bash
whoami              # current user
id                  # user info
adduser username    # add user
passwd username     # set password
su - username       # switch user
```

## Search & Find
```bash
grep "pattern" file       # search in file
grep -r "pattern" dir      # recursive search
find /path -name "file"    # find by name
find /path -type f -size +10M # find files >10MB
```

## File Viewing
```bash
cat file            # view file
less file           # view with scroll
head -n 10 file     # first 10 lines
tail -n 10 file     # last 10 lines
tail -f file        # follow file updates
```

## Compression & Archiving
```bash
tar -cvf file.tar dir    # create tar
tar -xvf file.tar        # extract tar
gzip file                # compress file
gunzip file.gz           # decompress
zip file.zip file        # zip file
unzip file.zip           # unzip
```

## Networking
```bash
ping host               # check connectivity
curl url                # fetch URL
wget url                # download file
ssh user@host           # connect via SSH
scp file user@host:/path# copy via SSH
```

## System Monitoring
```bash
ps aux                 # list processes
top                    # live process view
htop                   # interactive process view
df -h                  # disk usage
du -sh dir             # directory size
free -m                # memory usage
uptime                 # system uptime
```

## Package Management (Debian/Ubuntu)
```bash
apt update && apt upgrade   # update system
apt install pkg             # install package
apt remove pkg              # remove package
```

## Miscellaneous
```bash
alias ll="ls -ltr"          # create alias
history                     # show command history
clear                       # clear terminal
```



---
[⬅ Back to Cheat Sheet Index](CHEATSHEET_INDEX.md)


