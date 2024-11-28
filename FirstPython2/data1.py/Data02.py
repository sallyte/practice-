
# class DataProcessor:
#     def read_data(self, file_path):
#       return open(file_path).read()
    
#     def process_data(self, data):
#       return data.lower()
    
#     def save_data(self, data, file_path):
#       with open(file_path, 'w')as f:
#         f.write(data)

# processor = DataProcessor()
# data = processor.read_data('input.txt')
# processed_data = processor.process_data(data)
# processor.save_data(processed_data, 'output.txt')

##내용 결합
class Database:
    def __init__(self):
        self._connection ="DB Connection" #이 속성은 외부에서 접근 불가가 원칙

    def get_db(self):
class UserManager:
    def __init__(self,db):
        self.db = db

    def manipulate_db(self):
        self.db._connection = "Hacked Connetion"

db = Database()
manager = UserManager(db)
manager.manipulate_db()
