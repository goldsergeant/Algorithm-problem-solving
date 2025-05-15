select concat('/home/grep/src/', ugb.board_id,'/',file_id,file_name,file_ext)
from used_goods_board ugb join used_goods_file ugf on (ugb.board_id=ugf.board_id)
where ugb.views= (select views from used_goods_board order by views desc limit 1)
order by ugf.file_id desc;