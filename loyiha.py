def binary_mind_game():
    print("--- BinaryMind O'yiniga xush kelibsiz! ---")
    print("1 dan 100 gacha bo'lgan biror son o'ylang, men uni topaman.")
    input("Tayyor bo'lsangiz, 'Enter' tugmasini bosing...")

    past = 1
    baland = 100
    urinishlar = 0

    while past <= baland:
        urinishlar += 1
        taxmin = (past + baland) // 2
        print(f"\nSiz o'ylagan son: {taxmin}?")
        javob = input("To'g'ri (t), Kattaroq (k), yoki Kichikroq (kich)?: ").lower()

        if javob == 't':
            print(f"🎉 Topdim! Bor-yo'g'i {urinishlar} ta urinish bilan topdim!")
            break
        elif javob == 'k':
            past = taxmin + 1
        elif javob == 'kich':
            baland = taxmin - 1
        else:
            print("Iltimos, faqat 't', 'k' yoki 'kich' harflaridan foydalaning.")

binary_mind_game()