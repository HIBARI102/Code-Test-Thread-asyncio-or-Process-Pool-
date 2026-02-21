# 01_async_io_weather.py
import asyncio
import time


async def fetch_weather(city):
    print(f"☁️  กำลังดึงข้อมูลสภาพอากาศของเมือง: {city}...")
    # จำลองการรอ Network I/O 2 วินาที
    await asyncio.sleep(2)
    print(f"✅ ดึงข้อมูลเมือง {city} สำเร็จ!")
    return f"{city}: 25°C"


async def main():
    start_time = time.perf_counter()
    cities = ["Bangkok", "Tokyo", "London", "New York", "Paris"]

    # สร้าง List ของ Tasks
    tasks = [fetch_weather(city) for city in cities]

    # รันทุกอย่างพร้อมกัน
    results = await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    print(f"\n📊 ผลลัพธ์: {results}")
    print(f"⏱️  ใช้เวลารวมทั้งหมด: {end_time - start_time:.2f} วินาที (ควรจะประมาณ 2 วินาที)")


if __name__ == "__main__":
    asyncio.run(main())
