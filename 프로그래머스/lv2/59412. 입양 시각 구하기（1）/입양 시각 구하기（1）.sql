-- 코드를 입력하세요
SELECT hour(datetime) h, count(*) from animal_outs group by h having h>=9 and h<=19 order by h;