import requests
from datetime import datetime, timedelta

def fetch_and_write_url_content(url, output_file):
    """Fetch content from a URL and write it to a file."""
    try:
        # Fetch the data from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Write the content to the file
        with open(output_file, 'a', encoding='utf-8') as file:
            # file.write(f"--- Data from {url} ---\n")
            file.write(response.text + "\n")
        
        print(f"Content successfully written to '{output_file}'")
    
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")

def generate_date_urls(start_date, end_date):
    """Generate sitemap URLs for each day in the date range."""
    urls = []
    current_date = start_date
    while current_date <= end_date:
        formatted_date = current_date.strftime('%Y/%m/%d/')
        url = f'https://www.nytimes.com/sitemap/{formatted_date}'
        urls.append(url)
        current_date += timedelta(days=1)
    return urls

def main(start_date_str, end_date_str, output_file):
    """Fetch data from the NYT sitemap for a range of dates and write to a file."""
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    # Generate URLs
    urls = generate_date_urls(start_date, end_date)
    
    # Fetch and write data from each URL
    for url in urls:
        fetch_and_write_url_content(url, output_file)

# Define the start and end dates
start_date_str = '2010-12-01'
end_date_str = datetime.now().strftime('%Y-%m-%d')  # Today’s date

# Output file
output_file = 'newtime.txt'

# Run the main function
main(start_date_str, end_date_str, output_file)
