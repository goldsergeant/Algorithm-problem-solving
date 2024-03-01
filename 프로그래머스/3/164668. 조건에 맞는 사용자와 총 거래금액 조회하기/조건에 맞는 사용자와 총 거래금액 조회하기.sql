select USER_ID,NICKNAME,sum(price) as total_sales
from USED_GOODS_BOARD ugb join USED_GOODS_USER ugu on ugb.writer_id = ugu.user_id
where status='DONE'
group by ugu.user_id
having sum(price)>=700000
order by total_sales;