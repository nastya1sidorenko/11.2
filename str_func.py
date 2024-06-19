def capitalize_string(input_string):
    return input_string.upper()
def capitalize_words(input_string):
    """
    Преобразует первую букву каждого слова во входной строке в верхний регистр.

    Args:
        input_string (str): Входная строка, содержащая слова.

    Returns:
        str: Строка с заглавными первыми буквами слов.
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)