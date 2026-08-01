import os
from PIL import Image, ImageDraw, ImageFont

def create_card(filename, title, subtitle, badge, accent_color, ui_type):
  width, height = 900, 1200
  img = Image.new('RGB', (width, height), color='#0d0a12')
  draw = ImageDraw.Draw(img)

  # Background subtle gradient effect
  for y in range(height):
    r = int(13 + (y / height) * 10)
    g = int(10 + (y / height) * 8)
    b = int(18 + (y / height) * 15)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

  # Outer margin
  m = 40

  # Draw App Window Header Bar (Browser Mockup Window)
  win_y = 120
  win_h = 960
  win_w = width - (m * 2)

  # Glassmorphic window background
  draw.rectangle([m, win_y, m + win_w, win_y + win_h], fill='#16121f', outline='#2a2238', width=2)
  
  # Window Top Bar
  draw.rectangle([m, win_y, m + win_w, win_y + 50], fill='#1f192b')
  # Window buttons (red, yellow, green)
  draw.ellipse([m + 16, win_y + 18, m + 28, win_y + 30], fill='#ff5f56')
  draw.ellipse([m + 36, win_y + 18, m + 48, win_y + 30], fill='#ffbd2e')
  draw.ellipse([m + 56, win_y + 18, m + 68, win_y + 30], fill='#27c93f')

  # Address Bar
  draw.rectangle([m + 100, win_y + 12, m + win_w - 120, win_y + 38], fill='#120e1a', outline='#332a42', width=1)
  
  # Load Font
  try:
    font_title = ImageFont.truetype("arial.ttf", 36)
    font_sub = ImageFont.truetype("arial.ttf", 22)
    font_small = ImageFont.truetype("arial.ttf", 18)
    font_mono = ImageFont.truetype("consola.ttf", 16)
    font_heading = ImageFont.truetype("arialbd.ttf", 42)
  except:
    font_title = font_sub = font_small = font_mono = font_heading = ImageFont.load_default()

  # Address Bar URL Text
  draw.text((m + 120, win_y + 16), f"https://{filename.split('.')[0]}.jashwanth.dev", fill='#a1a1aa', font=font_small)

  # UI Content Area
  content_y = win_y + 70

  # Badge Tag
  draw.rectangle([m + 30, content_y, m + 240, content_y + 36], fill=accent_color)
  draw.text((m + 45, content_y + 8), badge.upper(), fill='#ffffff', font=font_small)

  # Main Project Title
  draw.text((m + 30, content_y + 55), title, fill='#ffffff', font=font_heading)
  draw.text((m + 30, content_y + 110), subtitle, fill='#a1a1aa', font=font_sub)

  # UI Mockup Components depending on UI Type
  ui_y = content_y + 170

  if ui_type == 'datapilot':
    # Search / Prompt Input Bar
    draw.rectangle([m + 30, ui_y, m + win_w - 30, ui_y + 60], fill='#0d0a12', outline=accent_color, width=2)
    draw.text((m + 50, ui_y + 18), "💬 Ask AI: 'Analyze total revenue & plot quarterly growth trend'", fill='#ffffff', font=font_sub)
    draw.rectangle([m + win_w - 140, ui_y + 10, m + win_w - 40, ui_y + 50], fill=accent_color)
    draw.text((m + win_w - 120, ui_y + 20), "RUN", fill='#ffffff', font=font_small)

    # Output Stream Box
    box_y = ui_y + 85
    draw.rectangle([m + 30, box_y, m + win_w - 30, box_y + 400], fill='#0a080e', outline='#2a2238')
    draw.text((m + 50, box_y + 20), "FastAPI StreamingResponse :: Executing Pandas Analysis...", fill=accent_color, font=font_mono)
    
    # Table headers
    draw.rectangle([m + 50, box_y + 60, m + win_w - 50, box_y + 100], fill='#1a1426')
    draw.text((m + 70, box_y + 72), "Quarter    Region      Revenue ($)    Growth (%)", fill='#ffffff', font=font_mono)
    
    rows = [
      "Q1 2025    North Am    $1,240,500     +18.4%",
      "Q2 2025    Europe      $980,200       +14.2%",
      "Q3 2025    Asia Pac    $1,450,000     +22.8%",
      "Q4 2025    Global      $2,100,800     +31.5%"
    ]
    for idx, row in enumerate(rows):
      ry = box_y + 120 + (idx * 35)
      draw.text((m + 70, ry), row, fill='#d4d4d8', font=font_mono)

    # Bar chart preview
    chart_y = box_y + 270
    bars = [120, 180, 240, 310]
    for idx, b_h in enumerate(bars):
      bx = m + 100 + (idx * 160)
      draw.rectangle([bx, chart_y + (100 - b_h//3.5), bx + 90, chart_y + 100], fill=accent_color)

  elif ui_type == 'medflow':
    # Role Selection Tabs
    tabs = ["PATIENT", "DOCTOR", "PHARMACIST", "ADMIN (RBAC)"]
    for idx, tab in enumerate(tabs):
      tx = m + 30 + (idx * 195)
      fill_c = accent_color if idx == 1 else '#1f192b'
      draw.rectangle([tx, ui_y, tx + 185, ui_y + 45], fill=fill_c, outline='#382d4d')
      draw.text((tx + 25, ui_y + 14), tab, fill='#ffffff', font=font_small)

    # Doctor Dashboard Panel
    box_y = ui_y + 65
    draw.rectangle([m + 30, box_y, m + win_w - 30, box_y + 420], fill='#0a080e', outline='#2a2238')
    draw.text((m + 50, box_y + 20), "Doctor Dashboard — Real-Time Token & Appointment Queue", fill='#ffffff', font=font_title)

    # Patient Queue Table
    patients = [
      ("Token #101", "Rahul Sharma", "Symptom Review", "10:30 AM", "APPROVED"),
      ("Token #102", "Priya Verma", "Prescription Renewal", "10:45 AM", "IN CONSULT"),
      ("Token #103", "Anish Kumar", "Lab Results Follow-up", "11:15 AM", "WAITING"),
      ("Token #104", "Sneha Patel", "General Checkup", "11:30 AM", "SCHEDULED")
    ]
    for idx, (tok, name, reason, time_val, status) in enumerate(patients):
      py = box_y + 80 + (idx * 80)
      draw.rectangle([m + 50, py, m + win_w - 50, py + 65], fill='#161124', outline='#2c223d')
      draw.text((m + 70, py + 20), f"{tok}  |  {name}", fill='#ffffff', font=font_sub)
      draw.text((m + 420, py + 22), f"{reason} ({time_val})", fill='#a1a1aa', font=font_small)
      draw.rectangle([m + win_w - 200, py + 15, m + win_w - 70, py + 50], fill=accent_color)
      draw.text((m + win_w - 185, py + 25), status, fill='#ffffff', font=font_small)

  elif ui_type == 'tender':
    # Search / Action Bar
    draw.rectangle([m + 30, ui_y, m + win_w - 30, ui_y + 50], fill='#1f192b', outline='#382d4d')
    draw.text((m + 50, ui_y + 15), "Enterprise Procurement & Bidding Portal (MERN Stack)", fill='#ffffff', font=font_sub)

    # Stat Badges
    box_y = ui_y + 70
    stats = [
      ("Active Tenders", "148"),
      ("Vendor Bids", "1,240"),
      ("Avg Response Time", "28% Faster (MongoDB)")
    ]
    for idx, (label, val) in enumerate(stats):
      sx = m + 30 + (idx * 260)
      draw.rectangle([sx, box_y, sx + 245, box_y + 90], fill='#161124', outline='#382d4d')
      draw.text((sx + 20, box_y + 15), label, fill='#a1a1aa', font=font_small)
      draw.text((sx + 20, box_y + 45), val, fill=accent_color, font=font_sub)

    # Tender List Table
    table_y = box_y + 110
    draw.rectangle([m + 30, table_y, m + win_w - 30, table_y + 300], fill='#0a080e', outline='#2a2238')
    tenders = [
      ("TND-8942", "Smart City Infrastructure Phase II", "$4.2M", "12 Bids", "OPEN"),
      ("TND-8943", "Cloud Server Migration & DevOps", "$850K", "8 Bids", "EVALUATING"),
      ("TND-8944", "Enterprise ERP System Modernization", "$1.8M", "19 Bids", "AWARDED")
    ]
    for idx, (tid, name, val, bids, status) in enumerate(tenders):
      ty = table_y + 30 + (idx * 80)
      draw.rectangle([m + 50, ty, m + win_w - 50, ty + 65], fill='#1a1426')
      draw.text((m + 70, ty + 20), f"{tid} — {name}", fill='#ffffff', font=font_sub)
      draw.text((m + win_w - 280, ty + 22), f"{val} ({bids})", fill=accent_color, font=font_small)

  elif ui_type == 'vanet':
    # Model Benchmarking Card
    box_y = ui_y
    draw.rectangle([m + 30, box_y, m + win_w - 30, box_y + 480], fill='#0a080e', outline='#2a2238')
    draw.text((m + 50, box_y + 25), "VANET Vehicle Mobility Prediction (LSTM vs GRU)", fill='#ffffff', font=font_title)
    draw.text((m + 50, box_y + 70), "Quantitative Test Accuracy Benchmark: 92.4% (LSTM Selected)", fill=accent_color, font=font_sub)

    # Graph Area Simulation
    gy = box_y + 120
    draw.rectangle([m + 50, gy, m + win_w - 50, gy + 320], fill='#140f1d', outline='#2d223d')
    
    # Plot grid lines
    for i in range(5):
      ly = gy + 40 + (i * 60)
      draw.line([(m + 70, ly), (m + win_w - 70, ly)], fill='#241b33', width=1)

    # LSTM accuracy curve (Green/Accent line)
    points_lstm = [(m + 90, gy + 260), (m + 220, gy + 180), (m + 350, gy + 110), (m + 480, gy + 80), (m + 650, gy + 55), (m + win_w - 90, gy + 45)]
    draw.line(points_lstm, fill=accent_color, width=4)

    # GRU accuracy curve (Secondary line)
    points_gru = [(m + 90, gy + 270), (m + 220, gy + 210), (m + 350, gy + 150), (m + 480, gy + 120), (m + 650, gy + 95), (m + win_w - 90, gy + 85)]
    draw.line(points_gru, fill='#38bdf8', width=3)

    draw.text((m + win_w - 220, gy + 50), "—— LSTM (92.4%)", fill=accent_color, font=font_small)
    draw.text((m + win_w - 220, gy + 90), "—— GRU (88.7%)", fill='#38bdf8', font=font_small)

  elif ui_type == 'sentiment':
    # NLP Overview
    box_y = ui_y
    draw.rectangle([m + 30, box_y, m + win_w - 30, box_y + 480], fill='#0a080e', outline='#2a2238')
    draw.text((m + 50, box_y + 25), "Hotel Guest Review Sentiment NLP Pipeline", fill='#ffffff', font=font_title)
    draw.text((m + 50, box_y + 70), "Processed 20,000+ Unstructured Guest Reviews Automatically", fill=accent_color, font=font_sub)

    # Sentiment Breakdown Bars
    sy = box_y + 130
    draw.text((m + 50, sy), "POSITIVE SENTIMENT (68%)", fill='#27c93f', font=font_small)
    draw.rectangle([m + 50, sy + 30, m + 500, sy + 55], fill='#27c93f')

    draw.text((m + 50, sy + 75), "NEUTRAL SENTIMENT (22%)", fill='#ffbd2e', font=font_small)
    draw.rectangle([m + 50, sy + 105, m + 220, sy + 130], fill='#ffbd2e')

    draw.text((m + 50, sy + 150), "NEGATIVE SENTIMENT (10%)", fill='#ff5f56', font=font_small)
    draw.rectangle([m + 50, sy + 180, m + 120, sy + 205], fill='#ff5f56')

    # TextBlob vs VADER Box
    bench_y = sy + 230
    draw.rectangle([m + 50, bench_y, m + win_w - 50, bench_y + 90], fill='#161124', outline='#2d223d')
    draw.text((m + 70, bench_y + 20), "Model Evaluation: TextBlob vs. VADER Metrics Benchmark", fill='#ffffff', font=font_sub)
    draw.text((m + 70, bench_y + 52), "Selected VADER lexicon model for superior consistency on noisy text data.", fill='#a1a1aa', font=font_small)

  # Footer branding on image
  draw.text((m + 30, height - 70), "JASHWANTH LAVUDYA  |  PRODUCTION PROJECT PREVIEW", fill='#ffffff', font=font_small)

  img.save(filename, quality=95)
  print(f"Saved {filename}")

# Generate all 5 realistic project cards
create_card("card_datapilot.jpg", "DataPilot AI Analyst", "Natural Language LLM Data Platform (FastAPI + FastMCP)", "LIVE PLATFORM", "#ff542d", "datapilot")
create_card("card_medflow.jpg", "MedFlow Healthcare Suite", "Multi-Role Healthcare App (MERN Stack + JWT RBAC)", "LIVE MERN APP", "#ff542d", "medflow")
create_card("card_tender.jpg", "Tender Management System", "Enterprise Procurement Portal (28% Response Speedup)", "MERN ENTERPRISE", "#ff542d", "tender")
create_card("card_vanet.jpg", "VANET Mobility Predictor", "Vehicle Mobility Time-Series Model (92% Accuracy)", "DEEP LEARNING", "#ff542d", "vanet")
create_card("card_sentiment.jpg", "Hotel Sentiment NLP", "20,000+ Hotel Guest Reviews Analytics Pipeline", "NLP ANALYTICS", "#ff542d", "sentiment")
