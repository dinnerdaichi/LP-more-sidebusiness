from bs4 import BeautifulSoup

# ファイルからHTMLを読み込む
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# 指定の文章
target_texts = ["独学者全員に適しているとは限りません。", "自分にとって最適な勉強法を確立する"]  # このリストに囲みたいテキストを追加

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(html_content, "html.parser")

# <p>タグ内のみで指定の文章を <strong> タグで囲む処理
for p_tag in soup.find_all("p"):  # <p>タグのみを対象にする
    for target in target_texts:
        if target in p_tag.text:
            # 指定の文章だけを <strong> タグで囲む
            modified_text = p_tag.text.replace(target, f"<strong>{target}</strong>")
            # p_tagの元の内容をクリアし、新しいHTMLを挿入
            p_tag.clear()
            p_tag.append(BeautifulSoup(modified_text, "html.parser"))

# 変換後のHTMLを新しいファイルに書き出す (prettifyではなくstrを使用)
with open("modified.html", "w", encoding="utf-8") as file:
    file.write(str(soup))

print("変換が完了し、modified.html に保存されました。")
