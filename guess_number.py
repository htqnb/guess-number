import random


best_history = 0
try:
    with open("best_score.txt", "r") as f:
        best_history = int(f.read().strip())
except FileNotFoundError:
    pass


while True:
    print("\n" + "=" * 30)


    if best_history > 0:
        print(f"🏆 你的历史最佳成绩为：{best_history} 次猜对")
    else:
        print("还没有历史记录，来创造第一个吧！")


    target = random.randint(1, 100)
    count = 0
    max_try = 7


    while count < max_try:
        guess = int(input("猜一个 1~100 的数字："))
        count += 1

        if guess < target:
            print("小了")
        elif guess > target:
            print("大了")
        else:
            print(f"猜中了！你用了 {count} 次。")

            if best_history == 0 or count < best_history:
                print("🎉 新纪录！")
                best_history = count
                with open("best_score.txt", "w") as f:
                    f.write(str(count))
            else:
                print(f"没破纪录，历史最佳是 {best_history} 次。")
            break
    else:

        print(f"次数用完了，别猜了，答案为：{target}")


    play_again = input("\n还要再来一局吗？(输入 y 继续，输入其他退出): ")


    if play_again.lower() != 'y':
        print("游戏结束，拜拜！")
        break