from aiogram import Bot, types
from aiogram.types import ParseMode
from django.http import JsonResponse
import asyncio
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import asyncio
CHAT_ID = "6620097375"  # Replace with actual chat ID
TOKEN = "8029575791:AAFZsJ98orJ_cB9_XxqVfmPCQQw8Mpa_Vj8"  # Replace with your bot token

bot = Bot(token=TOKEN)

async def send_message_async(chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_form(request):
    if request.method == "POST":
        try:
            # request.body orqali JSON ma'lumotlarni oling
            data = json.loads(request.body)

            name = data.get("name")
            surname = data.get("surname")
            phone = data.get("phone")
            phon1 = data.get("phon1]")

            # Check if all fields are provided
            if not all([name, surname, phone, phon1]):
                return JsonResponse({"error": "All fields are required."}, status=400)

            message = f"*Name*: {name}\n*Surname*: {surname}\n*Phone*: {phone}\n*phon1*: {phon1}"

            # Asynchronous message sending
            asyncio.run(send_message_async(chat_id=CHAT_ID, message=message))

            return JsonResponse({"status": "Message sent successfully!"})
        except Exception as e:
            print(f"Error occurred: {e}")
            return JsonResponse({"error": "Internal Server Error"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)
