from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import openai
import pyautogui
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import webbrowser


def openai_complete(prompt):  # openai 사용 함수 - 일단 다빈치03사용
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=4000,
    )
    return response["choices"][0]["text"].strip()


""" def what_time():  # 시간 보여주기용 함수 - 내장 함수 사용
    dnow = datetime.now()
    btn.config(text=dnow) """


""" def show_entry():  # 답변 출력 함수 - 일단 다빈치로 답변
    design = entry1.get()
    price = entry2.get()
    furniture = entry3.get()
    # prompt = f"{design} 디자인에 {price} 가격의 {furniture} 추천해줘"
    prompt = f"Recommend {furniture} furniture with a {design} design for {price}"
    response = openai_complete(prompt)
    text.insert(END, f"qes : {prompt}\nreq : {response}\n\n")
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
 """


""" def show_entry(selected_category):
    design = category_combobox2.get()
    price = category_combobox3.get()
    furniture = category_combobox.get()
    color = category_combobox4.get()
    prompt = f"Recommend {furniture} furniture with a {design} of {color} color design for {price} in the {selected_category} category"
    response = openai_complete(prompt)
    text.insert(END, f"qes : {prompt}\nreq : {response}\n\n") """


def show_entry():
    selected_category = category_combobox.get()
    design = category_combobox2.get()
    price = category_combobox3.get()
    furniture = category_combobox.get()
    color = category_combobox4.get()
    prompt = f"Recommend {furniture} furniture with a {design} of {color} color design for {price} in the {selected_category} category"
    response = openai_complete(prompt)
    text.insert(END, f"qes : {prompt}\nreq : {response}\n\n")


def open_new_window():
    new_window = Toplevel(root)
    new_window.title("새로운 창")

    # 새로운 창에 원하는 위젯들을 추가합니다.
    label = Label(new_window, text="새로운 창입니다.")
    label.pack()
    # 검색 버튼

    entry4_label = Label(new_window, text="상품 검색")
    entry4_label.pack()
    entry4 = Entry(root)  # 구글 검색
    entry4.pack()

    button2 = Button(new_window, text="네이버 검색", command=search)
    button2.pack()


""" def search():
    total = entry4.get()
    response = requests.get(
        # f"https://search.shopping.naver.com/search/all?query=%{total}"
        f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query= {total}"
    )
    html = response.text
    soup = BeautifulSoup(html, "html.parser")  # 깔끔하게 가져오기 위해 html.parser 사용
    links = soup.select(".basicList_link__JLQJf linkAnchor")  # 네이버의 쇼핑 제목만 크롤링

    for link in links:
        title = link.text
        uri = link.attrs["href"]
        text.insert(END, f"결과 : {title, uri}")
        entry4.delete(0, END)
        # print(title, uri) """


""" def hi():  # 출력 테스트용 함수
    hello = entry4.get()
    text.insert(END, hello) """


root = Tk()
root.title("인테리어 추천(프로토타입)")

new_window_button = Button(root, text="검색창 열기", command=open_new_window)
new_window_button.pack(anchor=NE)


def on_category_selected(event):
    selected_category = category_combobox.get()
    show_entry(selected_category)
    # 선택된 카테고리에 따른 동작 수행


furniture_categories = ["desk", "chair", "bed", "wardrobe"]
color_categories = ["blue", "black", "red", "yellow"]
price_categories = ["$10", "$100", "$1000", "$10000"]
design_categories = ["Modern", "Simple", "Unique", "Minimal"]

category_label = tk.Label(root, text="가구 ")
category_label.pack()
category_combobox = ttk.Combobox(root, values=furniture_categories)
category_combobox.pack()
category_combobox.bind("<<ComboboxSelected>>", on_category_selected)

category_label = tk.Label(root, text="색상")
category_label.pack()
category_combobox4 = ttk.Combobox(root, values=color_categories)
category_combobox4.pack()
category_combobox4.bind("<<ComboboxSelected>>", on_category_selected)

category_label = tk.Label(root, text="가격대")
category_label.pack()
category_combobox2 = ttk.Combobox(root, values=price_categories)
category_combobox2.pack()
category_combobox2.bind("<<ComboboxSelected>>", on_category_selected)

category_label = tk.Label(root, text="디자인")
category_label.pack()
category_combobox3 = ttk.Combobox(root, values=design_categories)
category_combobox3.pack()
category_combobox3.bind("<<ComboboxSelected>>", on_category_selected)

""" 
# 디자인, 가격, 가구 종류 입력창
entry1_label = Label(root, text="디자인")
entry1_label.pack()
entry1 = Entry(root)  # 디자인
entry1.pack()

entry2_label = Label(root, text="가격")
entry2_label.pack()
entry2 = Entry(root)  # 가격
entry2.pack()

entry3_label = Label(root, text="가구종류")
entry3_label.pack()
entry3 = Entry(root)  # 가구 종류
entry3.pack()
 """

""" button1 = Button(root, text="검색", command=show_entry) """
button1 = Button(root, text="search", command=show_entry)
button1.pack()

# 검색 버튼
""" button1 = Button(root, text="검색", command=show_entry) """
""" button1 = Button(root, text="search", command=show_entry)
button1.pack()

entry4_label = Label(root, text="상품 검색")
entry4_label.pack()
entry4 = Entry(root)  # 구글 검색
entry4.pack()

button2 = Button(root, text="네이버 검색", command=search)
button2.pack() """

# 시간 표시창
""" time_frame = Frame(root)
time_frame.pack() """

""" btn = Button(time_frame)
btn.config(text="현재 시각", width=30, height=3, font=("궁서", 20), command=what_time)
btn.pack() """

# 질문과 답변 표시창
text_frame = Frame(root)
text_frame.pack()

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(text_frame, yscrollcommand=scrollbar.set)
text.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=text.yview)


root.mainloop()
