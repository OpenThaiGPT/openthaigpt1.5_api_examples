# OpenThaiGPT 1.5 API Examples
This repository contains examples of how to use the OpenThaiGPT 1.5 API powered by Float16.

Author: kobkrit@aieat.or.th

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/openthaigpt1.5_api_examples.git
   cd openthaigpt1.5_api_examples
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

The main example is provided in the `api_generate_powered_by_float16.py` file. Here's how to use it:

1. Open the `api_generate_powered_by_float16.py` file.

2. Replace the following variables with your actual API credentials:
   ```python
   api_base = "https://api.float16.cloud/dedicate/YOUR_DEDICATED_ID/v1"
   api_key = "YOUR_API_KEY"
   model = "openthaigpt/openthaigpt1.5-7b-instruct"
   ```

3. Run the script:
   ```
   python api_generate_powered_by_float16.py
   ```

The script demonstrates how to use the OpenAIClient class to generate text using the OpenThaiGPT 1.5 model. You can modify the prompt and other parameters as needed.

## Example Output

The script will print the generated text based on the given prompt. For example:

```
Generated Text: กรุงเทพมหานคร หรือที่เรียกสั้นๆ ว่า กรุงเทพ คือเมืองหลวงของประเทศไทย มีฐานะเป็นจังหวัดพิเศษ ตั้งอยู่บนที่ราบศุกร์ บริเวณตอนกลางของภาคกลาง มีพื้นที่ประมาณ 1,568.72 ตารางกิโลเมตร ซึ่งเป็นพื้นที่ที่มีประชากรหนาแน่นที่สุดในประเทศไทย มีประชากรประมาณ 10.2 ล้านคน (ปี 2020) กรุงเทพมหานครเป็นศูนย์กลางการเมือง การศึกษา การเงิน การค้า การท่องเที่ยว และเทคโนโลยีสารสนเทศของประเทศ ประกอบด้วยสถานที่สำคัญๆ มากมาย เช่น พระบรมมหาราชวัง พระบรมมหาราชวัง วัดพระแก้ว อนุสาวรีย์ชัยสมรภูมิ อนุสาวรีย์ประชาธิปไตย ตลาดลุมพินี ห้างสรรพสินค้าชั้นนำ ตึกสูง อาคารสำนักงาน รวมถึงสถานที่ท่องเที่ยวและวัฒนธรรมอื่นๆ มากมาย
```