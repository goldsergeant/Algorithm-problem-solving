select sum(price) as total_price
from item_info
group by rarity
having rarity = 'legend';