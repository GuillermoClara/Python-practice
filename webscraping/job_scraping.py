from bs4 import BeautifulSoup
import requests

# Program that scrapes information about
# jobs related to a topic of the users interest
# Data scraped from: www.timesjobs.com


def find_jobs(interest):
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=%interest%&txtLocation='
    url = url.replace('%interest%', interest)  # Replace placeholder with user input
    html_text = requests.get(url).text      # We obtain the contents of the html

    soup = BeautifulSoup(html_text, 'html.parser')  # Instance of BS object

    # Find all ocurrences of tag li with specified class name
    jobs = soup.findAll('li', class_='clearfix job-bx wht-shd-bx')
    if len(jobs) < 1:
        print('No jobs related to {} were found :( !'.format(interest.replace('+', ' ')))
        return

    print('Recent Jobs related to ' + interest.replace('+', ' ') + ": ")
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text.strip()  # .text represents the text in a tag

        # We include only the most recent published jobs
        if 'few' not in published_date and 'today' not in published_date:
            continue

        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills_required = job.find('span', class_='srp-skills').text.replace(' ', '').strip()

        # Specific to the used website, the tab with location data is the last sibling of the first li element
        location = job.find('ul', class_='top-jd-dtl clearfix').li.find_next_siblings('li')[-1].span.text

        # We can get different elements of a tag with [name]
        more_info = job.find('h2').a['href'].strip()

        print('========================')
        print()
        print('Position name: ')
        print('Company: ' + company_name)
        print('Location: ' + location)
        print('Skills required: {}'.format(skills_required))
        print('Published: {}'.format(published_date))
        print('Interested? Click me!: {}'.format(more_info))
        print()


user_interest = input('Enter interest of job: ')
user_interest = user_interest.strip()             # Eliminate leading and trailing spaces
user_interest = user_interest.replace(' ', '+')  # Search engine interpets spaces as '+'
find_jobs(user_interest)
