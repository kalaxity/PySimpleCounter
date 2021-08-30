import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED

# 変数宣言やウィンドウの作成
count = 0

sg.theme("Light Blue")
menu = [
    [sg.MenuBar([
        # ::の後にkeyを書くことができる
        ["非表示設定", ["リセットボタン", ["表示::reset_able", "非表示::reset_disable"], "1戻すボタン", ["表示::undo_able", "非表示::undo_disable"]]],
        ["詳細", ["このアプリについて::about"]]
    ],
    key="menu")]
]
layout = [
    [menu],
    [sg.Text(text=f"{count:10}", key="display", justification="center", font=("Helvetica", 20))], # とりあえず5桁で
    [sg.Button(button_text="カウント！", size=(20, 10), key="count")],
    [sg.Text()], # 誤爆防止のため空欄を入れる
    [sg.Button(button_text="reset", size=(9, 1), key="reset"),
     sg.Button(button_text="1戻す", size=(9, 1), key="undo")]
]

window = sg.Window("PySimpleCounter", layout, keep_on_top=True, text_justification="center") # 最前面表示する

# カウント数表示の更新をする関数
# windowを用いているのでwindowの定義を済ませてから定義する必要があり、しょうがなくこの位置に書いた
def updateDisplay():
    window["display"].Update(f"{count:10}")

# === メイン関数 ===
while(True):
    event, values = window.read()
    if (event == "count"):
        count += 1
        updateDisplay()
    elif (event == "reset"):
        count = 0
        updateDisplay()
    elif (event == "undo"):
        if (count > 0): # マイナスにならないようにする
            count -= 1
            updateDisplay()
    elif (event == "このアプリについて::about"):
        sg.popup("PySimpleCounter ver. 1.0", title="About", keep_on_top=True, )
    elif (event == "表示::reset_able"):
        window["reset"].Update(visible=True)
    elif (event == "非表示::reset_disable"):
        window["reset"].Update(visible=False)
    elif (event == "表示::undo_able"):
        window["undo"].Update(visible=True)
    elif (event == "非表示::undo_disable"):
        window["undo"].Update(visible=False)
    elif (event == sg.WIN_CLOSED):
        break

window.close()