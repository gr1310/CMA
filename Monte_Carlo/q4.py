from random import choice
class TextGenerator:
    def __init__(self):
        self.prefix_dict= dict()
    def assimilateText(self,file):
        try:
            file_name=file.replace(',','.')
            with open(file_name,'r', encoding="utf-8") as f:
                contents= f.read()
            list_of_words= contents.split()
            # list_of_words=[i.lower() for i in list_of_words]

            for i in range(len(list_of_words)-2):
                prefix= (list_of_words[i],list_of_words[i+1])
                suffix= list_of_words[i+2]

                if(prefix in self.prefix_dict):
                    self.prefix_dict[prefix].append(suffix)
                else:
                    self.prefix_dict[prefix]=[suffix]

        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def generateText(self,n, first_word=""):
        if not self.prefix_dict:
            print("Error, dictionary empty")
            return
        current_word= choice(list(self.prefix_dict.keys()))
        gen_txt= list(current_word)
        if(first_word!=""):
            possible_tuples=[]
            for x in list(self.prefix_dict.keys()):
                if (x[0]==first_word):
                    possible_tuples.append(x)
            if not possible_tuples:
                raise Exception("Unable to produce text with the specified start word.")
            current_word= choice(possible_tuples)
            gen_txt= list(current_word)
        while len(gen_txt) <= n:
            if not self.prefix_dict[tuple(current_word)]:
                print("No words to continue!!")
                break
            next_word= choice(list(self.prefix_dict[tuple(current_word)]))
            current_word= [current_word[1],next_word]
            gen_txt.append(next_word)
        final_txt=""
        for text in gen_txt:
            final_txt= final_txt+text+" "
        print(final_txt)
        


t = TextGenerator()
t.assimilateText('sherlock,txt')
t.generateText(50)
print('\n')
t.generateText(100,'London')
print('\n')
t.generateText(50, 'Wedge')
