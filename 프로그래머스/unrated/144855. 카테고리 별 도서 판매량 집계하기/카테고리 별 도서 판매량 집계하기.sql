-- 코드를 입력하세요
SELECT category,sum(sales) from book b join book_sales bs on b.book_id=bs.book_id where sales_date like '%-01-%' group by category order by category;