import re

def extract_phone_numbers(string):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phone_numbers = re.findall(pattern, string)
    return phone_numbers

def extract_email_addresses(string):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_addresses = re.findall(pattern, string)
    return email_addresses

def replace_email_addresses(string, replacement):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    replaced_string = re.sub(pattern, replacement, string)
    return replaced_string

# test cases below
string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"
assert extract_phone_numbers(string) == ['(123) 456-7890', '(111) 222-3333']
print("Phone numbers extracted: ", extract_phone_numbers(string))
assert extract_email_addresses(string) == ['info@example.com']
print("Email addresses extracted: ", extract_email_addresses(string))
assert replace_email_addresses(string, "REPLACED") == "Please contact REPLACED for assistance. Phone: (123) 456-7890 or (111) 222-3333"
print("Email addresses replaced: ", replace_email_addresses(string, "REPLACED"))
