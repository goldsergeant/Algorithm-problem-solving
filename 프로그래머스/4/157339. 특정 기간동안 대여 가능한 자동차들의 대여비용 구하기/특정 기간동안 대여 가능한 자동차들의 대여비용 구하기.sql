-- 코드를 입력하세요
select car_id,car_type,floor(30*DAILY_FEE*(1-DISCOUNT_RATE/100)) as fee
from car_rental_company_car join CAR_RENTAL_COMPANY_DISCOUNT_PLAN using(car_type) 
where car_type in ('세단','SUV')
and car_id not in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where end_date>='2022-11-01' and start_date <='2022-11-30')
and duration_type ='30일 이상'
and 30*DAILY_FEE*(1-DISCOUNT_RATE/100) between 500000 and 1999999
order by fee desc, car_type,car_id desc;