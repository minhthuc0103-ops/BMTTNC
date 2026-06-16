import hashlib
import time

# ==========================================
# 1. LỚP BLOCK (Định nghĩa cấu trúc một khối)
# ==========================================
class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.proof)
        return hashlib.sha256(data.encode()).hexdigest()


# ==========================================
# 2. LỚP BLOCKCHAIN (Quản lý chuỗi khối)
# ==========================================
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # Tạo khối nguyên thủy (Genesis Block) khi khởi tạo chuỗi
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, time.time(), self.current_transactions, proof)
        self.current_transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            # Thuật toán mã hóa kiểm tra số Proof hợp lệ
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append({'sender': sender, 'receiver': receiver, 'amount': amount})
        return self.get_previous_block().index + 1

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            # Kiểm tra tính liên kết hash giữa khối cũ và khối mới
            if block.previous_hash != previous_block.hash:
                return False
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True


# ==========================================
# 3. KỊCH BẢN KIỂM THỬ (Testing the blockchain)
# ==========================================
if __name__ == '__main__':
    # Khởi tạo chuỗi blockchain
    my_blockchain = Blockchain()

    # Thêm các giao dịch vào danh sách chờ
    my_blockchain.add_transaction('Alice', 'Bob', 10)
    my_blockchain.add_transaction('Bob', 'Charlie', 5)
    my_blockchain.add_transaction('Charlie', 'Alice', 3)

    # Thực hiện đào một khối mới (Mining a new block)
    previous_block = my_blockchain.get_previous_block()
    previous_proof = previous_block.proof
    new_proof = my_blockchain.proof_of_work(previous_proof)
    previous_hash = previous_block.hash
    
    # Phần thưởng đào block (Giao dịch từ hệ thống cho thợ đào)
    my_blockchain.add_transaction('Genesis', 'Miner', 1)
    new_block = my_blockchain.create_block(new_proof, previous_hash)

    # Hiển thị thông tin chuỗi Blockchain ra màn hình
    print("--- HIỂN THỊ DANH SÁCH CÁC KHỐI ---")
    for block in my_blockchain.chain:
        print(f"Block #{block.index}")
        print("Timestamp:", block.timestamp)
        print("Transactions:", block.transactions)
        print("Proof:", block.proof)
        print("Previous Hash:", block.previous_hash)
        print("Hash:", block.hash)
        print("-" * 40)

    # Kiểm tra tính hợp lệ của toàn bộ chuỗi
    print("# Kiểm tra tính hợp lệ:")
    is_valid = my_blockchain.is_chain_valid(my_blockchain.chain)
    print("Is Blockchain Valid:", is_valid)