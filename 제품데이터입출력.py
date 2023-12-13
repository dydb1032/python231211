import sqlite3

class ProductManager:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                product_id TEXT,
                product_name TEXT,
                price REAL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_id, product_name, price):
        self.cursor.execute('''
            INSERT INTO products (product_id, product_name, price)
            VALUES (?, ?, ?)
        ''', (product_id, product_name, price))
        self.conn.commit()

    def update_product(self, product_id, new_product_name, new_price):
        self.cursor.execute('''
            UPDATE products
            SET product_name = ?, price = ?
            WHERE product_id = ?
        ''', (new_product_name, new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM products
            WHERE product_id = ?
        ''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute('''
            SELECT * FROM products
            WHERE product_id = ?
        ''', (product_id,))
        return self.cursor.fetchone()

# 샘플 데이터 추가
def insert_sample_data(product_manager):
    sample_data = [
        ("P001", "Keyboard", 25.0),
        ("P002", "Mouse", 15.0),
        ("P003", "Monitor", 200.0),
        ("P004", "Headphones", 50.0),
        ("P005", "Laptop", 800.0),
        ("P006", "Desk", 120.0),
        ("P007", "Printer", 150.0),
        ("P008", "Speakers", 70.0),
        ("P009", "Webcam", 45.0),
        ("P010", "Microphone", 55.0),
    ]

    for data in sample_data:
        product_manager.insert_product(*data)

if __name__ == "__main__":
    # ProductManager 인스턴스 생성
    manager = ProductManager()

    # 샘플 데이터 추가
    insert_sample_data(manager)

    # 예시: 제품 조회
    product = manager.select_product("P003")
    print("Selected Product:", product)

    # 예시: 제품 업데이트
    manager.update_product("P004", "Wireless Headphones", 60.0)

    # 예시: 제품 삭제
    manager.delete_product("P007")
