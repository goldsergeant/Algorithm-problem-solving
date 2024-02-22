select iti.item_id,iti.item_name,iti.rarity
from item_info iti
where item_id not in (select parent_item_id
                    from item_tree 
                     where exists (
                     select * from item_info where item_id=parent_item_id
                     ))
order by item_id desc;