# 03_process_pool_math.py
from concurrent.futures import ProcessPoolExecutor
import time


def heavy_calculation(n):
    # จำลองงาน CPU-bound: คำนวณเลขยกกำลังจำนวนมาก
    print(f"🔢 เริ่มคำนวณชุดตัวเลขถึง {n}...")
    result = sum(i * i for i in range(n))
    return result


if __name__ == "__main__":
    # รายการตัวเลขที่ต้องการคำนวณ (ขนาดใหญ่)
    numbers = [8_000_000, 9_000_000, 10_000_000, 7_000_000]

    start_time = time.perf_counter()

    # ใช้ ProcessPoolExecutor เพื่อแยก Process (หนี GIL)
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_calculation, numbers))

    end_time = time.perf_counter()
    print(f"\n📊 ผลลัพธ์การคำนวณ: {results}")
    print(f"⏱️  Process Pool ใช้เวลารวม: {end_time - start_time:.2f} วินาที")
