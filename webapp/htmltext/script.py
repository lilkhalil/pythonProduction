import re
import requests
import html


def format_html(str):
    regex = r"<(script|style|svg|noscript|preload|global-message).*?>.*?<\/\1>|<(link|meta|img|!--.*?--).*?>" # Unnecessary tags needs to be removed
    
    page = re.sub(regex, '', str, flags=re.DOTALL) # Delete unnecessary tags

    page = page.replace('\n', '') # HTML to raw format
    page = page.replace('\t', '')
    page = page.replace('\r', '')
    return html.unescape(page)


def find_text(str):
    regex = r">([^>]+?)<"
    return [text for text in re.findall(regex, str) if text.strip()]

def gettext(url):
    html = requests.get(url).text

    page = format_html(html)

    text = find_text(page)

    dictionary = {}
    dictionary['url'] = url
    dictionary['value'] = text # Prepare dictionary for JSON returns


    return dictionary


if __name__ == '__main__':
    gettext()