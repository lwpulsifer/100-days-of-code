
class BaseParser():

    def __init__(self, regex):
        self.regex = regex
        self.tokens = self.tokenize(regex)
        print(self.tokens)
    
    def set_regex(self, regex):
        print(f"Setting regex to {regex}")
        self.__init__(regex)

    def match(self, string):
        string_counter = 0
        token_counter = 0
        while token_counter < len(self.tokens):
            token = self.tokens[token_counter]
            if string_counter == len(string):
                print(f"{string} does not match regex {self.regex}")
                return
            if "?" in token:
                if string[string_counter] == token[0]:
                    string_counter += 1
            elif "*" in token:
                next_token = self.tokens[token_counter + 1] if token_counter + 1 < len(self.tokens) else ""
                if next_token == token:
                    if string[string_counter] == token[0]:
                        string_counter += 1
                    else:
                        print(f" 1 {string} does not match regex {self.regex}")
                        return
                else:
                    while string[string_counter] != next_token[0]:
                        if string[string_counter] == token[0]:
                            string_counter += 1
                        else:
                            print(f" 2 {string} does not match regex {self.regex}")
                            return
            else:
                if token == string[string_counter]:
                    string_counter += 1
                    continue
                else:
                    print(f" 3 {string} does not match regex {self.regex}")
                    return
            token_counter += 1
                
        print(f"{string} matches regex {self.regex}")

    
    def tokenize(self, string):
        tokens = []
        i = 0
        while i < len(string):
            if i == len(string) - 1:
                tokens.append(string[i])
                break
            if string[i + 1] in ["?", "*"]:
                tokens.append(string[i:i + 2])
                i += 2
            else:
                tokens.append(string[i])
                i += 1
        return tokens

def run_tests():
    parser = BaseParser("b*b*b*b*a")
    parser.match("bbbbbbbbbba")
    parser.match("ba")
    parser.match("cbbbba")
    parser.match("aslkdfjlkj")
    parser.match("bbbba")
    parser.set_regex("b?cba")
    parser.match("bcba")
    parser.match("cba")
    parser.match("ccc")
    

if __name__ == '__main__':
    run_tests()