select year(sales_date),month(sales_date),count(distinct(user_id)), round(count(distinct(user_id))/(select count(user_id) from user_info where year(joined)=2021),1)
from user_info join online_sale using(user_id)
where year(joined)=2021
group by year(sales_date),month(sales_date)
order by year(sales_date),month(sales_date);
