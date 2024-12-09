from django import template
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

# Register the template library
register = template.Library()

@register.filter
def truncate_words(value, arg):
    """
    Truncate a string to a certain number of words. Removes HTML tags for safety.
    Usage: {{ value|truncate_words:10 }}
    """
    try:
        arg = int(arg)
    except ValueError:
        return value  # Return the original value if arg is not an integer

    if not value:
        return ''

    # Remove HTML tags and split the string into words
    words = strip_tags(value).split()
    if len(words) > arg:
        return ' '.join(words[:arg]) + '...'  # Truncate and append ellipsis
    return value

@register.filter
def truncatewords_html(value, arg):
    """
    Truncate a string containing HTML to a certain number of words.
    Preserves the HTML structure.
    Usage: {{ value|truncatewords_html:10 }}
    """
    try:
        from bs4 import BeautifulSoup  # Import BeautifulSoup dynamically to handle missing imports
    except ImportError:
        return truncate_words(value, arg)  # Fallback if BeautifulSoup is unavailable

    try:
        arg = int(arg)
    except ValueError:
        return value  # Return the original value if arg is not an integer

    if not value:
        return ''

    # Parse HTML and truncate words while preserving HTML structure
    soup = BeautifulSoup(value, 'html.parser')
    word_count = 0

    for element in soup.recursiveChildGenerator():
        if element.string:  # Process text nodes only
            element_words = element.string.split()
            remaining_words = arg - word_count
            if word_count >= arg:
                element.extract()  # Remove elements beyond the word limit
            elif len(element_words) > remaining_words:
                element.string = ' '.join(element_words[:remaining_words]) + '...'  # Truncate text
                word_count += remaining_words
            else:
                word_count += len(element_words)

    return mark_safe(str(soup))  # Return the modified HTML as safe

@register.filter
def format_date(value):
    """
    Format a date into 'Month Day, Year' format.
    Usage: {{ value|format_date }}
    """
    if not value:
        return ''
    try:
        return value.strftime('%B %d, %Y')  # Format the date
    except AttributeError:
        return value  # Return the original value if it's not a date

@register.filter
def strip_html(value):
    """
    Remove all HTML tags from a string.
    Usage: {{ value|strip_html }}
    """
    return strip_tags(value) if value else ''
