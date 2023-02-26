-- 코드를 입력하세요
SELECT WAREHOUSE_ID,WAREHOUSE_NAME,ADDRESS,
case
when freezer_yn='Y' then 'Y'
when freezer_yn='N' then 'N'
when freezer_yn is null then 'N'
end as freezer_yn
from food_warehouse where address like '경기%' order by warehouse_id;