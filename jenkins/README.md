# Jenkins

working with a throw away repo `/Users/kasterma/tmp/gittest/AAA`

Add Jenkinsfile

    pipeline {
        agent any
    
        stages {
            stage('echo') {
                steps {
                    sh "echo hi"
    
                }
            }
        }
    }
    
to the repo add a post-commit hook (that you must make executable)

    echo "trigger jenkins"
    curl --user kasterma:XXXXXXXXX  http://localhost:8080/git/notifyCommit?url=/AAA

Then create multibranch pipeline with ref to the repo `/AAA` (where we mounted the repo).  Note: polling the repo
must be turned on.

Q: in the git console we see

    trigger jenkins
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
    100    78  100    78    0     0     78      0  0:00:01 --:--:--  0:00:01   276
    No git jobs using repository: /AAA and branches: 
    Scheduled indexing of test1

why is there the message about no git repos.

Note Jenkins also gives a stacktracke with root:

    org.kohsuke.stapler.NoStaplerConstructorException: There's no @DataBoundConstructor on any constructor of class jenkins.plugins.git.GitSCMSourceDefaults
