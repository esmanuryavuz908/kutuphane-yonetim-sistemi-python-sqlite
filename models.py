class Book():
    def __init__(self, title, author, category, total_count, available_count):
        self.title = title
        self.author = author
        self.category = category
        self.total_count = total_count
        self.available_count = available_count


class Student():
    def __init__(self,name, student_no, department):
        self.name = name
        self.student_no = student_no
        self.department = department

        
class BorrowRecord():
    def __init__(self, book_ID, student_ID, borrow_date, return_date, status):
        self.book_ID = book_ID
        self.student_ID = student_ID
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.status = status
