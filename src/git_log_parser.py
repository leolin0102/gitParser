import git
import re

def git_log():
    g = git.Git('/Users/leo/dev/Larks/major/ios-client')
    return g.log('--stat', '--since=2018-03-11')


def parse_log():
    items = []
    logs = git_log().splitlines(True)
    for l in logs:
        result = parse_commit(l, None)
        if result is not None:
            pass
        else:
            pass


def add_commit_id(change_log_item, commit_id):
    pass


def parse_commit(line, detailParser):
    result = re.match("commit .*", line)
    return result


def parse_commit_file(line):
    pass


parse_log()

