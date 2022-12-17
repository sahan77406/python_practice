
from jira import JIRA
import sys
import maskpass
import base64

jiraOptions = {'server': "https://xxxxxxxxxxxxxx.com/"}

username = input("Enter username: ")
password = maskpass.askpass("Enter password : ")
encpwd = base64.b64encode(password.encode("utf-8"))
date = input("Enter a date formatted as YYYY-MM-DD: ")

jira = JIRA(options=jiraOptions, basic_auth=(
    username, password))

file_path = 'Jira Report 1.txt'
File = sys.stdout = open(file_path, "w")

for singleIssue in jira.search_issues(jql_str='project = CISAMTSTAUTO AND created>=' + date):
    print('{}{}{}{}{}{}'.format(50*'=', '\nKey: ' + singleIssue.key, '\nSummary: ' + singleIssue.fields.summary,
                                '\nReporter: ' + singleIssue.fields.reporter.displayName, '\nStatus: ' +
                                singleIssue.fields.status.name,
                                '\nUpdate Date: ' + singleIssue.fields.updated[0:10]))
    if (singleIssue.fields.assignee is None):
        print('Assignee: None')
    else:
        print('Assignee: ' + singleIssue.fields.assignee.displayName)
