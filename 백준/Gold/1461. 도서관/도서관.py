N, M = map(int, input().split())
books = list(map(int, input().split()))

positive_books = [i for i in books if i > 0]
negative_books = [i for i in books if i < 0]

positive_books.sort(reverse=True)
negative_books.sort()

check_books=[]

for i in range(0,len(positive_books),M):
    check_books.append(positive_books[i])

for i in range(0,len(negative_books),M):
    check_books.append(abs(negative_books[i]))

check_books.sort()

print(sum(check_books[:-1])*2+check_books[-1])

