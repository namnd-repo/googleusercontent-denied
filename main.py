import argparse

parser = argparse.ArgumentParser(description="Convert 'googleusercontent denied' url to an accessible one")
# parser.add_argument("url", type=str, help="URL at the denied page")
# args = parser.parse_args()

"""
If the url has "&" in it, command prompt will split the url into 2 commands. So parse_args() won't work properly.
"""
# def convert(url):
#     new_url = "https://drive.google.com/uc?id=" + url[url.rfind("/")+1:url.find("?")]
#     return new_url

def convert():
    url = input("Enter the url at denied page: ")
    new_url = "https://drive.google.com/uc?id=" + url[url.rfind("/")+1:url.find("?")]
    print("\nHere is your url: " + new_url + "\n")

if __name__ == "__main__":
    convert()
    input("Press any key to exit")

