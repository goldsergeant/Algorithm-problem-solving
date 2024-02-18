select author_id,author_name,category,sum(sales*price) as total_sales
from book join author using(author_id) join book_sales using(book_id)
where sales_date between '2022-01-01' and '2022-01-31'
group by author_id,category
order by author_id,category desc;