from urllib.parse import urlparse   #module import

def detect_phishing(url):      #define phishing detection function
    parsed_url = urlparse(url)
    if 'login' in parsed_url.path or 'verify' in parsed_url.path:
        return True
    return False

test_url = "http://phishing-example.com/login"   #website to test
print(f"Phishing Detected: {detect_phishing(test_url)}")