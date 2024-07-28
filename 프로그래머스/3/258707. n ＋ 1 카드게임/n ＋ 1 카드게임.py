def solution(coin, cards):
    cur_round = 1
    target_sum = len(cards) + 1
    had_cards = set(cards[:len(cards) // 3])

    keep_cards = set()

    for draw_card_idx in range(len(cards) // 3, len(cards), 2):
        flag = False
        tmp = set()
        for num1 in had_cards:
            if flag:
                break
            for num2 in had_cards:
                if num1 == num2:
                    continue

                if num1 + num2 == target_sum:
                    tmp.add(num1)
                    tmp.add(num2)
                    flag = True
                    break
        for num in tmp:
            had_cards.remove(num)

        keep_cards.add(cards[draw_card_idx])
        keep_cards.add(cards[draw_card_idx + 1])

        if flag:
            cur_round += 1
            continue

        for card in keep_cards.copy():
            target = target_sum - card
            if coin > 0 and target in had_cards:
                had_cards.remove(target)
                keep_cards.remove(card)
                coin -= 1
                flag = True
                break

        if flag:
            cur_round += 1
            continue

        tmp_keep_cards = keep_cards.copy()
        for card1 in tmp_keep_cards:
            if flag:
                break
            for card2 in tmp_keep_cards:
                if card1 == card2:
                    continue

                if coin >= 2 and card1 + card2 == target_sum:
                    keep_cards.remove(card1)
                    keep_cards.remove(card2)
                    coin -= 2
                    flag = True
                    break

        if flag:
            cur_round += 1
            continue

        break

    return cur_round