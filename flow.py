import json


class ChatFlow:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_file(self):
        try:
            file = json.load(open(self.file_path, encoding='utf-8'))
            return file
        except FileNotFoundError:
            raise FileNotFoundError('data.json')

    def print_categories(self):
        data = self.load_file()
        categories = list(data.keys())
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")

        category_choice = int(input("اختر السؤال: "))
        customer_category = data[categories[category_choice-1]]

        for i, category in enumerate(customer_category):
            print(f"{i + 1}. {list(category.keys())[0]}")

        question_choice = int(input("اختر السؤال: "))
        question_answer = list(customer_category[question_choice-1].values())[0]
        print(question_answer)


chat_flow = ChatFlow("data.json")
chat_flow.print_categories()