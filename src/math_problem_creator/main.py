from equation_generator import *
from math_problem_creator.word_generator import WordGenerator

if __name__ == '__main__':
    creator = EasyEquationCreator(num_steps=0.1)

    word_generator = WordGenerator()
    word_generator.create_table(num_rows=15, num_cols=4, equation_fun=creator)
    word_generator.create_simple_word_doc2()
