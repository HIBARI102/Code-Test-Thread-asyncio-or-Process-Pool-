# 02_threaded_logs.py
from concurrent.futures import ThreadPoolExecutor
import time
import threading


def write_log(filename):
    thread_id = threading.get_ident()
    print(f"📝 Thread {thread_id} กำลังเขียนไฟล์ {filename}...")
    time.sleep(1)  # จำลองการเขียนไฟล์ (I/O)
    print(f"✔️  ไฟล์ {filename} เขียนเสร็จสิ้น")


if __name__ == "__main__":
    filenames = [f"log_{i}.txt" for i in range(5)]
    start_time = time.perf_counter()

    # ใช้ ThreadPoolExecutor จัดการ Thread
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(write_log, filenames)

    end_time = time.perf_counter()
    print(f"\n⏱️  Threading ใช้เวลารวม: {end_time - start_time:.2f} วินาที")
