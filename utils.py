from voices import language

def get_language_code(language_name):
    """
    Get the language code for a given language name.
    """
    # Use a dictionary instead of switch
    language_map = {
        'american english': 'a',
        'british english': 'b',
        'mandarin chinese': 'z',
        'spanish': 'e',
        'japanese': 'j',
        'french': 'f',
        'hindi': 'h',
        'italian': 'i',
        'brazilian portuguese': 'p',
        # Add other languages as needed
    }
    
    # Return the code if found, otherwise return a default
    return language_map.get(language_name.lower(), 'a')