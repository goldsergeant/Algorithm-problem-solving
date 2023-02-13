-- 코드를 입력하세요
SELECT product_code,sum(sales_amount*price) from product p join offline_sale o on p.product_id= o.product_id group by product_code order by sum(sales_amount*price) desc,product_code;