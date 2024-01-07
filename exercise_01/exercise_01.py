def formatNumber(number: float, format_digit: str = "fr", decimal_places: int = 2, rounding: bool = False) -> str:
    """
    Converts a decimal number to a commercial number string with customizable formatting.

    Args:
        number (float): The decimal number to be formatted.
        format_digit (str, optional): The digit format to use, either "en" for English or "fr" for French. Default is "fr".
        decimal_places (int, optional): The number of decimal places in the formatted result. Default is 2.
        rounding (bool, optional): Indicates whether to round the result. Default is False.

    Returns:
        str: The formatted commercial number as a string.
    """
    formatted_number:str = ""
    
    # get the appropriate separator and formatter depending on the format_digit
    separator = ""; formatter = ""
    if format_digit == "en":
        separator = "."
        formatter = ","
    elif format_digit == "fr":
        separator = ","
        formatter = "."
    else:
        raise ValueError("Invalid format digit: %s - expect 'en' or 'fr'." % format_digit)
    
    # declare new_number to store the number in string format, and round the value if necessary
    new_number:str = str(number)
    if rounding:
        new_number = str(round(number, decimal_places))
    
    # separate the integer and decimal parts from the new_number
    new_number_list:list[str] = new_number.split('.')  
    integer_part:str = new_number_list[0]; decimal_part:str = new_number_list[1][:decimal_places]
    integer_part_list:list[str] = [val for val in integer_part]
    
    # insert the separator between the integer part
    for i in range(len(integer_part)-3, 0, -3):
        integer_part_list.insert(i, formatter)

    # add zero after the decimal part if it length is lower than the decimal places
    zeros_after = decimal_places - len(decimal_part)
    for i in range(zeros_after):
        decimal_part += "0"
        
    formatted_number = "".join(integer_part_list) + separator + decimal_part
    
    return formatted_number

