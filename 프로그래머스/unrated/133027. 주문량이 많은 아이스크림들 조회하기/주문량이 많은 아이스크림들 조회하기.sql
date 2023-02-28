-- 코드를 입력하세요
SELECT j.flavor from july j join first_half f on j.flavor=f.flavor group by flavor order by sum(j.total_order)+sum(f.total_order) desc limit 3;