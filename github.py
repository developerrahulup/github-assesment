import datetime
import requests
import smtplib
from email.mime.text import MIMEText

def get_pull_requests(repo_url):

    today = datetime.date.today()
    last_week = today - datetime.timedelta(days=7)

    # Construct the URL to fetch the pull requests
    url = repo_url
    params = {
        'state': 'all',
        'direction': 'desc',
        'sort': 'updated',
        'since': last_week.isoformat()
    }

    # Send GET request to the GitHub API
    response = requests.get(url, params=params)
    pull_requests = response.json()

    return pull_requests

## AS not having smtp . I am printing the content

def send_email(sender, recipient, subject, body):
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    smtp_username = 'your_smtp_username'
    smtp_password = 'your_smtp_password'

    # Create email message
    msg = MIMEText(body)
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject


def generate_email_content(pull_requests):
    content = 'Summary of Pull Requests in the Last Week:\n\n'
    for pr in pull_requests:
        if isinstance(pr, dict) and 'title' in pr:
            content += f'- Title: {pr["title"]}\n'
            content += f'  State: {pr["state"]}\n'
            content += f'  Created By: {pr["user"]["login"]}\n'
            content += f'  Created At: {pr["created_at"]}\n\n'
    print (content)
    return content

# GitHub repository URL
repository_url = 'https://api.github.com/repos/linuxacademy/cicd-pipeline-train-schedule-git/pulls'

# Retrieve pull requests from the GitHub API
pull_requests = get_pull_requests(repository_url)

# Generate email content
email_content = generate_email_content(pull_requests)

# Email details
sender = 'sender@example.com'
recipient = 'recipient@example.com'
subject = 'Summary of Pull Requests in the Last Week'
