select ugu.user_id, ugu.nickname,concat(ugu.city,' ',ugu.street_address1,' ',ugu.street_address2) as 전체주소, concat(substring(tlno,1,3),'-',substring(tlno,4,4),'-',substring(tlno,8,4)) as 전화번호
from used_goods_board ugb join used_goods_user ugu on (ugb.writer_id=ugu.user_id)
group by ugb.writer_id
having count(ugb.writer_id)>=3
order by ugu.user_id desc;