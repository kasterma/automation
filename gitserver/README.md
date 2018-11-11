# Use

The script `create_local_repo.sh` is intended to be added to your ~/bin to create a new repo in the container and
set the remote `local` for the current repo to that new repo.  Execute

    create_local_repo.sh <repo_name>

with `<repo_name>` e.g. gitrepo.git to execute this.

# TODO

1. the create_repo script is not yet working well inside the container.  This means that now create_local_repo.sh
   uses a docker exec command; would prefer that to be an ssh or git command.
2. persistence with use of volume.

# Notes

on gitserver
    ssh-keygen -A
    passwd -u git
    /usr/sbin/sshd -D -e

on gitclient

    echo -e "$PRIVKEY" > .ssh/id_rsa
    chown -R git:git .ssh
    chmod 600 .ssh/id_rsa
    su git
    ssh git@gitserver
    
    
On localhost can now log in with:

    ssh git@localhost -p 2222 -vvv -i rsatestkey   # disabled by changing shell
    
    ssh-add rsatestkey
    
    git remote add local ssh://git@localhost:2222/home/git/test/
     