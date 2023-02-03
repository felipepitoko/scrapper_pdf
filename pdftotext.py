import requests
from bs4 import BeautifulSoup

def extract_text_from_pdf(pdf_file):
    # Upload the PDF file to the website
    with open(pdf_file, 'rb') as f:
        response = requests.post('https://pdftotext.com/pt/', files={'file': f})
        print(response)
    
    # Parse the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the processed text from the response
    text = soup.find('textarea', {'id': 'text'}).text

    return text

# Example usage
if __name__ == '__main__':
    pdf_file = 'ipca.pdf'
    text = extract_text_from_pdf(pdf_file)
    print(text)