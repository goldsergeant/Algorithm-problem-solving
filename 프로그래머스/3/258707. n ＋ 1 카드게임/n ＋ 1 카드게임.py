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
            if target_sum-num1 in had_cards:
                tmp.add(num1)
                tmp.add(target_sum-num1)
                flag = True
                break
        for num in tmp:
            had_cards.remove(num)

        keep_cards.add(cards[draw_card_idx])
        keep_cards.add(cards[draw_card_idx + 1])

        if flag:
            cur_round += 1
            continue
            
        tmp=set()

        for card in keep_cards:
            target = target_sum - card
            if coin>=1 and target in had_cards:
                had_cards.remove(target)
                tmp.add(card)
                coin -= 1
                flag = True
                break
        for num in tmp:
            keep_cards.remove(num)

        if flag:
            cur_round += 1
            continue
        
        tmp=set()
        for card in keep_cards:
            if coin>=2 and target_sum - card in keep_cards:
                    tmp.add(card)
                    tmp.add(target_sum-card)
                    coin -= 2
                    flag = True
                    break
        for num in tmp:
            keep_cards.remove(num)

        if flag:
            cur_round += 1
            continue

        break

    return cur_round