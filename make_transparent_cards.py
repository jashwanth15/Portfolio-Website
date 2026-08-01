import os
from PIL import Image, ImageDraw, ImageFont

def create_transparent_title_card(filename, title_text, tag_text):
  width, height = 900, 1200
  # 100% transparent RGBA canvas
  img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
  draw = ImageDraw.Draw(img)

  # Subtle glass border outline with light opacity
  m = 20
  draw.rounded_rectangle([m, m, width - m, height - m], radius=36, fill=(255, 255, 255, 10), outline=(255, 255, 255, 50), width=2)

  # Try to load fonts
  try:
    font_title = ImageFont.truetype("arialbd.ttf", 62)
    font_tag = ImageFont.truetype("arialbd.ttf", 22)
  except:
    font_title = font_tag = ImageFont.load_default()

  # Center calculations
  cx, cy = width // 2, height // 2

  # Category Tag Badge (Orange pill)
  tag_w = 260
  tag_h = 44
  draw.rounded_rectangle([cx - tag_w//2, cy - 100, cx + tag_w//2, cy - 100 + tag_h], radius=22, fill=(255, 84, 45, 240))
  draw.text((cx, cy - 78), tag_text.upper(), fill=(255, 255, 255, 255), font=font_tag, anchor="mm")

  # Main Single Title (Big, Bold, Crisp with drop shadow effect)
  draw.text((cx + 3, cy + 23), title_text, fill=(0, 0, 0, 180), font=font_title, anchor="mm")
  draw.text((cx, cy + 20), title_text, fill=(255, 255, 255, 255), font=font_title, anchor="mm")

  # Subtle bottom accent line
  draw.line([(cx - 100, cy + 110), (cx + 100, cy + 110)], fill=(255, 84, 45, 220), width=4)

  img.save(filename, "PNG")
  print(f"Created transparent card: {filename}")

# Generate transparent title PNG cards for ALL 9 projects
create_transparent_title_card("card_datapilot.png", "DataPilot AI", "AI ANALYTICS")
create_transparent_title_card("card_medflow.png", "MedFlow", "HEALTHCARE PORTAL")
create_transparent_title_card("card_queuectl.png", "QueueCTL", "SYSTEMS / CLI")
create_transparent_title_card("card_tender.png", "Tender System", "ENTERPRISE MERN")
create_transparent_title_card("card_sentiment.png", "Hotel Sentiment", "NLP PIPELINE")
create_transparent_title_card("card_vanet.png", "VANET Model", "DEEP LEARNING")
create_transparent_title_card("card_forecasting.png", "Sales Forecast", "TIME SERIES")
create_transparent_title_card("card_foodapp.png", "Food Order App", "FULL STACK MERN")
create_transparent_title_card("card_skillhub.png", "SkillHub", "LEARNING PLATFORM")
