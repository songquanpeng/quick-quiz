import os


def load_questions(filename="./data.txt", n=42):
    if not os.path.isfile(filename):
        print(f"题目文件 ”{filename}“ 不存在！")
        input("按回车键退出程序。")
        exit()
    questions = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = [line.replace("\n", "").strip().replace(u"\u2002", "") for line in lines]
    for i in range(1, n + 1):
        start_index = 6 * (i - 1)
        question = {"index": i, "description": "", "answer": "",
                    "options": [lines[start_index + x + 1] for x in range(4)]}
        description = lines[start_index]
        left_bracket = description.find("（")
        right_bracket = description.find("）")
        question["answer"] = description[left_bracket + 1:right_bracket].strip()
        question["description"] = description[:left_bracket + 1] + " " + description[right_bracket:]
        questions.append(question)
    return questions


def ask_question(question):
    os.system('cls')
    print(question["description"])
    for option in question["options"]:
        print(option, flush=True)
    answer = input("你的答案：")
    answer = answer.strip().upper()
    is_answer_correct = False
    if answer == question["answer"]:
        is_answer_correct = True
        print("正确！")
    else:
        print(f"错误，答案应为：{question['answer']}")
        input("按回车键继续。")
    return is_answer_correct


def main():
    questions = load_questions()
    print(f"题目加载完成，一共 {len(questions)} 道问题。")
    input("按回车键继续。")
    wrong_questions = []
    for i in range(len(questions)):
        if not ask_question(questions[i]):
            wrong_questions.append(i)
    while len(wrong_questions) != 0:
        print(f"测试完毕，错题共 {len(wrong_questions)} 道，现在开始错题训练。")
        input("按回车键继续。")
        question_indices = wrong_questions[:]
        wrong_questions = []
        for i in question_indices:
            if not ask_question(questions[i]):
                wrong_questions.append(i)
    input("训练完毕，按回车键退出程序。")


if __name__ == '__main__':
    main()
