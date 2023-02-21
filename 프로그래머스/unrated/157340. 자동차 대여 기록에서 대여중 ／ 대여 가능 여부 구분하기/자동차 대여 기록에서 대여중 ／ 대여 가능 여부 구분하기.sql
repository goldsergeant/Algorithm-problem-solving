-- 코드를 입력하세요
SELECT car_id,if(max(end_date)>='2022-10-16','대여중','대여 가능') as availability from car_rental_company_rental_history where start_date<='2022-10-16' group by car_id order by car_id desc;