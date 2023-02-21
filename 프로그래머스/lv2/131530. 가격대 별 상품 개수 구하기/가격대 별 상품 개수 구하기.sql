-- 코드를 입력하세요
SELECT truncate((price/10000),0)*10000 p
,count(*) from product group by p order by p; 