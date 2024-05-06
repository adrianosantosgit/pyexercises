websites = ['google.com', 'youtube.com', 'apple.com']

def auto_add_https(site):
    return "https://" + site

auto_add = [auto_add_https(site) for site in websites]

print(auto_add)