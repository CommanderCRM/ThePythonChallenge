import string


# making the translation table (shift by 2 to the right)
def shift_letters(shift):
  lowercase_letters = string.ascii_lowercase
  shifted_letters = lowercase_letters[shift:] + lowercase_letters[:shift]
  return str.maketrans(lowercase_letters, shifted_letters)


# deciphering
shift = 2
translation_table = shift_letters(shift)
modified_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
original_string = modified_string.translate(translation_table)

print(original_string)
