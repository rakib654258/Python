letters = {'A':'D','B':'E','C':'F','D':'G','E':'H','F':'I','G':'J','H':'K','I':'L',
           'J':'M','K':'N','L':'O','M':'P','N':'Q','O':'R','P':'S','Q':'T','R':'U',
           'S':'V','T':'W','U':'X','V':'Y','W':'Z','X':'A','Y':'B','Z':'C'}
message = input('Enter your message').upper()
encrypted = ""

for letter in message:
    if letter.upper() in letters:
        encrypted += letters[letter]
    else:
        encrypted += letter
print(encrypted)
