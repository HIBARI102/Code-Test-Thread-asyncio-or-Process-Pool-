import time
import threading

# 1. จำลองการดึงสภาพอากาศ (แบบปกติ)
def fetch_weather_sync(city):
    print(f"☁️  (Sync) กำลังดึงข้อมูล: {city}...")
    time.sleep(2)  # หยุดรอจริงๆ 2 วินาที
    return f"{city}: 25°C"


# 2. การเขียนบันทึกข้อมูล (Logging) ลงไฟล์หลายๆ (แบบปกติ)
def write_log(filename, mode="Normal"):
    thread_id = threading.get_ident()
    print(f"📝 [{mode}] Thread {thread_id} กำลังเขียนไฟล์ {filename}...")
    time.sleep(1)  # จำลองการทำงานที่ต้องรอ (I/O Bound)
    return f"✔️ {filename} เสร็จสิ้น"


# 3. จำลองการคำนวณเลข (แบบปกติ)
def heavy_calculation_sync(n):
    print(f"🔢 (Sync) กำลังคำนวณชุดตัวเลข {n}...")
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    print("--- เริ่มการทดสอบแบบ Sequential (ทำทีละอย่าง) ---\n")

    # ทดสอบ Weather
    start = time.perf_counter()
    cities = ["Bangkok", "Tokyo", "London"]
    [fetch_weather_sync(c) for c in cities]
    print(
        f"⏱️  Weather (Sync) ใช้เวลา: {time.perf_counter() - start:.2f} วินาที (ควรจะ ~6 วินาที)\n"
    )

    # ทดสอบเขียน Log
    filenames = [f"log_{i}.txt" for i in range(5)]
    print("--- เริ่มการทำงานแบบปกติ (ทีละไฟล์) ---")
    start_sync = time.perf_counter()
    for f in filenames:
        write_log(f)
    end_sync = time.perf_counter()
    sync_duration = end_sync - start_sync
    print(f"⏱️ แบบปกติใช้เวลารวม: {sync_duration:.2f} วินาที\n")

    print("-" * 40)
    # ทดสอบ Math
    start = time.perf_counter()
    numbers = [8_000_000, 9_000_000, 10_000_000]
    [heavy_calculation_sync(n) for n in numbers]
    print(f"⏱️  Math (Sync) ใช้เวลา: {time.perf_counter() - start:.2f} วินาที")
