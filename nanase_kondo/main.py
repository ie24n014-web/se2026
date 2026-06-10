study_history = []
goal = ""

while True:
    print("\n=== 基本情報技術者 学習システム ===")
    print("1. 過去問を解く")
    print("2. 学習ノルマを設定")
    print("3. 学習履歴を表示")
    print("4. 用語を検索")
    print("5. 復習する")
    print("6. 終了")

    choice = input("番号を選択してください: ")

    if choice == "1":
        question = "OSI参照モデルは何層ですか？"
        print("\n問題:", question)

        answer = input("解答を入力してください: ")

        if answer == "7":
            print("正解です")
            study_history.append("過去問: 正解")
        else:
            print("不正解です")
            study_history.append("過去問: 不正解")

    elif choice == "2":
        goal = input("学習ノルマを入力してください: ")
        print("学習ノルマを設定しました:", goal)

    elif choice == "3":
        print("\n--- 学習履歴 ---")
        print("現在のノルマ:", goal)

        if len(study_history) == 0:
            print("履歴はありません")
        else:
            for i, history in enumerate(study_history, start=1):
                print(f"{i}. {history}")

    elif choice == "4":
        word = input("検索したい用語を入力してください: ")

        if word == "OSI":
            print("OSI参照モデルはネットワーク通信の7層モデルです。")
        else:
            print(word, "を検索しました")

    elif choice == "5":
        print("復習する問題はありません。")

    elif choice == "6":
        print("システムを終了します")
        break

    else:
        print("無効な入力です")