-- 코드를 입력하세요
SELECT title,board_id,reply_id,ugr.writer_id,ugr.contents,date_format(ugr.created_date,'%Y-%m-%d') as created_date
from used_goods_board ugb join used_goods_reply ugr using(board_id)
where year(ugb.created_date)=2022 and month(ugb.created_date)=10
order by created_date,title;