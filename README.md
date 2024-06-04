# Quantum_Computing_introduction
## Thuật toán trên máy tính cổ điển
Repo này implement thuật toán tạo số ngẫu nhiên, thuật toán tìm một số bất kì trong dãy cho trước và thuật toán tìm tất cả các số tự nhiên nhỏ hơn k trong một dãy cho trước

1) Discuss the method used for generating random numbers and its impact on the results. Can we generate the same random values multiple times? If so, please add that implementation.

    Ở task tạo số ngẫu nhiên, tôi sử dụng một thuật toán cơ bàn là Linear Congruential Generator (LCG), thuật toán được implement trong hàm sau 
    ```python
    def lcg_random(seed, a=1664525, c=1013904223, m=2**32):
        """
        Linear Congruential Generator (LCG) for generating pseudo-random numbers.
        """
        while True:
            seed = (a * seed + c) % m
            yield seed
    ```

    Đây là một thuật toán tạo số giả ngẫu nhiên với các tham số 
        
        - seed là tham số khởi tạo để sinh ngẫu nhiên
        - a và c là hai hằng số nhân và hằng số cộng thêm, có giá trị nhỏ hơn m
        - m là chu kì, các số khởi tạo sẽ nằm trong khoảng 0-> m-1, giả sử với n bit thì ta có thể tạo số ngẫu nhiên với m = 2**n 

    Hạn chế:

    LCG được sử dụng nhiều trong các hàm random của c++ hay java, tuy nhiên nó còn vài hạn chế sau. 

        các thuật toán ramdom trong máy tính cổ điển sinh ngẫu nhiên phụ thuộc vào số seed khởi đầu. Về cơ bản nếu seed cố định, 2 lần chạy khác nhau sẽ ra 2 số ngẫu nhiên giống nhau, để tránh trường hợp này các thư viện thường lấy một giá trị thời gian bất kì tại thời điểm chạy thuật toán để làm giá trị seed

    Hạn chế trên cũng là câu trả lời cho câu hỏi thứ 2, chỉ cần đặt seed giống nhau, ta sẽ tạo được các số nguẫ nhiên giống nhau 

    Vì thế nên các thuật toán ngẫu nhiên chạy trên máy tính cổ điển được gọi là "giả ngẫu nhiên", vì nó không hoàn toàn "ngẫu nhiên"


2) Analyze the average number of trials needed to solve Task 1.a and 1.b. Try to find the optimal solution with the smallest number of steps required. Discuss the complexities involved in the operations.

    Các thuật toán trong task 1.a (tìm k trong list) và 1.b(tìm tất cả các số nhỏ hơn k trong list) đều có độ phức tạp tối đa là O(n)

    thuật toán trong task 1.a có độ phức tạp trong best case là O(1), avg case là o(n/2) = O(n)

    thuật toán trong task 1.b có độ phức tạp trong cả best case và avg case là O(n)

    Với cấu trúc dữ liệu là list, có lẽ độ phức tạp O(n) cho cả bài toán 1.a và 1.b không thể tối ưu thêm



## Chay app trên docker 
step 1: build docker image from docker file 

    docker build -t flask-api-tester .

step 2 : run docker image

    docker run -p 5000:5000 flask-api-tester


## Tối ưu trên máy tính lượng tử

ở phần này, tôi có đọc qua về thuật toán tìm kiếm Grover cho máy tính lượng tử giúp tối ưu độ phức tạp thuật toán xuống còn O(log(n)), tuy nhiên vẫn chưa thực sự hiểu và có thể implement trong repo này :( 

