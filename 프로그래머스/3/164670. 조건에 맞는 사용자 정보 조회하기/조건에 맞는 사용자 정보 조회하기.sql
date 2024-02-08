-- 코드를 입력하세요
SELECT user_id,nickname,concat(city,' ',street_address1,' ',street_address2),concat(substring(tlno,1,3),'-',substring(tlno,4,4),'-',substring(tlno,8,4))
from used_goods_user ugu 
join used_goods_board ugb on user_id=writer_id 
group by writer_id having count(writer_id)>=3
order by user_id desc;