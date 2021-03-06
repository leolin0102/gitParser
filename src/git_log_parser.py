import git
import re

def git_log():
    g = git.Git('/Users/leo/dev/Larks/major/ios-client')
    return g.log('--stat', '--since=2018-03-11')


def parse_log():
    items = []
    log_item = None
    logs = git_log().splitlines(True)
    for l in logs:
        result = parse_commit(l)
        if result is not None:
            if log_item is not None:
                items.append(log_item)
            log_item = {'commit': result.group(1)}
        else:
            add_commit_file(log_item, parse_commit_file(l))

    return items


def add_commit_id(change_log_item, commit_id):
    pass


def parse_commit(line):
    result = re.match("commit (.*)", line)
    return result


def parse_commit_file(line):
    result = re.match("(.*.swift) \| \d* .*", line)
    if result is not None:
        return result.group(1)
    else:
        return None


def add_commit_file(item, file_path):
    if file_path is None:
        return
    if 'files' not in item.keys():
        item['files'] = []

    item['files'].append(file_path)

items = parse_log()
print(items)

