import git


def git_log():
    g = git.Git('/Users/leo/dev/Larks/major/ios-client')
    return g.log('--stat', '--since=2018-03-11')


def add_commit_id(change_log_item, commit_id):
    pass


print(git_log())

