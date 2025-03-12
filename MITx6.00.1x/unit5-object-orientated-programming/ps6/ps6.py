import string
from os import getcwd, path

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    fpath = path.join(getcwd(), "unit5-object-orientated-programming/ps6", file_name)
    in_file = open(fpath, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(r" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # build the shift dict
        shift_dict = {}

        # make string.ascii_lowercase more pleasant to type
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase

        # enumerate over the lowercases
        for i, x in enumerate(lc):
            # build the shift index
            shift_index = (i + shift) % 26 # ensures we remain in confines of alphabet 

            # now assign to shift dict
            shift_dict[x] = lc[shift_index]

        for i, x in enumerate(uc):
            # build the shift index
            shift_index = ((i + shift) % 26)  # insert above lower case 

            # now assign to shift dict
            shift_dict[x] = uc[shift_index]
        
        # le done
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # get the shift dict
        shift_dict = self.build_shift_dict(shift)
        mt = self.get_message_text()

        applied_shift = []
        for character in mt:
            if character in shift_dict.keys():
                applied_shift.append(shift_dict[character])
            else:
                applied_shift.append(character)
        
        return "".join(applied_shift)



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        # call parent init
        super(PlaintextMessage, self).__init__(text)

        # do what we have to here
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super(CiphertextMessage, self).__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # access valid words once
        valid_words = self.get_valid_words()

        # store success
        success = []

        # brute force this. LEEEROOOOOY JJJJEEEEEENNNNKINSS
        # start at 0.
        for i in range(26):
            # shift it.
            self.build_shift_dict(i)
            shifted = self.apply_shift(i)

            # split the words up
            words = shifted.split(" ")


            # iterate over the first 30 words, if most are words
            # in our list then we have decrypted it, so return it
            for word in words[:30]:

                # if word in valid words, append shift success
                if is_word(valid_words, word):
                    success.append(i)
        
        # success was highest value in count minus one
        probable_shift = max(set(success), key=success.count)        


        # rebuild shift dict, calc result and return
        self.build_shift_dict(probable_shift) 
        result = self.apply_shift(probable_shift)
        return (probable_shift, result)



# message test case

# m = Message("hello")
# m.build_shift_dict(2)
# x = m.apply_shift(2)



# #Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('aoqvwbsfm ucr pfsohvs zwd gohwgtoqhcfm gvoas psr qfcgg ozz pfsoytogh vwrs hcushvsf gvwzzwbu fohs fsqcubwhwcb')
print('Expected Output:', (12, 'machinery god breathe lip satisfactory shame bed cross all breakfast hide together shilling rate recognition'))
print('Actual Output:', ciphertext.decrypt_message())

c2 = CiphertextMessage("Bcbgsbgs kcfrg: qcbjsbwsbh ufobr qcbhsbh tfca cttsbr rwghobqs qcibhfm dcgh hvs bchspccy ibqzs cddcgwhs gczjs bskgdodsf fsrrsb ciuvh fstsfsbqs ibrsf kcfr fsghoifobh pszck gcibr pfobqv gdccb dfcdcgoz pckz awzs gdofs vsfs gsfjs oacbu sbuwbs qsbhsf bswhvsf kvoh")
print('Expected: ', (12,  'Nonsense words: convenient grand content from offend distance country post the notebook uncle opposite solve newspaper redden ought reference under word restaurant below sound branch spoon proposal bowl mile spare here serve among engine center neither what'))
print('Actual Output:', c2.decrypt_message())
