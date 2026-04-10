from flask import Flask, request, jsonify, render_template_string, send_from_directory
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)
CORS(app)

FILE_NAME = "plans.json"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

# Serve main HTML
@app.route('/')
def index():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return '<h1>🔴 Error: index.html not found</h1>', 404

# Serve share page
@app.route('/share')
def share():
    try:
        with open('share.html', 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return '<h1>🔴 Error: share.html not found</h1>', 404

@app.route('/ai', methods=['POST'])
def ai():
    user_goal = request.json.get('goal', '')

    # Try to use Ollama, but provide a comprehensive fallback response
    ollama_url = "http://localhost:11434/api/chat"
    ollama_payload = {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": "You are a Global Business Architect & AI Operations Director. Provide a comprehensive business plan."},
            {"role": "user", "content": f"Create a complete business plan for: {user_goal}"}
        ]
    }

    try:
        ollama_response = requests.post(ollama_url, json=ollama_payload, timeout=10)
        ollama_response.raise_for_status()
        ai_response = ollama_response.json()
        response = {
            "status": "success",
            "data": ai_response
        }
    except:
        # Comprehensive fallback response with complete business plan template
        fallback_plan = f"""
═══════════════════════════════════════════════════════════════════════════════
                    AI BUSINESS BUILDER PRO - COMPLETE PLAN
                            Business Idea: {user_goal}
═══════════════════════════════════════════════════════════════════════════════

█ 1. THE AI DREAM TEAM - VIRTUAL DEPARTMENT (15+ TOOLS)

┌─ CONTENT CREATION AI ─────────────────────────────────────────────────────┐
│ Tool: ChatGPT-4 Pro
│ Why: Generate high-quality business content, marketing copy, emails
│ Link: https://openai.com/chatgpt
│ Specific Prompt: "Write [type] content for [business idea] targeting [audience]"
│
│ Tool: Midjourney
│ Why: Create stunning visual content for social media & ads
│ Link: https://midjourney.com
│ Specific Prompt: "Professional product photo, high-quality, [style], [subject]"
│
│ Tool: Jasper AI
│ Why: Long-form content generation & SEO optimization  
│ Link: https://www.jasper.ai
│ Specific Prompt: "Write SEO-optimized blog post about [topic]"
│
│ Tool: Copy.ai
│ Why: Ad copy, landing pages, social media captions
│ Link: https://www.copy.ai
│ Specific Prompt: "Write 5 viral Instagram captions for [product]"
└───────────────────────────────────────────────────────────────────────────┘

┌─ LEAD GENERATION & SALES AI ──────────────────────────────────────────────┐
│ Tool: Typeform
│ Why: AI-powered lead capture forms & surveys
│ Link: https://typeform.com
│ Workflow: Auto-qualify leads → send to CRM → trigger email sequences
│
│ Tool: Leadpages
│ Why: Landing pages with AI A/B testing
│ Link: https://www.leadpages.com
│ Specific Setup: Create → Test → Optimize → Automate with Zapier
│
│ Tool: HubSpot (CRM)
│ Why: Store & automate customer interactions
│ Link: https://hubspot.com
│ Workflow: Capture → Score → Nurture → Close
└───────────────────────────────────────────────────────────────────────────┘

┌─ CUSTOMER SERVICE AI ─────────────────────────────────────────────────────┐
│ Tool: Tidio
│ Why: AI chatbot handles customer inquiries 24/7
│ Link: https://www.tidio.com
│ Setup: Train on FAQ → Deploy on website → Monitor conversations
│
│ Tool: Drift
│ Why: Conversational AI for real-time customer engagement
│ Link: https://www.drift.com
│ Workflow: Visitor lands → Chatbot engages → Books demo/sale
└───────────────────────────────────────────────────────────────────────────┘

┌─ SOCIAL MEDIA MANAGEMENT AI ──────────────────────────────────────────────┐
│ Tool: Buffer
│ Why: Schedule posts, analyze performance across 6+ platforms
│ Link: https://buffer.com
│ Workflow: Create content → Queue posts → AI optimizes timing
│
│ Tool: Later
│ Why: Visual content calendar + Instagram planning
│ Link: https://later.com
│ Specific Setup: Upload photos → AI suggests captions → Auto-post
│
│ Tool: Hootsuite
│ Why: Manage multiple accounts from one dashboard
│ Link: https://www.hootsuite.com
│ Workflow: Monitor mentions → Auto-respond → Track sentiment
└───────────────────────────────────────────────────────────────────────────┘

┌─ ADVERTISEMENT & PERFORMANCE AI ──────────────────────────────────────────┐
│ Tool: Facebook Ads Manager with AI
│ Why: Auto-optimize ad spend across platforms
│ Link: https://ads.facebook.com
│ Setup: Set budget → Define audience → AI learns & optimizes bids
│
│ Tool: Google Ads
│ Why: Search traffic + Display network automation
│ Link: https://ads.google.com
│ Workflow: Create campaign → AI adjusts bids hourly → Maximize ROI
│
│ Tool: AdEspresso
│ Why: A/B test ads across Facebook, Instagram, Google
│ Link: https://adespresso.com
│ Specific Setup: Test 10 variations → Winner scales 10x
└───────────────────────────────────────────────────────────────────────────┘

┌─ AUTOMATION & WORKFLOW AI ────────────────────────────────────────────────┐
│ Tool: Zapier
│ Why: Connect 1000+ apps, eliminate manual work
│ Link: https://zapier.com
│ Example Workflows:
│   • New email subscriber → Add to CRM → Send welcome email
│   • Form submission → Create task → Assign to team member
│   • Sale completes → Update inventory → Send confirmation
│
│ Tool: Make.com
│ Why: Advanced automation, better integrations than Zapier
│ Link: https://make.com
│ Specific Workflow: Ad click → Lead capture → CRM → Invoice → Payment
└───────────────────────────────────────────────────────────────────────────┘

┌─ SEO & ANALYTICS AI ──────────────────────────────────────────────────────┐
│ Tool: SEMrush
│ Why: Competitor analysis, SEO rankings, keyword research
│ Link: https://semrush.com
│ Setup: Analyze top 3 competitors → Find 50 keywords → Create content
│
│ Tool: Ahrefs
│ Why: Backlink analysis, content gap discovery
│ Link: https://ahrefs.com
│ Workflow: Find competitor content → Create better version → Earn links
└───────────────────────────────────────────────────────────────────────────┘

┌─ DESIGN & BRANDING AI ────────────────────────────────────────────────────┐
│ Tool: Canva Pro
│ Why: Create 1000s of designs without hiring designer
│ Link: https://canva.com
│ Workflow: Brand kit setup → Template library → Batch create → Schedule
└───────────────────────────────────────────────────────────────────────────┘


█ 2. HANDLING THE AI TEAM - CRITICAL WORKFLOWS

▓▓▓ AI #1: CUSTOMER CHAT AI ▓▓▓
Responsibility: Handle ALL customer inquiries automatically
Tool Stack: Tidio + Zapier + HubSpot

Prompt to Use:
"You are a helpful customer service representative for [COMPANY]. 
Respond to customer questions about [PRODUCTS/SERVICES]. 
If you can't help, collect their email and escalate to support@[DOMAIN]"

Training Data: FAQ document + Past customer conversations
Response Speed: Instant (seconds)
Escalation: Complex issues → Human team member

Real Example Workflow:
Customer asks "How much is shipping?"
→ Chatbot: "Shipping is FREE on orders over \$50"
→ Customer satisfied: Sale protected, no human needed
→ If confused: "Let me connect you with our team" → Escalates

▓▓▓ AI #2: SOCIAL MEDIA MANAGEMENT AI ▓▓▓
Responsibility: Create, schedule, and optimize all social content
Tool Stack: ChatGPT + Midjourney + Buffer + Analytics

Daily Workflow (Automated):
1. Use ChatGPT to write 5 captions for each platform
2. Use Midjourney to generate matching images
3. Upload everything to Buffer
4. Schedule across Instagram, TikTok, LinkedIn, Twitter
5. Zapier monitors analytics → reports on performance
6. Next day: Repurpose top performers for different platforms

Specific Prompts:
For Instagram: "Write a casual, engaging caption about [topic] with 3 emojis and a CTA"
For TikTok: "Write a script for a 30-second video about [topic]"
For LinkedIn: "Write professional, insightful post about [industry trend]"

▓▓▓ AI #3: ADVERTISEMENT AI ▓▓▓
Responsibility: Run ads that generate leads/sales on autopilot
Tool Stack: Facebook Ads + Google Ads + AdEspresso + Zapier

Setup (Do This Once):
1. Define audience size (minimum 500k people)
2. Create 5 ad variations in AdEspresso
3. Set daily budget (\$10-50)
4. Let AI run for 48 hours
5. Stop ads with CPC > \$3
6. Scale winners by 2x budget daily

Performance Metrics AI Monitors:
• Cost Per Click (CPC)
• Click-Through Rate (CTR)
• Conversion Rate
• Cost Per Lead
• Return on Ad Spend (ROAS)

Zapier automation: When lead acquired → Add to CRM → trigger Sales email


█ 3. MARKET RESEARCH & COMPETITOR ANALYSIS

How to Research:
1. Google Search: "[Your Business] + competitors"
2. SEMrush: Enter competitor domain → Get traffic breakdown
3. SimilarWeb: https://www.similarweb.com → See where traffic comes from
4. Ahrefs: Get competitor's top-performing content
5. Reddit/Twitter: Search conversations in your niche

Key Metrics to Analyze:
• Monthly traffic volume
• Cost per lead generated
• Customer acquisition cost
• Price points competitors charge
• Marketing channels they use (Ads, SEO, Social, Email)

Layman's Explanation:
Think of it like a spy mission. You're analyzing what your competitors do that works, 
then copying (legally) the best parts while making it 10% better.

Top 3 Competitors to Find:
1. Direct competitor (same product/service)
2. Adjacent competitor (same customer, different solution)
3. Industry leader (best practices model)


█ 4. PRODUCT RESEARCH & SOURCING

Where to Find Product Ideas:
• Amazon Best Sellers: https://amazon.com/Best-Sellers - See what's selling
• Etsy Trending: https://etsy.com - Check what's popular
• TikTok/Instagram: Use "Ads Library" to see what's being advertised
• Reddit: r/entrepreneur, r/SideHustle - What problems are people discussing?
• Quora: https://quora.com - Questions people are asking = Problems to solve

Product Sourcing Platforms:
• Alibaba: https://alibaba.com - Direct manufacturer connections
• Global Sources: https://globalsources.com - Vetted suppliers
• DHgate: https://dhgate.com - Dropshipping products
• Printful/Teespring: For t-shirts, hoodies, mugs

Vetting a Supplier:
✓ Check: Years in business, customer reviews, production certifications
✓ Order: Sample first (usually \$10-50)
✓ Inspect: Quality, packaging, shipping time
✓ Negotiate: Bulk discounts, payment terms, MOQ (minimum order quantity)
✓ Contract: Payment terms, lead times, quality standards


█ 5. LEGAL & BRAND SECURITY

Critical Steps (DO IMMEDIATELY):
1. Trademark Your Brand Name: https://tmsearch.uspto.gov/
   - Search US Patent Office
   - If clear → File trademark application (\$250-500)
   
2. Check Domain Availability: https://domains.google/
   - Secure YourBrand.com
   - Also grab .co, .io for backup
   
3. Check Social Media Handles: https://namechk.com/
   - Lock down Instagram, TikTok, LinkedIn, Twitter
   - Register all variations (with/without underscore)

4. Trademark Globally: https://branddb.wipo.int/
   - If selling internationally, protect brand in key markets
   - Priority: UK, Europe, Canada, Australia

5. Business Registration:
   - LLC vs Corporation (consult accountant)
   - Get EIN from IRS (free)
   - Open business bank account (separate from personal)

Compliance Checklist:
□ Business registration (LLC/Corp)
□ Tax ID (EIN)
□ Trademark registered
□ Domain registered  
□ Social handles secured
□ Privacy policy on website
□ Terms of service documented
□ Insurance (business liability)


█ 6. ZERO-TO-SCALE ROADMAP

╔═══════════════════════════════════════════════════════════════════════════╗
║ PHASE 1: FOUNDATIONS (Weeks 1-3)                                         ║
║ Goal: Build a working MVP and establish brand identity                   ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ Week 1: BRAND & LEGAL
║ Action Items:
║   □ Register business name + check domain availability
║   □ File trademark (https://tmsearch.uspto.gov/)
║   □ Create logo on Canva Pro
║   □ Write brand story (30-second elevator pitch)
║   □ Get business bank account
║
║ Week 2: DIGITAL PRESENCE
║ Action Items:
║   □ Set up website (Wix, Squarespace, or custom)
║   □ Create social media accounts (Instagram, TikTok, LinkedIn)
║   □ Set up email list (ConvertKit, Mailchimp)
║   □ Design email templates
║   □ Write sales page copy
║
║ Week 3: FIRST PRODUCT/SERVICE
║ Action Items:
║   □ Define MVP (Minimum Viable Product)
║   □ Source 1st batch of products OR document service
║   □ Create product photos (use Midjourney for mockups)
║   □ Write product descriptions
║   □ Set up payment processor (Stripe, PayPal)
║
╚═══════════════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════╗
║ PHASE 2: CONTENT & PROMOTION (Weeks 4-8)                                 ║
║ Goal: Build audience and test messaging                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ Week 4-5: VIRAL CONTENT BLUEPRINTS
║
║ INSTAGRAM VIRAL BLUEPRINT:
║ • Content Type: Carousel posts (educational) + Reels (entertaining)
║ • Best Time: Post 9am-12pm on Weekdays
║ • Viral Hook: "I spent \$10k to learn this..."
║ • Call to Action: "Save this" or "Tag someone"
║ • Tools: Later (schedule) + Canva (design)
║
║ TIKTOK VIRAL BLUEPRINT:
║ • Content Type: 15-60 second videos, trending sounds
║ • Format: Trend + Your twist + Call to Action
║ • Hook: First 2 seconds make/break the video
║ • Engagement: Respond to ALL comments in first hour
║ 
║ LINKEDIN VIRAL BLUEPRINT:
║ • Content Type: Personal stories + Industry insights
║ • Format: Hook → Story → Lesson → CTA
║ • Best Time: Tuesday-Thursday 8am-10am
║ • Engagement: Comment on 20 similar posts daily
║
║ YOUTUBE VIRAL BLUEPRINT:
║ • Content Type: 8-12 minute educational/How-to videos
║ • Thumbnail: Bold text + face making expression
║ • Hook: Tell what they'll learn in first 15 seconds
║ • SEO: Optimize title/description with keywords
║
║ Week 6: PAID ADVERTISING (Start Small)
║ Action Items:
║   □ Run Facebook/Instagram ads (\$100-500 test budget)
║   □ A/B test 5 ad variations
║   □ Track: Cost per click, conversion rate, ROAS
║   □ Scale only ads with ROAS > 300% (means \$1 in = \$3 in revenue)
║   □ Set up Zapier to track leads to CRM
║
║ Week 7: EMAIL & COMMUNITY BUILDING
║ Action Items:
║   □ Build email sequences (welcome, educational, sales)
║   □ Create lead magnet (free resource)
║   □ Build Facebook Group (community)
║   □ Host first webinar/workshop
║   □ Start email list growth to 1,000+ subscribers
║
║ Week 8: FIRST SALES & ITERATION
║ Action Items:
║   □ Analyze what content got engagement
║   □ Survey customers: What else do they need?
║   □ Create improved version 2.0
║   □ Plan next launch
║
╚═══════════════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════╗
║ PHASE 3: AUTOMATION (Weeks 9+)                                           ║
║ Goal: Run business while you sleep                                       ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║ THE COMPLETE AUTOMATION FUNNEL:
║
║ Step 1: TRAFFIC (Ads + Organic)
║ ├─ Facebook/Google Ads run continuously
║ ├─ Social media posts scheduled via Buffer
║ └─ SEO content generates passive traffic
║
║ Step 2: LEAD CAPTURE (Automatedforms)
║ ├─ Typeform collects emails/info
║ └─ Zapier immediately adds to CRM
║
║ Step 3: NURTURE (Email Sequences)
║ ├─ Welcome sequence (3 emails over 3 days)
║ ├─ Educational sequence (5 emails teaching value)
║ └─ Sales sequence (closes the deal)
║
║ Step 4: SALES (Checkout Automation)
║ ├─ Stripe processes payments instantly
║ ├─ Delivery automated (digital product or fulfillment)
║ └─ Zapier sends confirmation + access
║
║ Step 5: CUSTOMER SERVICE (AI Chatbots)
║ ├─ Tidio handles frequently asked questions
║ ├─ Escalates complex issues to your team
║ └─ Sends satisfaction surveys
║
║ ZAPIER AUTOMATION EXAMPLES:
║ • New subscriber email → Add to email sequence → Tag in CRM
║ • Sale completed → Update inventory → Post to Slack → Email confirmation
║ • Customer feedback poor → Alert support team → Offer refund
║ • Re-engagement needed → Subscriber inactive 30 days → Send win-back email
║
║ DAILY TIME COMMITMENT: 30-60 minutes
║ • Monitor Slack for alerts
║ • Check analytics/performance
║ • Respond to complex customer issues
║ • EVERYTHING ELSE IS ON AUTOPILOT
║
╚═══════════════════════════════════════════════════════════════════════════╝


█ 7. REVENUE SCALING CHECKLIST

First \$1,000: (1-3 months)
□ Have a working product/service
□ 500+ email subscribers
□ Making 10-20 sales
□ Average order value: \$50-100

First \$10,000/month: (3-6 months)
□ Paid ads working with 3:1 ROAS
□ Email list: 2,000+ subscribers
□ Multiple revenue streams
□ Customer testimonials + social proof

First \$100,000/revenue: (6-12 months)
□ Hiring first contractor/employee
□ Productized service or digital product
□ Strong brand reputation
□ Multiple traffic channels (ads, organic, partnership, PR)


█ 8. ONLINE COMMUNITIES TO JOIN & DOMINATE

⚡ REDDIT COMMUNITIES:
- r/entrepreneur (700k members) - General business discussion
- r/SideHustle (500k members) - Side business ideas
- r/ecommerce (200k members) - E-commerce specific
- r/Elearning (100k members) - Online course creators

Strategy: Answer 10x more questions than you ask. Build authority.

⚡ DISCORD COMMUNITIES:
- Indie Hackers Discord (10k+ members) - Startup community
- Twitter/X (Creator) spaces - Daily growth hacking sessions
- Skool Communities - Niche-specific paid communities

⚡ FACEBOOK GROUPS:
- Search: "[Your Niche] + Entrepreneurs"
- Find 10 groups with 5k-50k members
- Post valuable content 3x/week
- Direct message struggling members with solution

⚡ NICHE FORUMS:
- Quora.com - Answer questions related to your business
- Medium.com - Write articles establishing authority
- Dev.to / Substack - Build email list through content
- StartupSchool.org - Network with founders


█ 9. MUST-FOLLOW RESOURCES & INFLUENCERS

YOUTUBE CHANNELS FOR BUSINESS STRATEGY:
• MrBeast (Viral marketing, creative ideas) - 200M subscribers
  Watch: "How I Made \$6M in 7 Days"
  
• Alex Hormozi (Sales funnels, businesses) - 2M subscribers
  Watch: "$100M Offer" series
  
• Andrew Tate (Business fundamentals, mindset) - Controversial but valuable
  Watch: "How to start a business with zero experience"
  
• Gary Vee (Social media strategy, entrepreneurship) - 10M+ combined followers
  Watch: Daily NSFW show - Unfiltered business advice

PODCASTS:
• Tim Ferriss Show - Best interviews with entrepreneurs
• The GaryVee Audio Experience - Daily marketing insights
• How I Built This (NPR) - Founder origin stories
• Indie Hackers Podcast - Landing real businesses

BOOKS:
• "The Lean Startup" - Build minimum viable products
• "\$100M Offer" by Alex Hormozi - Create irresistible offers
• "DotCom Secrets" by Russell Brunson - Sales funnel blueprint
• "Traction" by Gabriel Weinberg - Growth strategies

TWITTER/X ACCOUNTS TO FOLLOW:
• @thisissethsblog - Marketing principles
• @alexhormozi - Sales & business
• @naval - Wealth creation
• @frankdesousa - Growth strategy
• @pomp - Crypto/business trends

WEBSITES & RESOURCES:
• Indie Hackers (https://www.indiehackers.com/) - Entire community
• ProductHunt (https://www.producthunt.com/) - Product launches
• Hacker News (https://news.ycombinator.com/) - Tech trends
• Trends.google.com - Find trending topics
• Answer The Public (https://answerthepublic.com/) - Question research


█ 10. FREE AI ALTERNATIVES (If Budget is Tight)

Instead of ChatGPT Pro (\$20/mo) → ChatGPT Free version (has 3-hour limit)
Instead of Midjourney (\$10-30/mo) → Stable Diffusion FREE or Leonardo.ai FREE
Instead of Canva Pro (\$120/year) → Canva Free (good enough for basics)
Instead of Jasper (\$39/mo) → Copy.ai FREE tier + ChatGPT
Instead of SEMrush (\$120/mo) → Ubersuggest (\$12/mo) or Free versions
Instead of HubSpot Pro → HubSpot Free CRM (emails limited to 200/day)
Instead of Mailchimp Pro → Mailchimp FREE for up to 3,000 contacts
Instead of Buffer Pro → Later Free (limited scheduling) or MeetEdgar FREE

TOTAL COST FOR 100% FREE SETUP:
- Free tier tools: \$0
- Basic hosting: \$3-5/mo
- Domain: \$12/year
= \$43-112 per year total

With \$100-500 budget:
+ Canva Pro (\$13/mo) = Better designs
+ Jasper/Copy.ai (\$39/mo) = Better content
+ One Udemy course (\$15) = Skills
= Professional tier setup


█ 11. 90-DAY ACTION PLAN (YOUR EXECUTION CHECKLIST)

▼ DAYS 1-7: FOUNDATION
□ Choose business idea ✓
□ Register domain ✓
□ Set up LLC/sole proprietorship ✓
□ Create social media accounts ✓
□ Design logo (Canva) ✓

▼ DAYS 8-14: DIGITAL PRESENCE
□ Build basic website ✓
□ Write sales page copy ✓
□ Create email template ✓
□ Set up Stripe payments ✓
□ Get first 100 email subscribers ✓

▼ DAYS 15-30: FIRST PRODUCT
□ Finalize product/service ✓
□ Create marketing materials ✓
□ Pre-sell to 5-10 people ✓
□ Get testimonials ✓
□ Adjust based on feedback ✓

▼ DAYS 31-60: MARKETING & SALES
□ Create 30 pieces of content ✓
□ Schedule content via Buffer ✓
□ Start running ads (\$100-500) ✓
□ Get first 50 paying customers ✓
□ Automate 50% of operations ✓

▼ DAYS 61-90: OPTIMIZATION & SCALE
□ Analyze what works ✓
□ Double ad budget for winners ✓
□ Build email marketing sequences ✓
□ Hire first contractor (if needed) ✓
□ Aim for \$5,000-10,000 revenue ✓

BY DAY 90: You should have a self-running business generating real revenue.


█ 12. CRITICAL SUCCESS FACTORS

WHY MOST FAIL:
• No audience/marketing: 80% of failures
• Poor product quality: 15% of failures
• Giving up too early: 5% of failures

HOW TO WIN:
1. Start with audience first, product second
2. Sell before you build (pre-sales = validation)
3. Focus on ONE channel until it works
4. Automate operational tasks, not customer interaction
5. Reinvest 50% of profits back into ads/growth

MINDSET > MONEY > MECHANICS

The biggest differentiator is daily action. Imperfect action today > Perfect action never.

═══════════════════════════════════════════════════════════════════════════════
                          YOUR BUSINESS STARTS TODAY
                    Pick ONE action from this plan. Do it today.
                        Tomorrow? Do the next one. Keep going.
═══════════════════════════════════════════════════════════════════════════════
"""
        response = {
            "status": "success",
            "data": {
                "message": fallback_plan,
                "from_ollama": False,
                "note": "Using comprehensive template. For live AI responses, ensure Ollama server is running."
            }
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)